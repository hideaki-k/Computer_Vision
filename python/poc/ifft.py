import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as sfft
import matplotlib.mlab as mlab
import scipy.signal as ss
import cis

y,fs = cis.wavread('audio/domiso.wav')
fftlen =256
noverlap=128
S,_,_=mlab.specgram(y,Fs=fs,NFFT=fftlen,window=np.hanning(fftlen),noverlap=noverlap,mode='complex',sides='twosided')
slen = S.shape[1]
S = sfft.fftshift(S,axes=0)
ry = np.zeros(slen*fftlen-(slen-1)*noverlap)
k1 = 0
for k in range(0,slen):
    ry[k1:k1+fftlen]=ry[k1:k1+fftlen]+np.real(sfft.ifft(S[:,k]))
    k1=k1+noverlap
plt.plot(ry)
plt.show()
cis.audioplay(ry,fs)
cis.audioplay(y,fs)