from hello_f2py import hello


def test_hello(capfd):
    hello("World")
    captured = capfd.readouterr()
    assert captured.out == "Hello, World!\n"
