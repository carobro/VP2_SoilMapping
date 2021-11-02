import numpy as np
import scipy
from osgeo import gdal
from skimage import exposure
from skimage.segmentation import quickshift
import time

naip_fn = 'F:/Sursee_2020/2020-10-22_adi_Wetzwil-Mspec/img/MSP_00251_00005.tif'

driverTiff = gdal.GetDriverByName('GTiff')

naip_ds = gdal.Open(naip_fn)
nbands = naip_ds.RasterCount
band_data = []

print('bands', naip_ds.RasterCount, 'rows', naip_ds.RasterYSize, 'columns', naip_ds.RasterXSize)
for i in range(1, nbands+1):
        band = naip_ds.GetRasterBand(i).ReadAsArray()
        band_data.append(band)

band_data = np.dstack(band_data)
print(band_data.shape)


# scale image values from 0.0 - 1.0
img = exposure.rescale_intensity(band_data)

# do segmentation multiple options with quickshift and slic
seg_start = time.time()
# segments = quickshift(img, convert2lab=False)
# segments = quickshift(img, ratio=0.8, convert2lab=False)
# segments = quickshift(img, ratio=0.99, max_dist=5, convert2lab=False)
# segments = slic(img, n_segments=100000, compactness=0.1)
# segments = slic(img, n_segments=500000, compactness=0.01)
segments = slic(img, n_segments=500000, compactness=0.1)
print('segments complete', time.time() - seg_start)

# save segments to raster
segments_fn = 'C:/Users/st1154414/Desktop/VP2/Processed/segments.tif'
segments_ds = driverTiff.Create(segments_fn, naip_ds.RasterXSize, naip_ds.RasterYSize,
                                1, gdal.GDT_Float32)
segments_ds.SetGeoTransform(naip_ds.GetGeoTransform())
segments_ds.SetProjection(naip_ds.GetProjectionRef())
segments_ds.GetRasterBand(1).WriteArray(segments)
segments_ds = None