import pytest
from myplotlib.colors.colormaps import CMAPS
import matplotlib.pyplot as plt
import myplotlib

__author__ = ["Riccardo Biondi"]
__email__ = ["riccardo.biondi7@unibo.it"]


registered_cmaps = plt.colormaps()
custom_cmaps = CMAPS.keys()


class TestColorMapRegistration:

    @pytest.mark.parametrize(
        "cmap", custom_cmaps)
    def test_is_registered(self, cmap):

        assert cmap in registered_cmaps
    
    @pytest.mark.parametrize(
        "cmap", custom_cmaps
    )
    def test_get_map(self, cmap):

        res = plt.get_cmap(cmap)

        assert res is not None