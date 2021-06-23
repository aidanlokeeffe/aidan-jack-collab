import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math


#THIS CAN ANIMATE ATTEMPTED AND ACTUAL. I WANT TO FIX IT SO THAT IT CAN IDENTIFY AND SET THE AXIS BOUNDS ITSELF BASED OFF OF WHAT DATA IT IS GIVEN
#IT KNOWS IF ITS ATTEMPTED OR ACTUAL AND TITLES IT BASED OFF OF THE INPUT CSV SAYING attempted OR actual FIRST. THE SECOND LETTER MUST BE c OR t


def animateBarchart(inFile):
    matrix = np.genfromtxt(inFile, delimiter=',')
    if math.isnan(matrix[0][0]):
        matrix = matrix[1:,1:]
    print(matrix)
    N= len(matrix[0])
    fig=plt.figure()
    if inFile[1]=='c':
        plt.title('Actual Activity')
        plt.ylim(0, 3)
        plt.xlabel('Node')
        plt.ylabel('Activity')
    elif inFile[1]=='t':
        plt.title('Attempted Activity')
        plt.ylim(0, 15)
        plt.xlabel('Node')
        plt.ylabel('Activity')
    else:
        plt.title('Message Ages')
        plt.xlabel('Age')
        plt.ylabel('No. of Messages')
        
    

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

    anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=n,
                             interval=200)

    #anim.save('mymovie.mp4',writer=animation.FFMpegWriter(fps=10))
    plt.show()

animateBarchart('attempted_test.csv')
animateBarchart('actual_test.csv')
animateBarchart('ages_test.csv')