
if __name__ == "__main__":
    from . import _hello as hello
    hello.hello("World")
    print("Elevation of Nevado Sajama is %d feet" % hello.size())
