import numpy as np
from mylib.Sec3 import *

if __name__ == '__main__':
    network = init_network()
    x = np.array([1.0, 0.5])
    y = forward_step(network, x)
    print("{}".format(y))
    y = forward_sigmoid(network, x)
    print("{}".format(y))
    y = forward_relu(network, x)
    print("{}".format(y))
    print("finish.")
