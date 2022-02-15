import hello


def test_hello():
    hello.hello()


def test_return_two():
    assert hello.return_two() == 2
