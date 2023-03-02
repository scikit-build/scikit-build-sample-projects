      subroutine estimate_pi(pi_estimated, num_trials)
C     Estimate pi using Monte Carlo
      integer num_trials, num_in_circle
      real*8 pi_estimated, x, y
Cf2py intent(in) num_trials
Cf2py intent(out) pi_estimated

      num_in_circle = 0d0
      do i = 1, num_trials
          call random_number(x)
          call random_number(y)
          if (x**2 + y**2 < 1.0d0) then
              num_in_circle = num_in_circle + 1
          endif
      end do
      pi_estimated = (4d0 * num_in_circle) / num_trials
      end subroutine estimate_pi
