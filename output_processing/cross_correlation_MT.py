import numpy as np
import scipy
from scipy import fftpack
from scipy import signal
import matplotlib.pyplot as plt
import os.path
import math
import adaptfilt
import sys

from constants import DATA_PATH

'''
An attempted implementation of the code in documents/colone2009.pdf
'''
def calc_params(binSizeTim):
    # Sampling frequency
    fs = 200e3
    # Constants
    c  = 3e8 # Speed of light
    f0 = 88.8e6 # Centre freq
    maxrange  = 60e3
    maxvel  = 500 / 3.5

    maxdoppler  = ((c + maxvel) / c ) * f0  - f0
    maxdelay = maxrange / c

    maxshift = int(maxdelay * fs)
    maxtrans = int( maxdoppler / (fs  / binSizeTim))

    params = {  'fs'        : fs, 
                'maxshift'  : maxshift,
                'maxtrans'  : maxtrans,
                'c'         : c,
                'f0'        : f0,
                'maxrange'  : maxrange,
                'maxvel'    : maxvel,
                'maxdoppler': maxdoppler,
                'maxdelay'  : maxdelay    }

    return params

def adaptiveFiltering(ch0, ch1):
    binSizeTim = np.size(ch0,0)
    biNum = np.size(ch0,1)
    
    M = 5;
    step = binSizeTim / 5.0;
    
    N = binSizeTim - M + 1
    ch0out = np.zeros(( N, biNum ))
    ch1out = np.zeros(( N, biNum ))

    for bi in range(biNum):    
        ch0out[:,bi], ch1out[:,bi], _ = adaptfilt.nlms(ch1[:,bi], ch0[:,bi], M, step)
        
    
    return ch0out, ch1out
    
def crosscorrelation(ch0, ch1, params ):
    maxshift = params['maxshift']
    maxtrans = params['maxtrans']
    binSizeTim = np.size(ch0,0)
    biNum = np.size(ch0,1)
    
    plt.ion()

    tempOut = np.zeros((2 * maxtrans + 1, 2 * maxshift + 1), dtype=np.complex64)
    
    out = np.zeros((biNum, maxtrans + 1, 2 * maxshift + 1), dtype=np.complex64)
    
    for bi in range(biNum):
        ch0fft = scipy.fftpack.fft(np.transpose(ch0[:,bi]))
        ch1fft = scipy.fftpack.fft(np.transpose(ch1[:,bi])) 
        
        for i in range(-maxtrans, maxtrans+1):
            # coor = np.zeros( (len(ch1fft)), dtype=np.complex64)
            
            coor = np.multiply(ch1fft, np.conjugate(np.roll(ch0fft,i)))
            coor = scipy.fftpack.ifft(coor)
            
            tempOut[i,:] = np.concatenate([coor[-maxshift:], coor[0:maxshift+1]])

        out[bi,:,:] = np.add(np.flipud(tempOut[maxtrans:,:][0]),(tempOut[0:maxtrans+1,:])) / 2
        
        plt.clf()
        plt.title("Bin number "+str(bi+1))

        #Relative Ballistic Range [km]
        xmin = 0
        xmax = params['maxrange'] / 1000
        #Relative Ballistic Velocity [m/s] 
        ymin = -params['maxvel']
        ymax = params['maxvel']
      
        plt.imshow( np.transpose(np.log(np.absolute(out[bi,:,:]))),
                    extent=[xmin, xmax, ymin, ymax],
                    aspect = xmax/ymax,
                    interpolation='none')
                    
        plt.pause(0.01)
    plt.ioff()
    plt.show()

def loadData(path_data1, path_data2, binSizeTim):    
    ch0 = scipy.fromfile(path_data1, dtype=scipy.complex64)
    ch1 = scipy.fromfile(path_data2, dtype=scipy.complex64)
    
    N = min(len(ch0),len(ch1))
    rem = N % binSizeTim
    bNum = int(math.floor( N / binSizeTim))
    
    ch0rshp = np.reshape(ch0[0:N-rem],[binSizeTim,bNum])
    ch1rshp = np.reshape(ch1[0:N-rem],[binSizeTim,bNum])
	
    return ch0rshp, ch1rshp
    
def main():
    path0 = os.path.join(DATA_PATH, "ch0.cfile")
    path1 = os.path.join(DATA_PATH, "ch1.cfile")
    binSizeTim = 50000
    
    ch0, ch1 = loadData(path0, path1, binSizeTim)
      
    #ch0, ch1 = adaptiveFiltering(ch0, ch1)   

    params = calc_params(binSizeTim)    
    crosscorrelation(ch0, ch1, params)

if __name__ == "__main__":
    main()
