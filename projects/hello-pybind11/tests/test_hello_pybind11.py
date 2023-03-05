# This kind of import is automatically done when importing hello from outside
import unittest

import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        hello.hello()

    def test_return_two(self):
        self.assertEqual(hello.return_two(), 2)


if __name__ == "__main__":
    unittest.main()
    # You can run all python test with:
    # ctest -R python -V
    # from the build folder
