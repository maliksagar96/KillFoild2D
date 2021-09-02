import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import tiff_file
from bpass import bpass

coord_all = np.load('fov0/MT_featsize_19.npy')
# for multi frames
coord = coord_all[np.where(coord_all[:,5]==0)]
# for single frame
#coord = np.load('fov0/MT_featsize_19.npy') 
x = np.array(coord[:,0])
y = np.array(coord[:,1])

image0 = tiff_file.imread('Data_0000.tif')
#image0 = tiff_file.imread('/media/hdd2/08June2021/OD1.52_fps30_3/Data_0000.tif')  #single frame
image = image0[:,:]
#image = image0[0,:,:]
print(image.shape)
#exit()
image = np.transpose(image,(1,0))


fig = plt.figure()
implot=plt.imshow(image,'gray',interpolation='none',origin='lower')
n = plt.plot(y,x,'go',markeredgecolor='b',markersize=2,label='Weeks')
plt.show()
