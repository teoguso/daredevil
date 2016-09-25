import scipy
import matplotlib.pyplot as plt
import os.path

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "new_example")

def main():
    '''
    Make a basic plot of the data output from gnuradio
    '''
    dataLen = 1000;
    ch0 = scipy.fromfile(open(os.path.join(DATA_PATH, "ch0.cfile")),
                         dtype=scipy.complex64, count=dataLen)

    ch1 = scipy.fromfile(open(os.path.join(DATA_PATH,"ch1.cfile")),
                         dtype = scipy.complex64, count = dataLen)

    fig1 = plt.figure()
    plt.plot(ch0)
    plt.show()

if __name__ == "__main__":
    main()



