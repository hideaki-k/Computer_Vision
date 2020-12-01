import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as sfft
import matplotlib.mlab as mlab
import scipy.signal as ss
import cis
import time

fs = 8000
t = np.arange(0,1,1/fs)
s = np.sin(2*np.pi*800*t) + np.sin(2*np.pi*500*t)
cis.audioplay(s, fs)
rg = np.arange(0, 100)
plt.subplot(3, 1, 1);plt.plot(s[rg])
sd = np.roll(s,5)
plt.subplot(3, 1, 2);plt.plot(sd[rg])
cis.audioplay(sd, fs)
ssd = s+sd
plt.subplot(3,1,3);plt.plot(ssd[rg])
plt.show()
cis.audioplay(ssd,fs)

print(t.shape)
r = np.random.standard_normal(t.shape)
print(r)
r = 0.8*r/np.max(np.abs(r))
n = np.arange(0,100)
plt.plot(t[n],r[n])
plt.show()
cis.audioplay(r,fs)

s = np.sin(2*np.pi*440*t)
sn = 0.8*s + 0.25*r
n = np.arange(0,100)
plt.plot(t[n],sn[n],t[n],0.8*s[n])
plt.show()
cis.audioplay(sn,fs)

y = np.zeros(sn.shape)
pn = 3
for k in np.arange(pn-1,t.shape[0]):
    print(k)
    y[k] = np.mean(sn[k-pn+1:k+1])
    
plt.plot(t[n],sn[n],t[n],y[n],t[n],0.8*s[n])
plt.show()
cis.audioplay(sn,fs) # 雑音交じりの音
time.sleep(1)
cis.audioplay(y,fs) # フィルタの出力
time.sleep(1)
cis.audioplay(s,fs) # 現信号