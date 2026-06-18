from imageio.plugins import grab
from pymodaq.control_modules.viewer_utility_classes import main, DAQ_Viewer_base
from pymodaq_plugins_mockexamples.daq_viewer_plugins.plugins_2D.daq_2Dviewer_BSCamera import DAQ_2DViewer_BSCamera
import imageio.v3 as iio
import laserbeamsize as lbs

class DAQ_2DViewer_BeamProfiler(DAQ_2DViewer_BSCamera):
    pass
    # def grab_data(self, Naverage=1, **kwargs):
    #     data=self.average_data(Naverage)
    #     data_array2D=data.get_data_from_name('Mock2D').data[0]




if __name__ == '__main__':
    main(__file__)
