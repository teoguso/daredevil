import scipy
import sys
import matplotlib.pyplot as plt  

dataLen = 1000;

ch0 = scipy.fromfile(open("../example_data/ch0.cfile"), dtype = scipy.complex64, count = dataLen)

ch1 = scipy.fromfile(open("../example_data/ch1.cfile"), dtype = scipy.complex64, count = dataLen)

fig1 = plt.figure()
plt.plot(ch0)

plt.show()



