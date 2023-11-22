"""Test the conversions.py"""
import os
import sys
import numpy as np
from typing import Optional

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from Moby_Land.astro.conversions import (ab_mag_to_flux, flux_to_ab_mag, ab_magerr_to_ferr, err_to_logerr)

# Values that correspond to eachother
MAG_VAL, FLUX_VAL, SIGMA_M, FERR = 3, 42.1, 0.2, 7.755106593203947
VAL, VAL_ERR, VAL_LOGERR = 3.1, 0.2, 0.8494660083746389


def is_near(val1: float, val2: float, thresh: Optional[float] = 10E-8) -> bool:
    """Check if a value is within a threshold from another."""
    delta = val1 - val2
    return (-1.0 * thresh < delta) | (thresh > delta)


class Test_Conversions:
    def test_ab_mag_to_flux(self):
        assert is_near(ab_mag_to_flux(MAG_VAL), FLUX_VAL)
        assert is_near(ab_mag_to_flux(np.array([MAG_VAL])), np.array([FLUX_VAL]))


    def test_ab_mag_to_flux(self):
        assert is_near(flux_to_ab_mag(FLUX_VAL), MAG_VAL)
        assert is_near(flux_to_ab_mag(np.array([FLUX_VAL])), np.array([MAG_VAL]))


    def test_ab_maggerr_to_ferr(self):
        assert is_near(ab_magerr_to_ferr(SIGMA_M, FLUX_VAL), FERR)
        assert is_near(ab_magerr_to_ferr(np.array([SIGMA_M]), np.array([FLUX_VAL])), np.array([FERR]))


    def test_err_to_logerr(self):
        assert is_near(err_to_logerr(VAL_ERR, VAL), VAL_LOGERR)
        assert is_near(err_to_logerr(np.array([VAL_ERR]), np.array([VAL])), np.array([VAL_LOGERR]))
