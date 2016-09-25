import numpy as np
import scipy
import matplotlib.pyplot as plt
import os.path
import math

from constants import DATA_PATH

'''
An attempted implementation of the code in documents/colone2009.pdf
'''

def plot_crosscorrelation(path_data1, path_data2, sample_size):
    # Read in data
    ch0 = scipy.fromfile(path_data1, dtype=scipy.complex64, count=sample_size)
    ch1 = scipy.fromfile(path_data2, dtype=scipy.complex64, count=sample_size)

    bucketSize = 100

    # Number of samples
    N = len(ch0)
    bNum = int(math.floor( N / bucketSize))

    # Sampling frequency
    f_s = 1.0E6

    # Sampling period
    T_s = 1/f_s

    # Doppler frequency range
    n_f_dop = 120
    f_dop = np.arange(0, n_f_dop, step=1)

    # time delay range
    R = 100

    plt.ion()
    # plt.colorbar()

    # corr = np.zeros((bucketSize, len(f_dop), bNum), dtype=np.complex64)
    corr_tmp = np.zeros((R,len(f_dop)), dtype=np.complex64)
    print(corr_tmp.shape)

    for bi in range(bNum):
        iStart = bi * bucketSize
        #iEnd = iStart + bucketSize - 1
        #i0 = 0	
        den_1 = 1/R
        for i in range(R):
            for j in range(len(f_dop)):
                # This equation is wrong, there must be a shift between ch0 and ch1
                # corr[i0,j, bi] = ch0[i]  * ch1[i] * np.exp(-1j *2*np.pi*f_dop[j]/(len(ch1)))
                corr_tmp[i, j] = ch0[i+iStart]  * ch1[i+iStart-j] * np.exp(-1j *2*np.pi*f_dop[j]*den_1)
            #i0 += 1

        plt.clf()
        # plt.plot(np.sin(np.arange(100)/float(bi+1)))
        plt.title("Bin number "+str(bi))
        plt.imshow(corr_tmp.imag)
        # plt.pcolormesh(corr_tmp.real)
        plt.pause(0.01)
    plt.ioff()
    plt.show()


    # Display
        
    #ax = plt.subplot(111)
    #quad = plt.pcolormesh(Log(corr[:,:,0].real))
    #plt.colorbar()

    # plt.plot(np.sin(np.arange(100)))
    # plt.ion()

    # plt.show()
    # for i in range(20):
    #     plt.plot(np.sin(np.arange(100)/float(i+1)))
        # time.sleep(0.1)
        # plt.pause(0.05)
        # plt.clf()


def main():
    sample_size = 15000
    path1 = os.path.join(DATA_PATH, "ch0.cfile")
    path2 = os.path.join(DATA_PATH, "ch1.cfile")
    plot_crosscorrelation(path1, path2, sample_size)

if __name__ == "__main__":
    main()
