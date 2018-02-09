# Setup test environment

```
git clone git://github.com/jcfr/scikit-build -b find-f2py-rebased

git clone git://github.com/scikit-build/scikit-build-sample-projects.git -b add-f2py-sample-projects

mkvirtualenv -p python3.5 scikit-build-35
pip install -e ./scikit-build

cd scikit-build-sample-project/hello-f2py
python setup.py develop
```

# Run tests

```
$ cd scikit-build-sample-project/hello-f2py
$ python -m hello
Traceback (most recent call last):
  File "/usr/lib/python3.5/runpy.py", line 170, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/lib/python3.5/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/home/jcfr/Projects/scikit-build-sample-projects/projects/hello-f2py/hello/__main__.py", line 3, in <module>
    from . import _cylinder_methods as cylinder_methods
ImportError: /home/jcfr/Projects/scikit-build-sample-projects/projects/hello-f2py/hello/_cylinder_methods.cpython-35m-x86_64-linux-gnu.so: undefined symbol: PyFortran_Type
```

```
$ cd scikit-build-sample-project/hello-f2py
$ python -m hello_auto 
Cylinder of radius [0.5] and height [3] has an area of [10.995574593544006]
```
