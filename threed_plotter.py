import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math


def plotKillingEdge(inFile):
    fig = plt.figure()
    #plt.title('Messages Killed by Edge')
    #plt.xlabel('Sending Node')
    #plt.ylabel('Recieving Node')
    #plt.zlabel('No. of Killed Messages')
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.set_xlabel('Sending Node')
    ax1.set_ylabel('Recieving Node')
    ax1.set_zlabel('No. of Killed Messages')
    ax1.set_title('No. of Messages Killed by Edge')


    matrix = np.genfromtxt(inFile, delimiter=',')
    if math.isnan(matrix[0][0]):
        matrix = matrix[1:,1:]
    N=len(matrix)
    xpos = []
    ypos = []

    dz = []
    for i in range(N):
        for j in range(N):
            if math.isnan(matrix[i][j]):
                pass
            else:
                dz.append(matrix[i][j])
                xpos.append(i)
                ypos.append(j)
    totally = len(dz)
    zpos = [0]*(totally)

    dx = np.ones(totally)
    dy = np.ones(totally)

    ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
    plt.show()

#plotKillingEdge('cumulative_death_edges_test.csv')