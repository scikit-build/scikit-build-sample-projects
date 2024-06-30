import freecomputepi.comp
import freecomputepi.pure
import freecomputepi.pybind
import pytest


@pytest.mark.parametrize("threads", [0, 1, 2, 4])
def test_pure(threads):
    π = freecomputepi.pure.pi_in_threads(threads, 10_000_000)
    assert π == pytest.approx(3.1415926535, rel=0.01)


@pytest.mark.parametrize("threads", [0, 1, 2, 4])
def test_comp(threads):
    π = freecomputepi.comp.pi_in_threads(threads, 100_000_000)
    assert π == pytest.approx(3.1415926535, rel=0.01)


@pytest.mark.parametrize("threads", [0, 1, 2, 4])
def test_pybind(threads):
    π = freecomputepi.pybind.pi_in_threads(threads, 100_000_000)
    assert π == pytest.approx(3.1415926535, rel=0.01)
