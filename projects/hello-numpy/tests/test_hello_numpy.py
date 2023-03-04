# This kind of import is automatically done when importing hello from outside
import hello
import unittest
import numpy as np


class TestHello(unittest.TestCase):
    def test_hello(self):
        hello.hello()

    def test_return_two(self):
        expected = np.zeros((2, 2), dtype=np.float64)
        actual = hello.zeros2x2()
        self.assertEqual(expected.dtype, actual.dtype)
        self.assert_(np.all(expected == actual))


if __name__ == "__main__":
    unittest.main()
    # You can run all python test with:
    # ctest -R python -V
    # from the build folder
