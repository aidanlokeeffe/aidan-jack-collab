setwd("C:/Users/aidan/OneDrive/Desktop/aidan-jack-collab")

# Load in all the data
coco_IS_0 = read.csv("cocomac_IS_stact/cocomac_IS_stact_stats_0.csv")
coco_IS_1 = read.csv("cocomac_IS_stact/cocomac_IS_stact_stats_1.csv")
coco_IS_2 = read.csv("cocomac_IS_stact/cocomac_IS_stact_stats_2.csv")
coco_IS_3 = read.csv("cocomac_IS_stact/cocomac_IS_stact_stats_3.csv")
coco_IS_4 = read.csv("cocomac_IS_stact/cocomac_IS_stact_stats_4.csv")
coco_RW_0 = read.csv("cocomac_RW_stact/cocomac_RW_stact_stats_0.csv")
coco_RW_1 = read.csv("cocomac_RW_stact/cocomac_RW_stact_stats_1.csv")
coco_RW_2 = read.csv("cocomac_RW_stact/cocomac_RW_stact_stats_2.csv")
coco_RW_3 = read.csv("cocomac_RW_stact/cocomac_RW_stact_stats_3.csv")
coco_RW_4 = read.csv("cocomac_RW_stact/cocomac_RW_stact_stats_4.csv")
monkey_IS_0 = read.csv("monkey91_IS_stact/monkey91_IS_stact_stats_0.csv")
monkey_IS_1 = read.csv("monkey91_IS_stact/monkey91_IS_stact_stats_1.csv")
monkey_IS_2 = read.csv("monkey91_IS_stact/monkey91_IS_stact_stats_2.csv")
monkey_IS_3 = read.csv("monkey91_IS_stact/monkey91_IS_stact_stats_3.csv")
monkey_IS_4 = read.csv("monkey91_IS_stact/monkey91_IS_stact_stats_4.csv")
monkey_RW_0 = read.csv("monkey91_RW_stact/monkey91_RW_stact_stats_0.csv")
monkey_RW_1 = read.csv("monkey91_RW_stact/monkey91_RW_stact_stats_1.csv")
monkey_RW_2 = read.csv("monkey91_RW_stact/monkey91_RW_stact_stats_2.csv")
monkey_RW_3 = read.csv("monkey91_RW_stact/monkey91_RW_stact_stats_3.csv")
monkey_RW_4 = read.csv("monkey91_RW_stact/monkey91_RW_stact_stats_4.csv")
mouse_IS_0 = read.csv("mouse_IS_stact/mouse_IS_stact_stats_0.csv")
mouse_IS_1 = read.csv("mouse_IS_stact/mouse_IS_stact_stats_1.csv")
mouse_IS_2 = read.csv("mouse_IS_stact/mouse_IS_stact_stats_2.csv")
mouse_IS_3 = read.csv("mouse_IS_stact/mouse_IS_stact_stats_3.csv")
mouse_IS_4 = read.csv("mouse_IS_stact/mouse_IS_stact_stats_4.csv")
mouse_RW_0 = read.csv("mouse_RW_stact/mouse_RW_stact_stats_0.csv")
mouse_RW_1 = read.csv("mouse_RW_stact/mouse_RW_stact_stats_1.csv")
mouse_RW_2 = read.csv("mouse_RW_stact/mouse_RW_stact_stats_2.csv")
mouse_RW_3 = read.csv("mouse_RW_stact/mouse_RW_stact_stats_3.csv")
mouse_RW_4 = read.csv("mouse_RW_stact/mouse_RW_stact_stats_4.csv")


##################
# COCOMAC, IS
##################
a1<-cor(coco_IS_0)
a2<-cor(coco_IS_1)
a3<-cor(coco_IS_2)
a4<-cor(coco_IS_3)
a5<-cor(coco_IS_4)

inf.v.in <- c(a1[2,6], a2[2,6], a3[2,6], a4[2,6], a5[2,6])
inf.v.out <- c(a1[3,6], a2[3,6], a3[3,6], a4[3,6], a5[3,6])
inf.v.clc <- c(a1[4,6], a2[4,6], a3[4,6], a4[4,6], a5[4,6])
inf.v.btc <- c(a1[5,6], a2[5,6], a3[5,6], a4[5,6], a5[5,6])

plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     In Degree vs. Load (Cocomac, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Out Degree vs. Load (Cocomac, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Closeness Centrality vs. Load (Cocomac, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Betweenness Centrality vs. Load (Cocomac, IS)", ylim=c(-1, 1))

 red.v.in <- c(a1[2,7], a2[2,7], a3[2,7], a4[2,7], a5[2,7])
red.v.out <- c(a1[3,7], a2[3,7], a3[3,7], a4[3,7], a5[3,7])
red.v.clc <- c(a1[4,7], a2[4,7], a3[4,7], a4[4,7], a5[4,7])
red.v.btc <- c(a1[5,7], a2[5,7], a3[5,7], a4[5,7], a5[5,7])

plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     In Degree vs. Load (Cocomac, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Out Degree vs. Load (Cocomac, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Closeness Centrality vs. Load (Cocomac, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Betweenness Centrality vs. Load (Cocomac, IS)", ylim=c(-1, 1))

 ada.v.in <- c(a1[2,8], a2[2,8], a3[2,8], a4[2,8], a5[2,8])
ada.v.out <- c(a1[3,8], a2[3,8], a3[3,8], a4[3,8], a5[3,8])
ada.v.clc <- c(a1[4,8], a2[4,8], a3[4,8], a4[4,8], a5[4,8])
ada.v.btc <- c(a1[5,8], a2[5,8], a3[5,8], a4[5,8], a5[5,8])

plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     In Degree vs. Load (Cocomac, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Out Degree vs. Load (Cocomac, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Closeness Centrality vs. Load (Cocomac, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Betweenness Centrality vs. Load (Cocomac, IS)", ylim=c(-1, 1))


##################
# COCOMAC, RW
##################
a1<-cor(coco_RW_0)
a2<-cor(coco_RW_1)
a3<-cor(coco_RW_2)
a4<-cor(coco_RW_3)
a5<-cor(coco_RW_4)

inf.v.in <- c(a1[2,6], a2[2,6], a3[2,6], a4[2,6], a5[2,6])
inf.v.out <- c(a1[3,6], a2[3,6], a3[3,6], a4[3,6], a5[3,6])
inf.v.clc <- c(a1[4,6], a2[4,6], a3[4,6], a4[4,6], a5[4,6])
inf.v.btc <- c(a1[5,6], a2[5,6], a3[5,6], a4[5,6], a5[5,6])

plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     In Degree vs. Load (Cocomac, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Out Degree vs. Load (Cocomac, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Closeness Centrality vs. Load (Cocomac, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Betweenness Centrality vs. Load (Cocomac, RW)", ylim=c(-1, 1))

red.v.in <- c(a1[2,7], a2[2,7], a3[2,7], a4[2,7], a5[2,7])
red.v.out <- c(a1[3,7], a2[3,7], a3[3,7], a4[3,7], a5[3,7])
red.v.clc <- c(a1[4,7], a2[4,7], a3[4,7], a4[4,7], a5[4,7])
red.v.btc <- c(a1[5,7], a2[5,7], a3[5,7], a4[5,7], a5[5,7])

plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     In Degree vs. Load (Cocomac, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Out Degree vs. Load (Cocomac, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Closeness Centrality vs. Load (Cocomac, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Betweenness Centrality vs. Load (Cocomac, RW)", ylim=c(-1, 1))

ada.v.in <- c(a1[2,8], a2[2,8], a3[2,8], a4[2,8], a5[2,8])
ada.v.out <- c(a1[3,8], a2[3,8], a3[3,8], a4[3,8], a5[3,8])
ada.v.clc <- c(a1[4,8], a2[4,8], a3[4,8], a4[4,8], a5[4,8])
ada.v.btc <- c(a1[5,8], a2[5,8], a3[5,8], a4[5,8], a5[5,8])

plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     In Degree vs. Load (Cocomac, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Out Degree vs. Load (Cocomac, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Closeness Centrality vs. Load (Cocomac, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Betweenness Centrality vs. Load (Cocomac, RW)", ylim=c(-1, 1))


##################
# MONKEY91, IS
##################
a1<-cor(monkey_IS_0)
a2<-cor(monkey_IS_1)
a3<-cor(monkey_IS_2)
a4<-cor(monkey_IS_3)
a5<-cor(monkey_IS_4)

inf.v.in <- c(a1[2,6], a2[2,6], a3[2,6], a4[2,6], a5[2,6])
inf.v.out <- c(a1[3,6], a2[3,6], a3[3,6], a4[3,6], a5[3,6])
inf.v.clc <- c(a1[4,6], a2[4,6], a3[4,6], a4[4,6], a5[4,6])
inf.v.btc <- c(a1[5,6], a2[5,6], a3[5,6], a4[5,6], a5[5,6])

plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     In Degree vs. Load (Monkey91, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Out Degree vs. Load (Monkey91, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Closeness Centrality vs. Load (Monkey91, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Betweenness Centrality vs. Load (Monkey91, IS)", ylim=c(-1, 1))

red.v.in <- c(a1[2,7], a2[2,7], a3[2,7], a4[2,7], a5[2,7])
red.v.out <- c(a1[3,7], a2[3,7], a3[3,7], a4[3,7], a5[3,7])
red.v.clc <- c(a1[4,7], a2[4,7], a3[4,7], a4[4,7], a5[4,7])
red.v.btc <- c(a1[5,7], a2[5,7], a3[5,7], a4[5,7], a5[5,7])

plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     In Degree vs. Load (Monkey91, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Out Degree vs. Load (Monkey91, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Closeness Centrality vs. Load (Monkey91, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Betweenness Centrality vs. Load (Monkey91, IS)", ylim=c(-1, 1))

ada.v.in <- c(a1[2,8], a2[2,8], a3[2,8], a4[2,8], a5[2,8])
ada.v.out <- c(a1[3,8], a2[3,8], a3[3,8], a4[3,8], a5[3,8])
ada.v.clc <- c(a1[4,8], a2[4,8], a3[4,8], a4[4,8], a5[4,8])
ada.v.btc <- c(a1[5,8], a2[5,8], a3[5,8], a4[5,8], a5[5,8])


plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     In Degree vs. Load (Monkey91, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Out Degree vs. Load (Monkey91, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Closeness Centrality vs. Load (Monkey91, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Betweenness Centrality vs. Load (Monkey91, IS)", ylim=c(-1, 1))


##################
# MONKEY91, RW
##################
a1<-cor(monkey_RW_0)
a2<-cor(monkey_RW_1)
a3<-cor(monkey_RW_2)
a4<-cor(monkey_RW_3)
a5<-cor(monkey_RW_4)

inf.v.in <- c(a1[2,6], a2[2,6], a3[2,6], a4[2,6], a5[2,6])
inf.v.out <- c(a1[3,6], a2[3,6], a3[3,6], a4[3,6], a5[3,6])
inf.v.clc <- c(a1[4,6], a2[4,6], a3[4,6], a4[4,6], a5[4,6])
inf.v.btc <- c(a1[5,6], a2[5,6], a3[5,6], a4[5,6], a5[5,6])

plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     In Degree vs. Load (Monkey91, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Out Degree vs. Load (Monkey91, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Closeness Centrality vs. Load (Monkey91, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Betweenness Centrality vs. Load (Monkey91, RW)", ylim=c(-1, 1))

red.v.in <- c(a1[2,7], a2[2,7], a3[2,7], a4[2,7], a5[2,7])
red.v.out <- c(a1[3,7], a2[3,7], a3[3,7], a4[3,7], a5[3,7])
red.v.clc <- c(a1[4,7], a2[4,7], a3[4,7], a4[4,7], a5[4,7])
red.v.btc <- c(a1[5,7], a2[5,7], a3[5,7], a4[5,7], a5[5,7])

plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     In Degree vs. Load (Monkey91, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Out Degree vs. Load (Monkey91, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Closeness Centrality vs. Load (Monkey91, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Betweenness Centrality vs. Load (Monkey91, RW)", ylim=c(-1, 1))

ada.v.in <- c(a1[2,8], a2[2,8], a3[2,8], a4[2,8], a5[2,8])
ada.v.out <- c(a1[3,8], a2[3,8], a3[3,8], a4[3,8], a5[3,8])
ada.v.clc <- c(a1[4,8], a2[4,8], a3[4,8], a4[4,8], a5[4,8])
ada.v.btc <- c(a1[5,8], a2[5,8], a3[5,8], a4[5,8], a5[5,8])

plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     In Degree vs. Load (Monkey91, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Out Degree vs. Load (Monkey91, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Closeness Centrality vs. Load (Monkey91, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Betweenness Centrality vs. Load (Monkey91, RW)", ylim=c(-1, 1))


##################
# MOUSE, IS
##################
a1<-cor(mouse_IS_0)
a2<-cor(mouse_IS_1)
a3<-cor(mouse_IS_2)
a4<-cor(mouse_IS_3)
a5<-cor(mouse_IS_4)

inf.v.in <- c(a1[2,6], a2[2,6], a3[2,6], a4[2,6], a5[2,6])
inf.v.out <- c(a1[3,6], a2[3,6], a3[3,6], a4[3,6], a5[3,6])
inf.v.clc <- c(a1[4,6], a2[4,6], a3[4,6], a4[4,6], a5[4,6])
inf.v.btc <- c(a1[5,6], a2[5,6], a3[5,6], a4[5,6], a5[5,6])

plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     In Degree vs. Load (Mouse, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Out Degree vs. Load (Mouse, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Closeness Centrality vs. Load (Mouse, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Betweenness Centrality vs. Load (Mouse, IS)", ylim=c(-1, 1))

red.v.in <- c(a1[2,7], a2[2,7], a3[2,7], a4[2,7], a5[2,7])
red.v.out <- c(a1[3,7], a2[3,7], a3[3,7], a4[3,7], a5[3,7])
red.v.clc <- c(a1[4,7], a2[4,7], a3[4,7], a4[4,7], a5[4,7])
red.v.btc <- c(a1[5,7], a2[5,7], a3[5,7], a4[5,7], a5[5,7])

plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     In Degree vs. Load (Mouse, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Out Degree vs. Load (Mouse, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Closeness Centrality vs. Load (Mouse, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Betweenness Centrality vs. Load (Mouse, IS)", ylim=c(-1, 1))

ada.v.in <- c(a1[2,8], a2[2,8], a3[2,8], a4[2,8], a5[2,8])
ada.v.out <- c(a1[3,8], a2[3,8], a3[3,8], a4[3,8], a5[3,8])
ada.v.clc <- c(a1[4,8], a2[4,8], a3[4,8], a4[4,8], a5[4,8])
ada.v.btc <- c(a1[5,8], a2[5,8], a3[5,8], a4[5,8], a5[5,8])

plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     In Degree vs. Load (Mouse, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Out Degree vs. Load (Mouse, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Closeness Centrality vs. Load (Mouse, IS)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Betweenness Centrality vs. Load (Mouse, IS)", ylim=c(-1, 1))


##################
# MOUSE, RW
##################
a1<-cor(mouse_RW_0)
a2<-cor(mouse_RW_1)
a3<-cor(mouse_RW_2)
a4<-cor(mouse_RW_3)
a5<-cor(mouse_RW_4)

inf.v.in <- c(a1[2,6], a2[2,6], a3[2,6], a4[2,6], a5[2,6])
inf.v.out <- c(a1[3,6], a2[3,6], a3[3,6], a4[3,6], a5[3,6])
inf.v.clc <- c(a1[4,6], a2[4,6], a3[4,6], a4[4,6], a5[4,6])
inf.v.btc <- c(a1[5,6], a2[5,6], a3[5,6], a4[5,6], a5[5,6])

plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     In Degree vs. Load (Mouse, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Out Degree vs. Load (Mouse, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Closeness Centrality vs. Load (Mouse, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), inf.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Influence and 
     Betweenness Centrality vs. Load (Mouse, RW)", ylim=c(-1, 1))

red.v.in <- c(a1[2,7], a2[2,7], a3[2,7], a4[2,7], a5[2,7])
red.v.out <- c(a1[3,7], a2[3,7], a3[3,7], a4[3,7], a5[3,7])
red.v.clc <- c(a1[4,7], a2[4,7], a3[4,7], a4[4,7], a5[4,7])
red.v.btc <- c(a1[5,7], a2[5,7], a3[5,7], a4[5,7], a5[5,7])

plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     In Degree vs. Load (Mouse, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Out Degree vs. Load (Mouse, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Closeness Centrality vs. Load (Mouse, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), red.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of Redundancy and 
     Betweenness Centrality vs. Load (Mouse, RW)", ylim=c(-1, 1))

ada.v.in <- c(a1[2,8], a2[2,8], a3[2,8], a4[2,8], a5[2,8])
ada.v.out <- c(a1[3,8], a2[3,8], a3[3,8], a4[3,8], a5[3,8])
ada.v.clc <- c(a1[4,8], a2[4,8], a3[4,8], a4[4,8], a5[4,8])
ada.v.btc <- c(a1[5,8], a2[5,8], a3[5,8], a4[5,8], a5[5,8])

plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.in, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     In Degree vs. Load (Mouse, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.out, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Out Degree vs. Load (Mouse, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.clc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Closeness Centrality vs. Load (Mouse, RW)", ylim=c(-1, 1))
plot(c(0, 0.01, 0.05, 0.1, 0.2), ada.v.btc, pch=20, xlab="Load", ylab = "Correlation", main = "Correlation of AverageDeathAge and 
     Betweenness Centrality vs. Load (Mouse, RW)", ylim=c(-1, 1))

plots.dir.path <- list.files(tempdir(), pattern="rs-graphics", full.names = TRUE); 
plots.png.paths <- list.files(plots.dir.path, pattern=".png", full.names = TRUE)

plots.png.detials <- file.info(plots.png.paths)
plots.png.detials <- plots.png.detials[order(plots.png.detials$mtime),]
sorted.png.names <- gsub(plots.dir.path, "cor_plots", row.names(plots.png.detials), fixed=TRUE)
numbered.png.names <- paste0("cor_plots/", 1:length(sorted.png.names), ".png")

# Rename all the .png files as: 1.png, 2.png, 3.png, and so on.
file.rename(from=sorted.png.names, to=numbered.png.names)

file.copy(from=plots.png.paths, to="cor_plots")










