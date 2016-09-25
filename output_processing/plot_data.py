import scipy
import matplotlib.pyplot as plt
import os.path

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "new_example")

def generate_plot(filepath):
    '''
    Make a basic plot of the binary output data (from gnuradio)
    '''
    dataLen = 1000
    data = scipy.fromfile(open(filepath), dtype=scipy.complex64, count=dataLen)
    plt.figure()
    plt.plot(data)
    plt.show()


def main():
    path = os.path.join(DATA_PATH, "ch0.cfile")
    generate_plot(path)


if __name__ == "__main__":
    main()



