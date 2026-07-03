import hello


def test_add():
    assert hello.add(2, 3) == 5


def test_greet():
    assert hello.greet("World") == "Hello, World!"
