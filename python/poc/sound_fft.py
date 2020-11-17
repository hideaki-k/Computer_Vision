import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as sfft
import matplotlib.mlab as mlab
import scipy.signal as ss
import cis

fs = 100
t = np.arange(0,7,1/fs)
y = np.sin(2*np.pi*15*t)+np.cos(2*np.pi*40*t)
cs = sfft.fft(y[:600])
plt.plot(np.abs(cs))
plt.show()

print(cs.shape)
print(np.abs(cs[297:304]))
print((np.abs(cs)>250).nonzero())
print(cs[90])

plt.plot(np.abs(sfft.fft(y[0:599])))
plt.show()
plt.plot(np.abs(sfft.fft(y[0:601])))
plt.show()

w = np.hanning(600)
plt.plot(w)
plt.show()

hy = y[:599]*np.hanning(599)
plt.plot(hy)
plt.show()

hcs = sfft.fft(hy)
plt.plot(np.abs(hcs))
lcs = sfft.fft(y[:599])
plt.plot(np.abs(lcs),":")
plt.show()

y,fs = cis.wavread("audio/domiso.wav")
plt.plot(np.abs(sfft.fft(y)))
plt.show()

plt.plot(np.abs(sfft.fft(y[1300:1812]*np.hanning(512))))
plt.show()

S,F,T = mlab.specgram(y,Fs=fs,NFFT=256,window=np.hanning(256),noverlap=128,mode='complex',sides='twosided')
print(S.shape)

_,_,_,_= plt.specgram(y,Fs=fs,NFFT=256,window=np.hanning(256),noverlap=128)
_ = plt.xlabel('Time(s)')
_ = plt.ylabel('Frequency (Hz)')
plt.show()