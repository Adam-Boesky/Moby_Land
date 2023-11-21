"""Test the clean_logger.py"""
import os
import sys

import matplotlib as mpl

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from Moby_Land.plotting.plotting_styles import (make_colors_gg,
                                                make_plots_scientific)


class Test_Plotting_Styles:
    def test_make_plots_scientific(self):

        # Call function
        make_plots_scientific()

        # Assert it make the right changes
        assert mpl.rcParams['font.family'][0] == 'serif'
        assert mpl.rcParams['font.serif'][0] == 'cmr10'
        assert mpl.rcParams['font.size'] == 12

        # Call function with optional argument
        make_plots_scientific(fs=45.2)

        # Assert it make the right changes
        assert mpl.rcParams['font.family'][0] == 'serif'
        assert mpl.rcParams['font.serif'][0] == 'cmr10'
        assert mpl.rcParams['font.size'] == 45.2

    def test_make_colors_gg(self):

        # Call function
        colors = make_colors_gg()

        # Assrt it gets the right colors
        gg_plot_colors = ['#E24A33', '#348ABD', '#988ED5', '#777777', '#FBC15E', '#8EBA42', '#FFB5B8']
        assert colors == gg_plot_colors
