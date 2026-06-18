import numpy as np
from pymodaq.control_modules.viewer_utility_classes import main
from pymodaq_data import DataCalculated, DataToExport

from pymodaq_plugins_mockexamples.daq_viewer_plugins.plugins_2D.daq_2Dviewer_BSCamera import DAQ_2DViewer_BSCamera

import laserbeamsize as lbs


class DAQ_2DViewer_BeamProfiler(DAQ_2DViewer_BSCamera):

    params = DAQ_2DViewer_BSCamera.params + [
        {'title': 'BeamSizeOptions', 'name': 'options', 'type': 'group',
         'children': [
             {'title': 'XY', 'name': 'plot_xy', 'type': 'bool', 'value': True},
             {'title': 'DXDY', 'name': 'plot_dxdy', 'type': 'bool_push', 'value': True},
             {'title': 'Phi', 'name': 'plot_phi', 'type': 'led', 'value': True},]}
    ]

    def ini_detector(self, controller=None):
        info, initialized = super().ini_detector(controller)
        self.settings.child('options', 'plot_phi').show()
        return info, initialized


    def grab_data(self, Naverage=1, **kwargs):
        dte = self.average_data(Naverage)

        data_array_2D = dte.get_data_from_name('BSCamera')[0]
        #calculation
        x, y, d_major, d_minor, phi = lbs.beam_size(data_array_2D)

        if self.settings['options', 'plot_xy']:
            dte.append(DataCalculated('BeamSizeXY',
                                      data=[np.atleast_1d(x),
                                            np.atleast_1d(y), ],
                                      labels=['X', 'Y'],))
        if self.settings.child('options', 'plot_dxdy').value():
            dte.append(DataCalculated('BeamSizeDXDY',
                                      data=[np.atleast_1d(d_major),
                                            np.atleast_1d(d_minor),],
                                      labels=['Dmajor', 'Dminor'],))
        if self.settings['options', 'plot_phi']:
            dte.append(DataCalculated('BeamSizePhi',
                                      data=[np.atleast_1d(phi),],
                                      labels=['Phi',],))

        self.dte_signal.emit(dte)


if __name__ == '__main__':
    main(__file__)
