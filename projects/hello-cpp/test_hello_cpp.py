import hello


def test_hello(capfd):
    hello.hello("World")
    captured = capfd.readouterr()
    assert captured.out == "Hello, World!"


def test_elevation():
    assert hello.elevation() == 21463
