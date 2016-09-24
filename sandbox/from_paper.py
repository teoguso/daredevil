from __future__ import print_function
import numpy as np
import adaptfilt as adf
import scipy
from scipy import signal
#from scipy import fromfile, complex64
import matplotlib.pyplot as plt

path = "../example_data/ch0.cfile"
ch0 = scipy.fromfile(path, dtype=scipy.complex64)
path = "../example_data/ch1.cfile"
ch1 = scipy.fromfile(path, dtype=scipy.complex64)

print(ch0.shape)
print(ch1.shape)
# Let's cut it VERY short
ch0 = ch0[:len(ch0)/100]
# Cut files to the same length
if len(ch1) < len(ch0):
    ch0 = ch0[:len(ch1)]
else:
    ch1 = ch1[:len(ch0)]
print(ch0.shape)
print(ch1.shape)

N = len(ch0) # Number of samples
# Sampling frequency
f_s = 1E6*1.0
# Sampling period
T_s = 1/f_s
# plt.plot(ch0.imag)
# Doppler frequency range
f_dop = np.arange(-120,120,step=1)
# time delay range
R = 500
l = np.arange(R)

corr = np.zeros((len(ch1)-R,len(f_dop)))

for i in range(R,len(ch1)):
    for j in range(len(f_dop)):
        # shift_ch1[i] = ch1[i-R]
        corr[i,j] = signal.fftconvolve(ch0[i],ch1[i-R]*np.exp(-1j*2*np.pi*f_dop[j]/(len(ch1)-R)))
# shift_ch1[i:i+1] = ch1[i-R,i-R+1]

# corr = signal.fftconvolve(ch0,ch1)

print(corr[0])
plt.plot(corr.real)
plt.plot(corr.imag)
plt.figure()
plt.plot(corr.real, corr.imag)
plt.show()

