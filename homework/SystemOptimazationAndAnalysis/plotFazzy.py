import matplotlib.pyplot as plt
import numpy as np

def plotFazzy(x,y1,y2,title):
    # plt.scatter(x,y1,c="b",label="A")
    # plt.scatter(x,y2,c="r",label="B")
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.title(title)
    plt.xlim(0.0, 10.0)
    plt.ylim(-0.1, 1.1)
    plt.show()

def plotLevel(X, range_h, dt):
    x_L = np.zeros_like(range_h)
    x_R = np.zeros_like(range_h)
    for h in range(len(range_h)):
        for i in range(len(X[h,:])-1):
            if X[h,i] == 0 and X[h,i+1] == 1:
                plt.scatter((i+1)*dt,range_h[h])
                x_L[h]=i+1
            if X[h,i] == 1 and X[h,i+1] == 0:
                plt.scatter(i*dt,range_h[h])
                x_R[h]=i
    return [np.array(x_L), np.array(x_R)]

def plusFazzySet(a_L, a_R, b_L, b_R):
    return [a_L + b_L, a_R + b_R]

def plotFazzySet(c_L, c_R, range_h, dt):
    plt.scatter(c_L*dt, range_h)
    plt.scatter(c_R*dt, range_h)
    plt.show()

def plotAllFazzySet(a_L, a_R, b_L, b_R, c_L, c_R, dt, range_h):
    plt.scatter([a_L*dt, a_R*dt], [range_h, range_h], c="r", label="Fazzy Set A")
    plt.scatter([b_L*dt, b_R*dt], [range_h, range_h], c="b", label="Fazzy Set B")
    plt.scatter([c_L*dt, c_R*dt], [range_h, range_h], c="g", label="Fazzy Set C=A+B")
    plt.title("Graphs of h-level set $[A]_h$(blue), $[B]_h$(red) and $[C]_h$(green).")
    plt.show()
