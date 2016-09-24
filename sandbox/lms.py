from __future__ import print_function
import numpy as np
import adaptfilt as adf
import scipy
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
# plt.plot(ch0.imag)
# plt.plot(ch1.imag)
# plt.plot(ch1.imag-ch0.imag)
# plt.show()

# AS SEEN ON https://pypi.python.org/pypi/adaptfilt/0.2
# This implementation tries to remove echoes from the total signal,
# we might be able to use it to do the opposite
# WARNING: we have complex signals while this is designed to work
# with real data (sound)

# u(n) is the main signal (from the big radar source supposedly)

u = ch0.imag

# d is the total signal (with echoes and everything)

d = ch1.imag

# Apply adaptive filter

M = 100  # Number of filter taps in adaptive filter
step = 0.1  # Step size
y, e, w = adf.nlms(u, d, M, step, returnCoeffs=True)

# Calculate mean square weight error
# mswe = adf.mswe(w, coeffs)

# Plot speech signals
plt.figure()
plt.title("Speech signals")
plt.plot(u, label="Emily's speech signal, u(n)")
plt.plot(d, label="Speech signal from John, d(n)")
plt.grid()
plt.legend()
plt.xlabel('Samples')

# Plot error signal - note how the measurement noise affects the error
plt.figure()
plt.title('Error signal e(n)')
plt.plot(e)
plt.grid()
plt.xlabel('Samples')

# Plot mean squared weight error - note that the measurement noise causes the
# error the increase at some points when Emily isn't speaking
# plt.figure()
# plt.title('Mean squared weight error')
# plt.plot(mswe)
# plt.grid()
# plt.xlabel('Samples')

# Plot final coefficients versus real coefficients
# plt.figure()
# plt.title('Real coefficients vs. estimated coefficients')
# plt.plot(w[-1], 'g', label='Estimated coefficients')
# plt.plot(coeffs, 'b--', label='Real coefficients')
# plt.grid()
plt.legend()
# plt.xlabel('Samples')

plt.show()


