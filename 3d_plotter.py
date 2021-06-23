from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math


def plotKillingEdge(inFile):
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')

    matrix = np.genfromtxt(inFile, delimiter=',')
    if math.isnan(matrix[0][0]):
        matrix = matrix[1:,1:]
    N=len(matrix)
    xpos = []
    ypos = []
    num_elements = len(xpos)

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

plotKillingEdge('cumulative_death_edges_test.csv')