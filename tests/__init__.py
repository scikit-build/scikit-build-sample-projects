"""This module defines functions used to test scikit-build-sample-projects."""

import _pytest.tmpdir
import errno
import os
import os.path
import py.path
import re
import six
import subprocess


SAMPLES_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../projects',
    )


class ContextDecorator(object):
    """A base class or mixin that enables context managers to work as
    decorators."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __enter__(self):
        # Note: Returning self means that in "with ... as x", x will be self
        return self

    def __exit__(self, typ, val, traceback):
        pass

    def __call__(self, func):
        @six.wraps(func)
        def inner(*args, **kwds):  # pylint:disable=missing-docstring
            with self:
                return func(*args, **kwds)
        return inner


def mkdir_p(path):
    """Ensure directory ``path`` exists. If needed, parent directories
    are created.

    Adapted from http://stackoverflow.com/a/600612/1539918
    """
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:  # pragma: no cover
            raise


class push_dir(ContextDecorator):
    """Context manager to change current directory.
    """
    def __init__(self, directory=None, make_directory=False):
        """
        :param directory:
          Path to set as current working directory. If ``None``
          is passed, ``os.getcwd()`` is used instead.

        :param make_directory:
          If True, ``directory`` is created.
        """
        self.directory = None
        self.make_directory = None
        self.old_cwd = None
        super(push_dir, self).__init__(
            directory=directory, make_directory=make_directory)

    def __enter__(self):
        self.old_cwd = os.getcwd()
        if self.directory:
            if self.make_directory:
                mkdir_p(self.directory)
            os.chdir(self.directory)
        return self

    def __exit__(self, typ, val, traceback):
        os.chdir(self.old_cwd)


def _tmpdir(basename):
    """This function returns a temporary directory similar to the one
    returned by the ``tmpdir`` pytest fixture.
    The difference is that the `basetemp` is not configurable using
    the pytest settings."""

    # Adapted from _pytest.tmpdir.tmpdir()
    basename = re.sub(r"[\W]", "_", basename)
    max_val = 30
    if len(basename) > max_val:
        basename = basename[:max_val]

    # Adapted from _pytest.tmpdir.TempdirFactory.getbasetemp()
    try:
        basetemp = _tmpdir._basetemp
    except AttributeError:
        temproot = py.path.local.get_temproot()
        user = _pytest.tmpdir.get_user()

        if user:
            # use a sub-directory in the temproot to speed-up
            # make_numbered_dir() call
            rootdir = temproot.join('pytest-of-%s' % user)
        else:
            rootdir = temproot

        rootdir.ensure(dir=1)
        basetemp = py.path.local.make_numbered_dir(prefix='pytest-',
                                                   rootdir=rootdir)

    # Adapted from _pytest.tmpdir.TempdirFactory.mktemp
    return py.path.local.make_numbered_dir(prefix=basename,
                                           keep=0, rootdir=basetemp,
                                           lock_timeout=None)


def _copy_dir(target_dir, entry, on_duplicate='exception', keep_top_dir=False):

    if isinstance(entry, six.string_types):
        entry = py.path.local(entry)

    # Copied from pytest-datafiles/pytest_datafiles.py (MIT License)
    basename = entry.basename
    if keep_top_dir:
        if on_duplicate == 'overwrite' or not (target_dir / basename).exists():
            entry.copy(target_dir / basename)
        elif on_duplicate == 'exception':
            raise ValueError(
                "'%s' already exists (entry %s)" % (basename, entry)
                )
        # else: on_duplicate == 'ignore': do nothing with entry
    else:
        # Regular directory (no keep_top_dir). Need to check every file
        # for duplicates
        if on_duplicate == 'overwrite':
            entry.copy(target_dir)
            return
        for sub_entry in entry.listdir():
            if not (target_dir / sub_entry.basename).exists():
                sub_entry.copy(target_dir / sub_entry.basename)
                continue
            if on_duplicate == 'exception':
                # target exists
                raise ValueError(
                    "'%s' already exists (entry %s)" % (
                        (target_dir / sub_entry.basename),
                        sub_entry,
                        )
                    )
            # on_duplicate == 'ignore': do nothing with e2


def initialize_git_repo_and_commit(project_dir, verbose=True):
    """Convenience function creating a git repository in ``project_dir``.

    If ``project_dir`` does NOT contain a ``.git`` directory, a new
    git repository with one commit containing all the directories and files
    is created.
    """
    if isinstance(project_dir, six.string_types):
        project_dir = py.path.local(project_dir)

    if project_dir.join('.git').exists():
        return

    # If any, exclude virtualenv files
    project_dir.join(".gitignore").write(".env")

    with push_dir(str(project_dir)):
        for cmd in [
            ['git', 'init'],
            ['git', 'config', 'user.name', 'scikit-build'],
            ['git', 'config', 'user.email', 'test@test'],
            ['git', 'add', '-A'],
            ['git', 'reset', '.gitignore'],
            ['git', 'commit', '-m', 'Initial commit']
        ]:
            do_call = (subprocess.check_call
                       if verbose else subprocess.check_output)
            do_call(cmd)


def prepare_project(project, tmp_project_dir, force=False):
    """Convenience function setting up the build directory ``tmp_project_dir``
    for the selected sample ``project``.

    If ``tmp_project_dir`` does not exist, it is created.

    If ``tmp_project_dir`` is empty, the sample ``project`` is copied into it.
    Specifying ``force=True`` will copy the files even if ``tmp_project_dir``
    is not empty.
    """
    if isinstance(tmp_project_dir, six.string_types):
        tmp_project_dir = py.path.local(tmp_project_dir)

    # Create project directory if it does not exist
    if not tmp_project_dir.exists():
        tmp_project_dir = _tmpdir(project)

    # If empty or if force is True, copy project files and initialize git
    if not tmp_project_dir.listdir() or force:
        _copy_dir(tmp_project_dir, os.path.join(SAMPLES_DIR, project))


def project_test(project, tmp_dir=None, verbose_git=True):

    def dec(fun):

        @six.wraps(fun)
        def wrapped(*iargs, **ikwargs):

            if wrapped.tmp_dir is None:
                wrapped.tmp_dir = _tmpdir(fun.__name__)
                prepare_project(wrapped.project, wrapped.tmp_dir)
                initialize_git_repo_and_commit(
                    wrapped.tmp_dir, verbose=wrapped.verbose_git)

            with push_dir(str(wrapped.tmp_dir)):
                result2 = fun(*iargs, **ikwargs)

            return wrapped.tmp_dir, result2

        wrapped.project = project
        wrapped.tmp_dir = tmp_dir
        wrapped.verbose_git = verbose_git

        return wrapped

    return dec


def install_skbuild(virtualenv):
    # virtualenv.install_ package('scikit-build', installer='pip')
    virtualenv.run("pip install /home/jcfr/Projects/scikit-build")


def run_setup(virtualenv, commands):
    install_skbuild(virtualenv)
    virtualenv.run("python setup.py %s" % " ".join(commands), cd=os.curdir)
