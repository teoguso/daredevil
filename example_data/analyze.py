import scipy
import sys

def main():
    f = scipy.fromfile(open(sys.argv[1]), dtype=scipy.complex64)


if __name__ == "__main__":
    main()
