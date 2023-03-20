! generate a signature file from this file with:
! $ python -m numpy.f2py hello.f90 -m _hello -h _hello.pyf
! and edit if helpful (see F2PY docs)
subroutine hello(a)
    character(len=*) :: a
    print "(a)", "Hello, " // a // "!"
end subroutine hello
