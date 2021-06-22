import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math


#THIS CAN ANIMATE ATTEMPTED AND ACTUAL. I WANT TO FIX IT SO THAT IT CAN IDENTIFY AND SET THE AXIS BOUNDS ITSELF BASED OFF OF WHAT DATA IT IS GIVEN


def animateBarchart(inFile):
    matrix = np.genfromtxt(inFile, delimiter=',')
    if math.isnan(matrix[0][0]):
        matrix = matrix[1:,1:]
    N= len(matrix[0])
    fig=plt.figure()

    def barlist(n): 
        if n >= N:
            return matrix[N]
        else:
            return matrix[n]

    def animate(i):
        y=barlist(i+1)
        for i, b in enumerate(barcollection):
            b.set_height(y[i])

    n=len(matrix) #Number of frames
    x=range(N) #number of bars
    barcollection = plt.bar(x,barlist(1))


    plt.ylim(0, 10)

    anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=n,
                             interval=200)

    #anim.save('mymovie.mp4',writer=animation.FFMpegWriter(fps=10))
    plt.show()

animateBarchart('attempted_test.csv')
animateBarchart('actual_test.csv')



    





