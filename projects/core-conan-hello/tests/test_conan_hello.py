import conan_hello


def test_greet():
    assert conan_hello.greet("World") == "Hello, World!"
