import matplotlib.pyplot as plt
import numpy as np
from myFunc import *
import seaborn as sns
import math

if __name__ == '__main__':
    # dt : プロットの粗さ
    dt = 0.01
    # x : x軸の集合
    x = np.arange(0,10,dt)
    # h : h-レベル集合の粗さ
    range_h = np.r_[0.0001, np.arange(0.1, 1.00000001, 0.1)]
    # fazzy集合のdef
    A = fazzy(dt, x, range_h)
    B = fazzy(dt, x, range_h)
    C = fazzy(dt, x, range_h)

    # self.sawFunc(self, dt,x,top,left,right)
#    A.sawFunc(dt, x, 5.0, 2.0, 8.0)
#    B.sawFunc(dt, x, 3.0, 1.0, 5.0)

    A.trapezoidFunc(dt, x, 1.3, 3.0, 4.0, 9.2)
    B.trapezoidFunc(dt, x, 1.0, 2.0, 7.0, 8.5)

    # self.hLevelFunc(self, range_h, dt)
    A.edgeFunc(range_h, dt)
    B.edgeFunc(range_h, dt)

    # fuzzy集合の和
    plusFazzySet(A, B, C)

    # x軸の幅の決定
    x_min = math.floor(np.min(np.array([A.edgeL[0]*dt,B.edgeL[0]*dt,C.edgeL[0]*dt]))) - 1
    x_max = math.ceil(np.max(np.array([A.edgeR[0]*dt,B.edgeR[0]*dt,C.edgeR[0]*dt]))) + 1

    # h-レベル集合のプロット
    plot_hLevelSet(A, B, C, dt, range_h, x_max, x_min)

    # h-レベル集合の概形
    plot_hLevelFunc(A, B, C, dt, range_h, x_max, x_min)
