#3.2.3 ステップ関数のグラフ
import numpy as np
import matplotlib.pylab as plt
from mylib.Sec3 import *

if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)
    y1 = step_function(x)
    plt.plot(x, y1)
    y2 = sigmoid(x)
    plt.plot(x, y2)
    y3 = relu(x)
    plt.plot(x, y3)
    plt.ylim(-0.1, 1.1)
    plt.show()
