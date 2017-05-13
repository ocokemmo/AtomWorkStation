import sys , os
sys.path.append(os.pardir)
from mylib.dataset.mnist import load_mnist

import numpy as np
from mylib.Sec3 import *

if __name__ == '__main__':
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize = False)
    # img = x_train[0]
    # label = t_train[0]
    # print(label)
    # print(img.shape)
    # img = img.reshape(28,28) # 784 = 28*28
    # print(img.shape)
    # img_show(img)

    x, t = get_data()
    network = init_network()

    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y)
        if p == t[i]:
            accuracy_cnt += 1
    print("Accuracy:{}".format( float(accuracy_cnt)/len(x) ))
