from __future__ import print_function
import numpy as np
#import adaptfilt as adf
import scipy
from scipy import signal
#from scipy import fromfile, complex64
import matplotlib.pyplot as plt
import math


# Read in data
ch0 = scipy.fromfile("../new_example/ch0.cfile", dtype=scipy.complex64, count = 15000 )
ch1 = scipy.fromfile("../new_example/ch1.cfile", dtype=scipy.complex64, count =  15000 )

#print("Array lengths differ by " + abs(ch0.shape - ch0.shape) +" samples.")

###
bucketSize = 100;
N = len(ch0) # Number of samples
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

corr = np.zeros((bucketSize, len(f_dop), bNum), dtype=complex)

for bi in range( bNum ):
	iStart = bi * bucketSize
	iEnd = iStart + bucketSize - 1
	i0 = 0	
	for i in range(iStart, iEnd):

		for j in range(len(f_dop)):
			corr[i0,j, bi] = ch0[i]  * ch1[i] * np.exp(-1 * j *2*np.pi*f_dop[j]/(len(ch1)))
			
			
		i0 = i0 + 1
		
		
print(corr.shape)


#Display
	

ax = plt.subplot(111)

quad = plt.pcolormesh(Log(corr[:,:,0].real))

plt.colorbar()

plt.ion()
plt.show()

for bi in range(1, bNum) :

    quad.set_array(Log(corr[:,:,bi].real).ravel())
    plt.draw()

plt.ioff()
plt.show()
#print(corr)
