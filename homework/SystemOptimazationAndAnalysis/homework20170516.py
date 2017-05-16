import matplotlib.pyplot as plt
import numpy as np
from plotFazzy import *
from myFunc import *
import seaborn as sns

if __name__ == '__main__':
        #mu_Aとmu_Bのグラフの記述
        dt = 0.01
        x = np.arange(0,10,dt)
        # 課題のグラフを生成する点列
        # mu_A = np.zeros_like(x)
        # mu_A[2/dt:8/dt] = 1 - np.abs(x[2/dt:8/dt]-5)/3
        # mu_B = np.zeros_like(x)
        # mu_B[1/dt:5/dt] = 1 - np.abs(x[1/dt:5/dt]-3)/2

        # 二次関数
        # mu_A = np.zeros_like(x)
        # mu_A[2/dt:8/dt] = -(x[2/dt:8/dt]-2)*(x[2/dt:8/dt]-8)/9
        # mu_B = np.zeros_like(x)
        # mu_B[1/dt:5/dt] = -(x[1/dt:5/dt]-1)*(x[1/dt:5/dt]-5)/4

        # 台形 + 二次関数
        mu_A = np.zeros_like(x)
        mu_A[2/dt:4/dt] = 1/2*(x[2/dt:4/dt]-2)
        mu_A[4/dt:6/dt] = 1
        mu_A[6/dt:7/dt] = -1*(x[6/dt:7/dt]-7)
        mu_B = np.zeros_like(x)
        mu_B[1/dt:5/dt] = -(x[1/dt:5/dt]-1)*(x[1/dt:5/dt]-5)/4

        # title = "graph"
        # plotFazzy(x,mu_A,mu_B,title)
        #fの概形をh-レベル集合から求める

        # hの定義
        range_h = np.r_[0.0001, np.arange(0.01, 1.00000001, 0.01)]

        # レベル集合の定義
        A_h = np.zeros( (len(range_h), int(10/dt + 1)) )
        B_h = np.zeros( (len(range_h), int(10/dt + 1)) )

        # 各hに対してレベル集合を求める
        for h in range(len(range_h)):
            # Aのh-レベル集合
            for i in range(0, int(10/dt)):
                if mu_A[i] >= range_h[h]:
                    # muがh以上の部分に対しては1を割り当て
                    A_h[h, i] = 1
            # Bのh-レベル集合
            for i in range(0, int(10/dt)):
                if mu_B[i] >= range_h[h]:
                    # muがh以上の部分に対しては1を割り当て
                    B_h[h, i] = 1

        # レベル集合のedgeを求める
        [a_L, a_R] = plotLevel(A_h, range_h, dt)
        [b_L, b_R] = plotLevel(B_h, range_h, dt)
        # print(a_L)
        # print(a_R)
        # print(b_L)
        # print(b_R)

        #[f(A,B)]h=f([A]h, [B]h)より,
        #[f(A,B)]h=[A+B]h=[C]h を f([A]h, [B]h)=[A]h+[B]hで求める
        #ファジィ集合の和は端の和
        [c_L, c_R] = plusFazzySet(a_L, a_R, b_L, b_R)
        # plotFazzySet(a_L, a_R, range_h, dt)
        # plotFazzySet(b_L, b_R, range_h, dt)
        # plotFazzySet(c_L, c_R, range_h, dt)
        plotAllFazzySet(a_L, a_R, b_L, b_R, c_L, c_R, dt, range_h)
