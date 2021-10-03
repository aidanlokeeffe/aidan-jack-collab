setwd("C:/Users/aidan/OneDrive/Desktop/aidan-jack-collab")

coco_IS = read.csv("better_correlation_data/cocomac_for_corr_IS.csv")
coco_RW = read.csv("better_correlation_data/cocomac_for_corr_RW.csv")
monkey91_IS = read.csv("better_correlation_data/monkey91_for_corr_IS.csv")
monkey91_RW = read.csv("better_correlation_data/monkey91_for_corr_RW.csv")
threshmouse_IS = read.csv("better_correlation_data/threshmouse_for_corr_IS.csv")
threshmouse_RW = read.csv("better_correlation_data/threshmouse_for_corr_RW.csv")

MK1Struct <- read.csv("monkey1_struct.csv")
MK2Struct <- read.csv("monkey2_struct.csv")
MSStruct <- read.csv("mouse_struct.csv")

######### Influence vs. Out Close Cent 
# Monkey1 IS
a <- cor(MK1Struct$OutCloseCent, monkey91_IS$influence_mean_0)
b <- cor(MK1Struct$OutCloseCent, monkey91_IS$influence_mean_1)
c <- cor(MK1Struct$OutCloseCent, monkey91_IS$influence_mean_2)
d <- cor(MK1Struct$OutCloseCent, monkey91_IS$influence_mean_3)
e <- cor(MK1Struct$OutCloseCent, monkey91_IS$influence_mean_4)
c(a,b,c,d,e)

# Monkey1 RW
a <- cor(MK1Struct$OutCloseCent, monkey91_RW$influence_mean_0)
b <- cor(MK1Struct$OutCloseCent, monkey91_RW$influence_mean_1)
c <- cor(MK1Struct$OutCloseCent, monkey91_RW$influence_mean_2)
d <- cor(MK1Struct$OutCloseCent, monkey91_RW$influence_mean_3)
e <- cor(MK1Struct$OutCloseCent, monkey91_RW$influence_mean_4)
c(a,b,c,d,e)

# Monkey2 IS
a <- cor(MK2Struct$OutCloseCent, coco_IS$influence_mean_0)
b <- cor(MK2Struct$OutCloseCent, coco_IS$influence_mean_1)
c <- cor(MK2Struct$OutCloseCent, coco_IS$influence_mean_2)
d <- cor(MK2Struct$OutCloseCent, coco_IS$influence_mean_3)
e <- cor(MK2Struct$OutCloseCent, coco_IS$influence_mean_4)
c(a,b,c,d,e)

# Monkey2 RW
a <- cor(MK2Struct$OutCloseCent, coco_RW$influence_mean_0)
b <- cor(MK2Struct$OutCloseCent, coco_RW$influence_mean_1)
c <- cor(MK2Struct$OutCloseCent, coco_RW$influence_mean_2)
d <- cor(MK2Struct$OutCloseCent, coco_RW$influence_mean_3)
e <- cor(MK2Struct$OutCloseCent, coco_RW$influence_mean_4)
c(a,b,c,d,e)

# Mouse IS
a <- cor(MSStruct$OutCloseCent, threshmouse_IS$influence_mean_0)
b <- cor(MSStruct$OutCloseCent, threshmouse_IS$influence_mean_1)
c <- cor(MSStruct$OutCloseCent, threshmouse_IS$influence_mean_2)
d <- cor(MSStruct$OutCloseCent, threshmouse_IS$influence_mean_3)
e <- cor(MSStruct$OutCloseCent, threshmouse_IS$influence_mean_4)
c(a,b,c,d,e)

# Mouse RW
a <- cor(MSStruct$OutCloseCent, threshmouse_RW$influence_mean_0)
b <- cor(MSStruct$OutCloseCent, threshmouse_RW$influence_mean_1)
c <- cor(MSStruct$OutCloseCent, threshmouse_RW$influence_mean_2)
d <- cor(MSStruct$OutCloseCent, threshmouse_RW$influence_mean_3)
e <- cor(MSStruct$OutCloseCent, threshmouse_RW$influence_mean_4)
c(a,b,c,d,e)

######### Redundancy vs. Out Close Cent
# Monkey1 IS
a <- cor(MK1Struct$OutCloseCent, monkey91_IS$redundancy_mean_0)
b <- cor(MK1Struct$OutCloseCent, monkey91_IS$redundancy_mean_1)
c <- cor(MK1Struct$OutCloseCent, monkey91_IS$redundancy_mean_2)
d <- cor(MK1Struct$OutCloseCent, monkey91_IS$redundancy_mean_3)
e <- cor(MK1Struct$OutCloseCent, monkey91_IS$redundancy_mean_4)
c(a,b,c,d,e)

# Monkey1 RW
a <- cor(MK1Struct$OutCloseCent, monkey91_RW$redundancy_mean_0)
b <- cor(MK1Struct$OutCloseCent, monkey91_RW$redundancy_mean_1)
c <- cor(MK1Struct$OutCloseCent, monkey91_RW$redundancy_mean_2)
d <- cor(MK1Struct$OutCloseCent, monkey91_RW$redundancy_mean_3)
e <- cor(MK1Struct$OutCloseCent, monkey91_RW$redundancy_mean_4)
c(a,b,c,d,e)

# Monkey2 IS
a <- cor(MK2Struct$OutCloseCent, coco_IS$redundancy_mean_0)
b <- cor(MK2Struct$OutCloseCent, coco_IS$redundancy_mean_1)
c <- cor(MK2Struct$OutCloseCent, coco_IS$redundancy_mean_2)
d <- cor(MK2Struct$OutCloseCent, coco_IS$redundancy_mean_3)
e <- cor(MK2Struct$OutCloseCent, coco_IS$redundancy_mean_4)
c(a,b,c,d,e)

# Monkey2 RW
a <- cor(MK2Struct$OutCloseCent, coco_RW$redundancy_mean_0)
b <- cor(MK2Struct$OutCloseCent, coco_RW$redundancy_mean_1)
c <- cor(MK2Struct$OutCloseCent, coco_RW$redundancy_mean_2)
d <- cor(MK2Struct$OutCloseCent, coco_RW$redundancy_mean_3)
e <- cor(MK2Struct$OutCloseCent, coco_RW$redundancy_mean_4)
c(a,b,c,d,e)

# Mouse IS
a <- cor(MSStruct$OutCloseCent, threshmouse_IS$redundancy_mean_0)
b <- cor(MSStruct$OutCloseCent, threshmouse_IS$redundancy_mean_1)
c <- cor(MSStruct$OutCloseCent, threshmouse_IS$redundancy_mean_2)
d <- cor(MSStruct$OutCloseCent, threshmouse_IS$redundancy_mean_3)
e <- cor(MSStruct$OutCloseCent, threshmouse_IS$redundancy_mean_4)
c(a,b,c,d,e)

# Mouse RW
a <- cor(MSStruct$OutCloseCent, threshmouse_RW$redundancy_mean_0)
b <- cor(MSStruct$OutCloseCent, threshmouse_RW$redundancy_mean_1)
c <- cor(MSStruct$OutCloseCent, threshmouse_RW$redundancy_mean_2)
d <- cor(MSStruct$OutCloseCent, threshmouse_RW$redundancy_mean_3)
e <- cor(MSStruct$OutCloseCent, threshmouse_RW$redundancy_mean_4)
c(a,b,c,d,e)



######### Redundancy vs. Betweenness Centrality
# Monkey1 IS
a <- cor(monkey91_IS$BetwnCent, monkey91_IS$influence_mean_0)
b <- cor(monkey91_IS$BetwnCent, monkey91_IS$influence_mean_1)
c <- cor(monkey91_IS$BetwnCent, monkey91_IS$influence_mean_2)
d <- cor(monkey91_IS$BetwnCent, monkey91_IS$influence_mean_3)
e <- cor(monkey91_IS$BetwnCent, monkey91_IS$influence_mean_4)
c(a,b,c,d,e)

# Monkey1 RW
a <- cor(monkey91_IS$BetwnCent, monkey91_RW$influence_mean_0)
b <- cor(monkey91_IS$BetwnCent, monkey91_RW$influence_mean_1)
c <- cor(monkey91_IS$BetwnCent, monkey91_RW$influence_mean_2)
d <- cor(monkey91_IS$BetwnCent, monkey91_RW$influence_mean_3)
e <- cor(monkey91_IS$BetwnCent, monkey91_RW$influence_mean_4)
c(a,b,c,d,e)

# Monkey2 IS
a <- cor(coco_IS$BetwnCent, coco_IS$influence_mean_0)
b <- cor(coco_IS$BetwnCent, coco_IS$influence_mean_1)
c <- cor(coco_IS$BetwnCent, coco_IS$influence_mean_2)
d <- cor(coco_IS$BetwnCent, coco_IS$influence_mean_3)
e <- cor(coco_IS$BetwnCent, coco_IS$influence_mean_4)
c(a,b,c,d,e)

# Monkey2 RW
a <- cor(coco_IS$BetwnCent, coco_RW$influence_mean_0)
b <- cor(coco_IS$BetwnCent, coco_RW$influence_mean_1)
c <- cor(coco_IS$BetwnCent, coco_RW$influence_mean_2)
d <- cor(coco_IS$BetwnCent, coco_RW$influence_mean_3)
e <- cor(coco_IS$BetwnCent, coco_RW$influence_mean_4)
c(a,b,c,d,e)

# Mouse IS
a <- cor(threshmouse_IS$BetwnCent, threshmouse_IS$influence_mean_0)
b <- cor(threshmouse_IS$BetwnCent, threshmouse_IS$influence_mean_1)
c <- cor(threshmouse_IS$BetwnCent, threshmouse_IS$influence_mean_2)
d <- cor(threshmouse_IS$BetwnCent, threshmouse_IS$influence_mean_3)
e <- cor(threshmouse_IS$BetwnCent, threshmouse_IS$influence_mean_4)
c(a,b,c,d,e)

# Mouse RW
a <- cor(threshmouse_IS$BetwnCent, threshmouse_RW$influence_mean_0)
b <- cor(threshmouse_IS$BetwnCent, threshmouse_RW$influence_mean_1)
c <- cor(threshmouse_IS$BetwnCent, threshmouse_RW$influence_mean_2)
d <- cor(threshmouse_IS$BetwnCent, threshmouse_RW$influence_mean_3)
e <- cor(threshmouse_IS$BetwnCent, threshmouse_RW$influence_mean_4)
c(a,b,c,d,e)















