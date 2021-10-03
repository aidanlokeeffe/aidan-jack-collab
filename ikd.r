setwd("C:/Users/aidan/OneDrive/Desktop/aidan-jack-collab")

coco_IS = read.csv("better_correlation_data/cocomac_for_corr_IS.csv")
coco_RW = read.csv("better_correlation_data/cocomac_for_corr_RW.csv")
monkey91_IS = read.csv("better_correlation_data/monkey91_for_corr_IS.csv")
monkey91_RW = read.csv("better_correlation_data/monkey91_for_corr_RW.csv")
threshmouse_IS = read.csv("better_correlation_data/threshmouse_for_corr_IS.csv")
threshmouse_RW = read.csv("better_correlation_data/threshmouse_for_corr_RW.csv")

hist(coco_IS$influence_mean_3, freq=FALSE, xlab="", ylab = "", main="", cex.axis = 1.5, ylim=c(0,70), breaks=20)
hist(monkey91_IS$influence_mean_3, freq=FALSE, xlab="", ylab = "", main="", cex.axis=1.5, breaks=23)
hist(threshmouse_IS$influence_mean_3, freq=FALSE, xlab="", ylab = "", main="", cex.axis=1.5, ylim=c(0,50), )
hist(coco_RW$influence_mean_3, freq=FALSE, xlab="", ylab = "", main="", cex.axis=1.5, xlim=c(0,0.02))
hist(monkey91_RW$influence_mean_3, freq=FALSE, xlab="", ylab = "", main="", cex.axis=1.5, xlim=c(0, 0.04))
hist(threshmouse_RW$influence_mean_3, freq=FALSE, xlab="", ylab = "", main="", cex.axis=1.5, ylim=c(0,100), xlim=c(0,0.02))

# REDUNDANCY MEANS
hist(coco_IS$redundancy_mean_3, freq=TRUE, xlab="", ylab = "", main="", cex.axis = 1.5, ylim=c(0,70))
hist(monkey91_IS$redundancy_mean_3, freq=TRUE, xlab="", ylab = "", main="", cex.axis=1.5, breaks=30)
hist(threshmouse_IS$redundancy_mean_3, freq=TRUE, xlab="", ylab = "", main="", cex.axis=1.5, ylim=c(0,50))
hist(coco_RW$redundancy_mean_3, freq=TRUE, xlab="", ylab = "", main="", cex.axis=1.5, ylim=c(0,100), xlim=c(0,0.02))
hist(monkey91_RW$redundancy_mean_3, freq=TRUE, xlab="", ylab = "", main="", cex.axis=1.5, ylim=c(0,50), xlim=c(0, 0.04))
hist(threshmouse_RW$redundancy_mean_3, freq=TRUE, xlab="", ylab = "", main="", cex.axis=1.5, ylim=c(0,100), xlim=c(0,0.02))

###
hist(coco_IS$influence_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=50, ylim=c(0,60), xlim=c(0, 0.2))
hist(monkey91_IS$influence_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=40, ylim=c(0,60), xlim=c(0, 0.3))
hist(threshmouse_IS$influence_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=40, ylim=c(0,60), xlim=c(0, 0.7))
hist(coco_RW$influence_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=40, ylim=c(0,35), xlim=c(0, 0.02))
hist(monkey91_RW$influence_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=40, ylim=c(0,35),xlim=c(0,0.034))
hist(threshmouse_RW$influence_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=40, ylim=c(0,35), xlim=c(0, 0.02))

###
hist(coco_IS$redundancy_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=50, xlim=c(0,1), ylim=c(0,90))
hist(monkey91_IS$redundancy_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=40, xlim=c(0, .25), ylim=c(0,90))
hist(threshmouse_IS$influence_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=40, xlim=c(0, 0.7), ylim=c(0,90))
hist(coco_RW$redundancy_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=20, ylim=c(0,200))
hist(monkey91_RW$redundancy_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=20, ylim=c(0,200), xlim=c(0,0.035))
hist(threshmouse_RW$redundancy_mean_3, xlab="", ylab="", main="", cex.axis=1.5, breaks=20, ylim=c(0,200), xlim=c(0,1.4))

################################################################################
################################################################################
h <- hist(coco_IS$influence_mean_3, plot=FALSE, breaks=50)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="red", cex.axis=1.5, xlim=c(0, 0.2))

h <- hist(monkey91_IS$influence_mean_3, plot=FALSE, breaks=40)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="green", cex.axis=1.5, xlim=c(0, 0.3))

h <- hist(threshmouse_IS$influence_mean_3, plot=FALSE, breaks=40)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="blue", cex.axis=1.5, xlim=c(0, 0.7))

h <- hist(coco_RW$influence_mean_3, plot=FALSE, breaks=40)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="red", cex.axis=1.5, xlim=c(0, 0.02))

h <- hist(monkey91_RW$influence_mean_3, plot=FALSE, breaks=10)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="green", cex.axis=1.5, xlim=c(0,0.034))

h <- hist(threshmouse_RW$influence_mean_3, plot=FALSE, breaks=30)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="blue", cex.axis=1.5, xlim=c(0, 0.02))

################################################################################
h <- hist(coco_IS$redundancy_mean_3, plot=FALSE, breaks=40)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="red", cex.axis=1.5, xlim=c(0,1))

h <- hist(monkey91_IS$redundancy_mean_3, plot=FALSE, breaks=40)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="green", cex.axis=1.5, xlim=c(0,0.25))

h <- hist(threshmouse_IS$redundancy_mean_3, plot=FALSE, breaks=40)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="blue", cex.axis=1.5, xlim=c(0,0.8))

h <- hist(coco_RW$redundancy_mean_3, plot=FALSE, breaks=20)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="red", cex.axis=1.5)

h <- hist(monkey91_RW$redundancy_mean_3, plot=FALSE, breaks=20)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="green", cex.axis=1.5, xlim=c(0, 0.035))

h <- hist(threshmouse_RW$redundancy_mean_3, plot=FALSE, breaks=20)
h$density = h$counts/sum(h$counts)
plot(h, freq=FALSE, xlab="", ylab="", main="", ylim=c(0,1), col="blue", cex.axis=1.5, xlim=c(0, 1.4))








