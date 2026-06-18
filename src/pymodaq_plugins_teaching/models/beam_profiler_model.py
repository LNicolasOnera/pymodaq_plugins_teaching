import numpy as np

from pymodaq.extensions.data_mixer.model import DataMixerModel, np  # np will be used in method eval of the formula

from pymodaq_utils.math_utils import gauss1D, my_moment

from pymodaq_data.data import DataToExport, DataWithAxes, DataCalculated, DataDim
from pymodaq_gui.parameter import Parameter

from pymodaq.extensions.data_mixer.parser import (
    extract_data_names, split_formulae, replace_names_in_formula)

import laserbeamsize as lbs

def gaussian_fit(x, amp, x0, dx, offset):
    dx = np.abs(dx)
    return amp * gauss1D(x, x0, dx) + offset


class DataMixerGaussianFitModel(DataMixerModel):

    def process_dte(self, dte: DataToExport):

        dte_processed=DataToExport('computed') #initialisation
        data_array_2D=dte.get_data_from_name('BSCamera')

        x, y, d_major, d_minor, phi = lbs.beam_size(data_array_2D)

        if True:
            dte.append(DataCalculated('BeamSizeXY',
                                      data=[np.atleast_1d(x),
                                            np.atleast_1d(y), ],
                                      labels=['X', 'Y'], ))
        if True:
            dte.append(DataCalculated('BeamSizeDXDY',
                                      data=[np.atleast_1d(d_major),
                                            np.atleast_1d(d_minor), ],
                                      labels=['Dmajor', 'Dminor'], ))
        if True:
            dte.append(DataCalculated('BeamSizePhi',
                                      data=[np.atleast_1d(phi), ],
                                      labels=['Phi', ], ))
        return dte_processed


