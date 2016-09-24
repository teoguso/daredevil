from __future__ import print_function
import numpy as np
import adaptfilt
from scipy import fromfile
import matplotlib.pyplot as plt

path = "../example_data/ch0.cfile"
ch0 = fromfile(path)

print(ch0.shape)
plt.plot(ch0)
plt.show()
