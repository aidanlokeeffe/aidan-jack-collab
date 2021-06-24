#start by just running 100 steps and low load and see how much slower it gets 
#run at load 1, .01, .05, .1, .2 for 500-1000+ steps, find avg age
#if a message is represented by where it has been, 5 100 21 is age of 3
#EVERYBODY GETS ONTO NETWORK WITH AGE 1. EVERY HOP, ADD ONE YEAR. DEATH IS A HOP, IT IS A YEAR
#let it run for like 200 to get out of the initial transient, into a steady state. THEN start keeping track of tings 
#1000 steps throwing out 500, but that's 'overkill'
#run it for 1000 steps and keep track of any numerical statistic I want to track and see that things fluctuate 
#LOOKING AT THE AFOREMENTIONED STAT: the beginning weird bit is the transient. get rid of the transient
#cut off the first 5 to 20% 
#gold standard is 500 to 1000 steps
#THEORETICAL / PURE / ALGORITHM THEORY IDEA: RANDOMIZING A NETWORK (KEEP ROW AND COLUMN SUMS THE SAME?)
#ASYMMETRICAL EDGE WEIGHTS MEANING if two nodes are doubly linked (A to B AND B to A), is one path/direction more used than the other? why?
#   alt, if they are bidirectional or an undirected link, which way does it usually go and why?
#   what if we consider weighting the edges based off of activity, or is there already correlation between weight and traffic

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('meetingpic.jpg')
imgplot = plt.imshow(img)
plt.show()