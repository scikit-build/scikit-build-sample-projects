import math

import pytest
from pi import pi


def test_estimate_pi():
    pi_est = pi.estimate_pi(1e8)
    assert pi_est == pytest.approx(math.pi, rel=0.001)
