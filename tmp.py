import matplotlib
# matplotlib.use('Agg') # no UI backend

import numpy as np
import matplotlib.pyplot as plt
plt.ioff()
for i in range(3):
    plt.plot(np.random.rand(10))
#plt.show()

import os
directory = './data'
if not os.path.exists(directory):
    os.makedirs(directory)

# plt.savefig('data/matplotlib.png')  #savefig, don't show
plt.show()
