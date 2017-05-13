import sys , os
sys.path.append(os.pardir)
from mylib.dataset.mnist import load_mnist

import numpy as np
from mylib.Sec3 import *
from mylib.Sec4 import *

if __name__ == '__main__':
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)
#-------------------------------------------------------------------------------------------
    train_loss_list = {}
    train_size = x_train.shape[0]
    # hyper parameter
    iters_num = 10000
    batch_size = 100
    learning_rate = 0.1
    # networkをclassから読み込み
    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

    for i in range(iters_num):
        #ミニバッチの取得
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]
        # 勾配の計算
        grad = network.numerical_gradient(x_batch, t_batch)
        # パラメータの更新
        for key in ("W1", "b1", "W2", "b2"):
            network.params[key] -= learning_rate * grad[key]
        # 学習経過の記録
        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)
#-------------------------------------------------------------------------------------------
    # net = simpleNet()
    # print("weight : \n {}".format(net.W) )
    # x = np.array([0.6, 0.9])
    # p = net.predict(x)
    # print("predict : \n{}".format(p) )
#-------------------------------------------------------------------------------------------
    # init_x = np.array([-3.0, 4.0])
    # print(gradient_descent(equation_function, init_x=init_x, lr=0.1, step_num=100))
