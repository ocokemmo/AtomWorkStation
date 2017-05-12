import numpy as np

def AND(x):
    w = np.array([0.5, 0.5])
    b = -0.7
    temp = np.dot(x, w) + b
    if temp <= 0:
        return 0
    else:
        return 1

def NAND(x):
    w = np.array([-0.5, -0.5])
    b = 0.7
    temp = np.dot(x, w) + b
    if temp <= 0:
        return 0
    else:
        return 1

def OR(x):
    w = np.array([0.5, 0.5])
    b = -0.2
    temp = np.dot(x, w) + b
    if temp <= 0:
        return 0
    else:
        return 1

def XOR(x):
    s1 = NAND(x)
    s2 = OR(x)
    return(AND(np.array([s1, s2])))
