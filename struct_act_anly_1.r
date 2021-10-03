setwd("C:/Users/aidan/OneDrive/Desktop/aidan-jack-collab")

#CocoSA = read.csv("dir_cocomac_struct_act_stats.csv")

# make a data frame for cocomac
# plot all of the scatterplots act vs. struct
# give me all the correlations

###################
# GET ALL THE DATAFRAMES!!!
###################


cols <- colnames(coco_IS_0)
cols[1]
length(cols)


can_store_dfs_as_vector <- c(coco_IS_0, coco_IS_1)
can_store_dfs_as_vector



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


###################
# PLOT THE INFLUENCE VALUES
###################
hist(coco_IS_0$Influence, main = "Influence Distribution (Cocomac, IS, L=1)", xlab = "Influence")
hist(coco_IS_1$Influence, main = "Influence Distribution (Cocomac, IS, L=0.01)", xlab = "Influence")
hist(coco_IS_2$Influence, main = "Influence Distribution (Cocomac, IS, L=0.05)", xlab = "Influence")
hist(coco_IS_3$Influence, main = "Influence Distribution (Cocomac, IS, L=0.1)", xlab = "Influence")
hist(coco_IS_4$Influence, main = "Influence Distribution (Cocomac, IS, L=0.2)", xlab = "Influence")

hist(coco_RW_0$Influence, main = "Influence Distribution (Cocomac, RW, L=1)", xlab = "Influence")
hist(coco_RW_1$Influence, main = "Influence Distribution (Cocomac, RW, L=0.01)", xlab = "Influence")
hist(coco_RW_2$Influence, main = "Influence Distribution (Cocomac, RW, L=0.05)", xlab = "Influence")
hist(coco_RW_3$Influence, main = "Influence Distribution (Cocomac, RW, L=0.1)", xlab = "Influence")
hist(coco_RW_4$Influence, main = "Influence Distribution (Cocomac, RW, L=0.2)", xlab = "Influence")

hist(monkey_IS_0$Influence, main = "Influence Distribution (Monkey91, IS, L=1)", xlab = "Influence")
hist(monkey_IS_1$Influence, main = "Influence Distribution (Monkey91, IS, L=0.01)", xlab = "Influence")
hist(monkey_IS_2$Influence, main = "Influence Distribution (Monkey91, IS, L=0.05)", xlab = "Influence")
hist(monkey_IS_3$Influence, main = "Influence Distribution (Monkey91, IS, L=0.1)", xlab = "Influence")
hist(monkey_IS_4$Influence, main = "Influence Distribution (Monkey91, IS, L=0.2)", xlab = "Influence")

hist(monkey_RW_0$Influence, main = "Influence Distribution (Monkey91, RW, L=1)", xlab = "Influence")
hist(monkey_RW_1$Influence, main = "Influence Distribution (Monkey91, RW, L=0.01)", xlab = "Influence")
hist(monkey_RW_2$Influence, main = "Influence Distribution (Monkey91, RW, L=0.05)", xlab = "Influence")
hist(monkey_RW_3$Influence, main = "Influence Distribution (Monkey91, RW, L=0.1)", xlab = "Influence")
hist(monkey_RW_4$Influence, main = "Influence Distribution (Monkey91, RW, L=0.2)", xlab = "Influence")

hist(mouse_IS_0$Influence, main = "Influence Distribution (Mouse, IS, L=1)", xlab = "Influence")
hist(mouse_IS_1$Influence, main = "Influence Distribution (Mouse, IS, L=0.01)", xlab = "Influence")
hist(mouse_IS_2$Influence, main = "Influence Distribution (Mouse, IS, L=0.05)", xlab = "Influence")
hist(mouse_IS_3$Influence, main = "Influence Distribution (Mouse, IS, L=0.1)", xlab = "Influence")
hist(mouse_IS_4$Influence, main = "Influence Distribution (Mouse, IS, L=0.2)", xlab = "Influence")

hist(mouse_RW_0$Influence, main = "Influence Distribution (Mouse, RW, L=1)", xlab = "Influence")
hist(mouse_RW_1$Influence, main = "Influence Distribution (Mouse, RW, L=0.01)", xlab = "Influence")
hist(mouse_RW_2$Influence, main = "Influence Distribution (Mouse, RW, L=0.05)", xlab = "Influence")
hist(mouse_RW_3$Influence, main = "Influence Distribution (Mouse, RW, L=0.1)", xlab = "Influence")
hist(mouse_RW_4$Influence, main = "Influence Distribution (Mouse, RW, L=0.2)", xlab = "Influence")

###################
# PLOT THE REDUNCANCY
###################
hist(coco_IS_0$Redundancy, main = "Redundancy Distribution (Cocomac, IS, L=1)", xlab = "Redundancy")
hist(coco_IS_1$Redundancy, main = "Redundancy Distribution (Cocomac, IS, L=0.01)", xlab = "Redundancy")
hist(coco_IS_2$Redundancy, main = "Redundancy Distribution (Cocomac, IS, L=0.05)", xlab = "Redundancy")
hist(coco_IS_3$Redundancy, main = "Redundancy Distribution (Cocomac, IS, L=0.1)", xlab = "Redundancy")
hist(coco_IS_4$Redundancy, main = "Redundancy Distribution (Cocomac, IS, L=0.2)", xlab = "Redundancy")

hist(coco_RW_0$Redundancy, main = "Redundancy Distribution (Cocomac, RW, L=1)", xlab = "Redundancy")
hist(coco_RW_1$Redundancy, main = "Redundancy Distribution (Cocomac, RW, L=0.01)", xlab = "Redundancy")
hist(coco_RW_2$Redundancy, main = "Redundancy Distribution (Cocomac, RW, L=0.05)", xlab = "Redundancy")
hist(coco_RW_3$Redundancy, main = "Redundancy Distribution (Cocomac, RW, L=0.1)", xlab = "Redundancy")
hist(coco_RW_4$Redundancy, main = "Redundancy Distribution (Cocomac, RW, L=0.2)", xlab = "Redundancy")

hist(monkey_IS_0$Redundancy, main = "Redundancy Distribution (Monkey91, IS, L=1)", xlab = "Redundancy")
hist(monkey_IS_1$Redundancy, main = "Redundancy Distribution (Monkey91, IS, L=0.01)", xlab = "Redundancy")
hist(monkey_IS_2$Redundancy, main = "Redundancy Distribution (Monkey91, IS, L=0.05)", xlab = "Redundancy")
hist(monkey_IS_3$Redundancy, main = "Redundancy Distribution (Monkey91, IS, L=0.1)", xlab = "Redundancy")
hist(monkey_IS_4$Redundancy, main = "Redundancy Distribution (Monkey91, IS, L=0.2)", xlab = "Redundancy")

hist(monkey_RW_0$Redundancy, main = "Redundancy Distribution (Monkey91, RW, L=1)", xlab = "Redundancy")
hist(monkey_RW_1$Redundancy, main = "Redundancy Distribution (Monkey91, RW, L=0.01)", xlab = "Redundancy")
hist(monkey_RW_2$Redundancy, main = "Redundancy Distribution (Monkey91, RW, L=0.05)", xlab = "Redundancy")
hist(monkey_RW_3$Redundancy, main = "Redundancy Distribution (Monkey91, RW, L=0.1)", xlab = "Redundancy")
hist(monkey_RW_4$Redundancy, main = "Redundancy Distribution (Monkey91, RW, L=0.2)", xlab = "Redundancy")

hist(mouse_IS_0$Redundancy, main = "Redundancy Distribution (Mouse, IS, L=1)", xlab = "Redundancy")
hist(mouse_IS_1$Redundancy, main = "Redundancy Distribution (Mouse, IS, L=0.01)", xlab = "Redundancy")
hist(mouse_IS_2$Redundancy, main = "Redundancy Distribution (Mouse, IS, L=0.05)", xlab = "Redundancy")
hist(mouse_IS_3$Redundancy, main = "Redundancy Distribution (Mouse, IS, L=0.1)", xlab = "Redundancy")
hist(mouse_IS_4$Redundancy, main = "Redundancy Distribution (Mouse, IS, L=0.2)", xlab = "Redundancy")

hist(mouse_RW_0$Redundancy, main = "Redundancy Distribution (Mouse, RW, L=1)", xlab = "Redundancy")
hist(mouse_RW_1$Redundancy, main = "Redundancy Distribution (Mouse, RW, L=0.01)", xlab = "Redundancy")
hist(mouse_RW_2$Redundancy, main = "Redundancy Distribution (Mouse, RW, L=0.05)", xlab = "Redundancy")
hist(mouse_RW_3$Redundancy, main = "Redundancy Distribution (Mouse, RW, L=0.1)", xlab = "Redundancy")
hist(mouse_RW_4$Redundancy, main = "Redundancy Distribution (Mouse, RW, L=0.2)", xlab = "Redundancy")

###################
# PLOT THE AVERAGE AGE AT DEATH
###################
hist(coco_IS_0$AvgDeathAge, main = "AvgDeathAge Distribution (Cocomac, IS, L=1)", xlab = "AvgDeathAge")
hist(coco_IS_1$AvgDeathAge, main = "AvgDeathAge Distribution (Cocomac, IS, L=0.01)", xlab = "AvgDeathAge")
hist(coco_IS_2$AvgDeathAge, main = "AvgDeathAge Distribution (Cocomac, IS, L=0.05)", xlab = "AvgDeathAge")
hist(coco_IS_3$AvgDeathAge, main = "AvgDeathAge Distribution (Cocomac, IS, L=0.1)", xlab = "AvgDeathAge")
hist(coco_IS_4$AvgDeathAge, main = "AvgDeathAge Distribution (Cocomac, IS, L=0.2)", xlab = "AvgDeathAge")

hist(coco_RW_0$AvgDeathAge, main = "AvgDeathAge Distribution (Cocomac, RW, L=1)", xlab = "AvgDeathAge")
hist(coco_RW_1$AvgDeathAge, main = "AvgDeathAge Distribution (Cocomac, RW, L=0.01)", xlab = "AvgDeathAge")
hist(coco_RW_2$AvgDeathAge, main = "AvgDeathAge Distribution (Cocomac, RW, L=0.05)", xlab = "AvgDeathAge")
hist(coco_RW_3$AvgDeathAge, main = "AvgDeathAge Distribution (Cocomac, RW, L=0.1)", xlab = "AvgDeathAge")
hist(coco_RW_4$AvgDeathAge, main = "AvgDeathAge Distribution (Cocomac, RW, L=0.2)", xlab = "AvgDeathAge")

hist(monkey_IS_0$AvgDeathAge, main = "AvgDeathAge Distribution (Monkey91, IS, L=1)", xlab = "AvgDeathAge")
hist(monkey_IS_1$AvgDeathAge, main = "AvgDeathAge Distribution (Monkey91, IS, L=0.01)", xlab = "AvgDeathAge")
hist(monkey_IS_2$AvgDeathAge, main = "AvgDeathAge Distribution (Monkey91, IS, L=0.05)", xlab = "AvgDeathAge")
hist(monkey_IS_3$AvgDeathAge, main = "AvgDeathAge Distribution (Monkey91, IS, L=0.1)", xlab = "AvgDeathAge")
hist(monkey_IS_4$AvgDeathAge, main = "AvgDeathAge Distribution (Monkey91, IS, L=0.2)", xlab = "AvgDeathAge")

hist(monkey_RW_0$AvgDeathAge, main = "AvgDeathAge Distribution (Monkey91, RW, L=1)", xlab = "AvgDeathAge")
hist(monkey_RW_1$AvgDeathAge, main = "AvgDeathAge Distribution (Monkey91, RW, L=0.01)", xlab = "AvgDeathAge")
hist(monkey_RW_2$AvgDeathAge, main = "AvgDeathAge Distribution (Monkey91, RW, L=0.05)", xlab = "AvgDeathAge")
hist(monkey_RW_3$AvgDeathAge, main = "AvgDeathAge Distribution (Monkey91, RW, L=0.1)", xlab = "AvgDeathAge")
hist(monkey_RW_4$AvgDeathAge, main = "AvgDeathAge Distribution (Monkey91, RW, L=0.2)", xlab = "AvgDeathAge")

hist(mouse_IS_0$AvgDeathAge, main = "AvgDeathAge Distribution (Mouse, IS, L=1)", xlab = "AvgDeathAge")
hist(mouse_IS_1$AvgDeathAge, main = "AvgDeathAge Distribution (Mouse, IS, L=0.01)", xlab = "AvgDeathAge")
hist(mouse_IS_2$AvgDeathAge, main = "AvgDeathAge Distribution (Mouse, IS, L=0.05)", xlab = "AvgDeathAge")
hist(mouse_IS_3$AvgDeathAge, main = "AvgDeathAge Distribution (Mouse, IS, L=0.1)", xlab = "AvgDeathAge")
hist(mouse_IS_4$AvgDeathAge, main = "AvgDeathAge Distribution (Mouse, IS, L=0.2)", xlab = "AvgDeathAge")

hist(mouse_RW_0$AvgDeathAge, main = "AvgDeathAge Distribution (Mouse, RW, L=1)", xlab = "AvgDeathAge")
hist(mouse_RW_1$AvgDeathAge, main = "AvgDeathAge Distribution (Mouse, RW, L=0.01)", xlab = "AvgDeathAge")
hist(mouse_RW_2$AvgDeathAge, main = "AvgDeathAge Distribution (Mouse, RW, L=0.05)", xlab = "AvgDeathAge")
hist(mouse_RW_3$AvgDeathAge, main = "AvgDeathAge Distribution (Mouse, RW, L=0.1)", xlab = "AvgDeathAge")
hist(mouse_RW_4$AvgDeathAge, main = "AvgDeathAge Distribution (Mouse, RW, L=0.2)", xlab = "AvgDeathAge")

###################
# PLOT THE AVERAGE AGE AT DEATH
###################

#plots.dir.path <- list.files(tempdir(), pattern="rs-graphics", full.names=TRUE)
#plots.png.paths <- list.files(plots.dir.path, pattern=".png", full.names=TRUE)

#file.copy(from=plots.png.paths, to="aidan_graphics")

plot(coco_IS_0$AvgDeathAge, coco_IS_3$Influence, pch=20)
plot(coco_IS_1$AvgDeathAge, coco_IS_3$Influence, pch=20)
plot(coco_IS_2$AvgDeathAge, coco_IS_3$Influence, pch=20)
plot(coco_IS_3$AvgDeathAge, coco_IS_3$Influence, pch=20)
plot(coco_IS_4$AvgDeathAge, coco_IS_3$Influence, pch=20)

# for cocomac only

# AvgDeathAge
summary(coco_IS_0$AvgDeathAge)
sd(coco_IS_0$AvgDeathAge)

summary(coco_IS_1$AvgDeathAge)
sd(coco_IS_1$AvgDeathAge)

summary(coco_IS_2$AvgDeathAge)
sd(coco_IS_2$AvgDeathAge)

summary(coco_IS_3$AvgDeathAge)
sd(coco_IS_3$AvgDeathAge)

summary(coco_IS_4$AvgDeathAge)
sd(coco_IS_4$AvgDeathAge)


# Redundancy
summary(coco_IS_0$Redundancy)
sd(coco_IS_0$Redundancy)

summary(coco_IS_1$Redundancy)
sd(coco_IS_1$Redundancy)

summary(coco_IS_2$Redundancy)
sd(coco_IS_2$Redundancy)

summary(coco_IS_3$Redundancy)
sd(coco_IS_3$Redundancy)

summary(coco_IS_4$Redundancy)
sd(coco_IS_4$Redundancy)


#Influence
summary(coco_IS_0$Influence)
sd(coco_IS_0$Influence)

summary(coco_IS_1$Influence)
sd(coco_IS_1$Influence)

summary(coco_IS_2$Influence)
sd(coco_IS_2$Influence)

summary(coco_IS_3$Influence)
sd(coco_IS_3$Influence)

summary(coco_IS_4$Influence)
sd(coco_IS_4$Influence)


