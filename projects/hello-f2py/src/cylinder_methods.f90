subroutine calculate_area(radius, height, area_out)

! Calculate the surface area of a cylinder.
!
! Declare variables and constants.
! constants=pi
! variables=radius, height and area

  implicit none    ! Require all variables to be explicitly declared

  real*8 :: radius, height, area
  real*8, parameter :: pi = 3.141592653589793
  real*8, intent(OUT) :: area_out

!   Compute area.  The ** means "raise to a power."

  area = 2*pi * (radius**2 + radius*height)

  area_out = area

  return

end subroutine calculate_area
