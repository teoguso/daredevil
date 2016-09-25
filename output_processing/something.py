import numpy as np
import scipy
import time
from scipy import signal
import matplotlib.pyplot as plt
import math


# Read in data
ch0 = scipy.fromfile("../new_example/ch0.cfile", dtype=scipy.complex64, count=15000)
ch1 = scipy.fromfile("../new_example/ch1.cfile", dtype=scipy.complex64, count=15000)

#print("Array lengths differ by " + abs(ch0.shape - ch0.shape) +" samples.")

###
bucketSize = 100
N = len(ch0) # Number of samples
# Number of sample buckets
bNum = int(math.floor( N / bucketSize))
# Sampling frequency
f_s = 1E6*1.0
# Sampling period
T_s = 1/f_s
# plt.plot(ch0.imag)
# Doppler frequency range
f_dop = np.arange(0,120,step=1)
# time delay range
R = 500
R = 100

# corr = np.zeros((bucketSize, len(f_dop), bNum), dtype=np.complex64)
corr_tmp = np.zeros((R,len(f_dop)), dtype=np.complex64)
print(corr_tmp.shape)

plt.ion()

for bi in range( bNum ):
    iStart = bi * bucketSize
    # iEnd = iStart + bucketSize - 1
    # i0 = 0
    den_1 = 1/R
    for i in range(R):
        for j in range(len(f_dop)):

            # This equation is wrong, there must be a shift between ch0 and ch1
            # corr[i0,j, bi] = ch0[i]  * ch1[i] * np.exp(-1j *2*np.pi*f_dop[j]/(len(ch1)))
            corr_tmp[i, j] = ch0[i+iStart]  * ch1[i+iStart-j] * np.exp(-1j *2*np.pi*f_dop[j]*den_1)

    plt.clf()
    # plt.plot(np.sin(np.arange(100)/float(bi+1)))
    plt.title("Bin number "+str(bi))
    plt.pcolormesh(np.log(corr_tmp.real))
    plt.pause(0.001)

            # i0 = i0 + 1




#Display


# ax = plt.subplot(111)

# quad = plt.pcolormesh(np.log(corr_tmp.real))

# plt.colorbar()
# plt.plot(np.sin(np.arange(100)))

# plt.show()

# for i in range(20):
#     plt.plot(np.sin(np.arange(100)/float(i+1)))
#     plt.pause(0.05)
#     plt.clf()

# for bi in range(1, bNum) :
#
#     quad.set_array(np.log(corr_tmp.real).ravel())
#     plt.draw()

plt.ioff()
plt.show()
#print(corr)
