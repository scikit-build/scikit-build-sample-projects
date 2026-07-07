from ._hello import lib

__all__ = ["square"]


def square(n: int) -> int:
    return lib.square(n)
