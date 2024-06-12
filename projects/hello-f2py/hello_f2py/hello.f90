! generate a signature file from this file with:
! $ python -m numpy.f2py hello.f90 -m _hello -h _hello.pyf
! and edit if helpful (see F2PY docs)
subroutine hello(a)
    use, intrinsic :: iso_fortran_env
    character(len=*) :: a
    print '(A)', 'Hello, ' // a // '!'
    flush(OUTPUT_UNIT)
end subroutine hello
