import mpretrack
import fancytrack
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import os


basepath = '/home/sagar/Documents/codes/python/untouched/'
#for i in range(5000):

fname = 'Data_0000.tif'
numframes = 1   #total number of frames in the stack
time = np.arange(0,numframes)
np.save(os.path.join(basepath, "fov0_times.npy"),time)

#mpretrack.test(basepath,fovn=0,frame=3,featuresize=6,masscut=0,Imin=0, barI=None, barRg=None, barCc=None, IdivRg=None, field=2)

mpretrack.run(basepath, fname, fovn=0, numframes=1, featuresize=19, masscut=13000, Imin=0, barI=None, barCc=None, barRg=None, IdivRg=None, field=2)

#fancytrack.run(basepath, fovn=0, featuresize=6, maxdisp=20, goodenough=4, memory=2)
