import numpy as np
from mylib.p2_3 import *

#コメントアウトは ctrl+/
if __name__ == '__main__':
#Section2.3.3, 2.5.2-------------------------------------------------------------------------------
    #AND
    w = np.array([0.5, 0.5])
    b = -0.7
    x = np.array([0, 0])
    print("{}   AND    :{}".format(x,AND(x)))
    x = np.array([0, 1])
    print("{}   AND    :{}".format(x,AND(x)))
    x = np.array([1, 0])
    print("{}   AND    :{}".format(x,AND(x)))
    x = np.array([1, 1])
    print("{}   AND    :{}".format(x,AND(x)))

    #NAND
    x = np.array([0, 0])
    print("{}   NAND    :{}".format(x,NAND(x)))
    x = np.array([0, 1])
    print("{}   NAND    :{}".format(x,NAND(x)))
    x = np.array([1, 0])
    print("{}   NAND    :{}".format(x,NAND(x)))
    x = np.array([1, 1])
    print("{}   NAND    :{}".format(x,NAND(x)))

    #OR
    x = np.array([0, 0])
    print("{}   OR    :{}".format(x,OR(x)))
    x = np.array([0, 1])
    print("{}   OR    :{}".format(x,OR(x)))
    x = np.array([1, 0])
    print("{}   OR    :{}".format(x,OR(x)))
    x = np.array([1, 1])
    print("{}   OR    :{}".format(x,OR(x)))

    #XOR
    x = np.array([0, 0])
    print("{}   XOR    :{}".format(x,XOR(x)))
    x = np.array([0, 1])
    print("{}   XOR    :{}".format(x,XOR(x)))
    x = np.array([1, 0])
    print("{}   XOR    :{}".format(x,XOR(x)))
    x = np.array([1, 1])
    print("{}   XOR    :{}".format(x,XOR(x)))

#Section2.3.2-------------------------------------------------------------------------------
    # import numpy as np
    # x = np.array([0,1])     #入力
    # w = np.array([0.5,0.5]) #重み
    # b = -0.7                #バイアス
    # print(w*x)
    # print(np.sum(w*x))
    # print(np.sum(w*x)+b)
#Section2.3.1-------------------------------------------------------------------------------
    # from mylib.circuitLogic import *
    # print(AND(0,0))
    # print(AND(0,1))
    # print(AND(1,0))
    # print(AND(1,1))
#動作チェック-------------------------------------------------------------------------------
    # from mylib.test import *
    # print_test()
