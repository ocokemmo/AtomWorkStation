import matplotlib.pyplot as plt
import numpy as np

class fazzy:
    def __init__(self, dt, x, range_h):
        self.membershipFunc = np.zeros_like(x)
        self.hLevelSet = np.zeros( (len(range_h), int(10/dt + 1)) )
        self.edgeL = np.zeros( len(range_h) )
        self.edgeR = np.zeros( len(range_h) )

    # のこぎり型のmembership関数生成
    def sawFunc(self, dt, x, top, left, right):
        self.membershipFunc = np.zeros_like(x)
        self.membershipFunc[left/dt : top/dt] = (x[left/dt : top/dt] - left)/(top - left)
        self.membershipFunc[top/dt : right/dt] = (x[top/dt : right/dt] - right)/(top - right)

    # 台形型のmembership関数生成
    def trapezoidFunc(self, dt, x, left_bottom, left_top, right_top, right_bottom):
        self.membershipFunc = np.zeros_like(x)
        self.membershipFunc[left_bottom/dt : left_top/dt] = (x[left_bottom/dt : left_top/dt] - left_bottom)/(left_top - left_bottom)
        self.membershipFunc[left_top/dt : right_top/dt] = 1
        self.membershipFunc[right_top/dt : right_bottom/dt] = (x[right_top/dt : right_bottom/dt] - right_bottom)/(right_top - right_bottom)

    def hLevelFunc():
        for h in range(len(range_h)):
            # 0から順にループ
            for i in range(0, int(10/dt)-1, 1):
                # range_h[h]以上のところを1にする
                if self.membershipFunc[i] >= range_h[h]:
                    self.hLevelSet[h, i] = i

    # 各hに対してh-レベル集合のedgeを求める
    def edgeFunc(self, range_h, dt):
        for h in range(len(range_h)):
            # 0から順にループ
            for i in range(0, int(10/dt)-1, 1):
                # 最初にh-レベルに当たった場所がedgeL
                if self.membershipFunc[i] >= range_h[h]:
                    self.edgeL[h] = i
                    break
            # 逆から順にループ
            for i in range(int(10/dt)-1, 0, -1):
                # 最初にh-レベルに当たった場所がedgeR
                if self.membershipFunc[i] >= range_h[h]:
                    self.edgeR[h] = i
                    break

def plusFazzySet(A, B, C):
    C.edgeL = A.edgeL + B.edgeL
    C.edgeR = A.edgeR + B.edgeR

def minusFazzySet(A, B, C):
    C.edgeL = A.edgeL - B.edgeL
    C.edgeR = A.edgeR - B.edgeR

def plot_hLevelSet(A, B, C, dt, range_h, x_max, x_min):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.scatter([A.edgeL*dt, A.edgeR*dt], [range_h, range_h], c="r")
    ax.scatter([B.edgeL*dt, B.edgeR*dt], [range_h, range_h], c="b")
    ax.scatter([C.edgeL*dt, C.edgeR*dt], [range_h, range_h], c="g")
    ax.set_xticks(range(x_min,x_max))
    ax.set_yticks(np.arange(-0.1,1.1,0.1))

    plt.show()

def plot_hLevelFunc(A, B, C, dt, range_h, x_max, x_min):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.plot([x_min, A.edgeL[0]*dt], [0, range_h[0]], c="r")
    ax.plot(A.edgeL*dt, range_h, c="r")
    ax.plot([A.edgeL[-1]*dt, A.edgeR[-1]*dt], [range_h[-1], range_h[-1]], c="r")
    ax.plot(A.edgeR*dt, range_h, c="r")
    ax.plot([A.edgeR[0]*dt, x_max], [range_h[0], 0], c="r")

    ax.plot([x_min, B.edgeL[0]*dt], [0, range_h[0]], c="b")
    ax.plot(B.edgeL*dt, range_h, c="b")
    ax.plot([B.edgeL[-1]*dt, B.edgeR[-1]*dt], [range_h[-1], range_h[-1]], c="b")
    ax.plot(B.edgeR*dt, range_h, c="b")
    ax.plot([B.edgeR[0]*dt, x_max], [range_h[0], 0], c="b")

    ax.plot([x_min, C.edgeL[0]*dt], [0, range_h[0]], c="g")
    ax.plot(C.edgeL*dt, range_h, c="g")
    ax.plot([C.edgeL[-1]*dt, C.edgeR[-1]*dt], [range_h[-1], range_h[-1]], c="g")
    ax.plot(C.edgeR*dt, range_h, c="g")
    ax.plot([C.edgeR[0]*dt, x_max], [range_h[0], 0], c="g")
    ax.set_xticks(range(x_min,x_max))
    ax.set_yticks(np.arange(-0.1,1.1,0.1))

    plt.show()
