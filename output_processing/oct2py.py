import numpy as np
import scipy
from scipy import fftpack
import matplotlib.pyplot as plt
import os.path
import math

from constants import DATA_PATH

'''
An attempted implementation of the code in documents/colone2009.pdf
'''

def plot_crosscorrelation(path_data1, path_data2, sample_size=None):
    # Read in data
    sample_size = 50000
    ch0 = scipy.fromfile(path_data1, dtype=scipy.complex64, count=sample_size)
    ch1 = scipy.fromfile(path_data2, dtype=scipy.complex64, count=sample_size)

    c = float(3E8)
    f0 = float(88.8E6)
    maxrange = float(100E3)
    maxvel = 500/3.6
    maxdoppler = (c+maxvel)/c*f0 - f0

    maxdelay = maxrange/c

    fs = float(200E3)
    min_len = min(len(ch0), len(ch1))

    maxshift = int(round(maxdelay * fs))
    maxtrans = int(round(min_len*maxdoppler/fs))
    print(maxtrans, maxdoppler, len(ch0), len(ch1))

    ch0_fft = fftpack.fft(ch0)
    ch1_fft = fftpack.fft(ch1)

    out = np.zeros((2*maxtrans+ 1, 2*maxshift), dtype=np.complex64)
    # plt.ion()

    for i in range(-maxtrans,maxtrans):
        # ch1s = np.copy(ch1)
        corr_fft = ch0_fft*np.roll(ch1, i)
        corr = fftpack.ifft(corr_fft)

        out[i+maxtrans+1] = np.concatenate((corr[-maxshift:], corr[:maxshift]))

    print(out.shape)
    out = np.absolute(out)
    # plt.clf()
    # plt.plot(np.sin(np.arange(100)/float(bi+1)))
    # plt.title("Bin number "+str(bi))
    plt.imshow(out)
    # plt.pcolormesh(corr_tmp.real)
    # plt.pause(0.01)
    # plt.ioff()
    plt.show()

def main():
    sample_size = 150000
    path1 = os.path.join(DATA_PATH, "ch0.cfile")
    path2 = os.path.join(DATA_PATH, "ch1.cfile")
    plot_crosscorrelation(path1, path2) #, sample_size)

if __name__ == "__main__":
    main()
