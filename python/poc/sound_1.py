import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as sfft
import matplotlib.mlab as mlab
import scipy.signal as ss
import cis

fs = 8000
t = np.arange(0, 1, 1/fs)
a = 0.3
y523 = a*np.sin(2*np.pi*523*t)
y660 = a*np.sin(2*np.pi*660*t)
y784 = a*np.sin(2*np.pi*784*t)
yy = y523 + y660 + y784
y438 = a*np.sin(2*np.pi*438*t)
y442 = a*np.sin(2*np.pi*442*t)
yy = y438+y442
#cis.audioplay(yy, fs)
v1 = np.arange(0,3)
v2 = np.arange(3,5)
v3 = np.arange(5,9)
v = np.hstack((v1,v2,v3))
print(v)
cis.audioplay(np.hstack((y523,y660,y442)),fs)
r = np.arange(200)
plt.plot(t[r],yy[r])
plt.show()

