library(ggplot2)
library(dplyr)
library(hrbrthemes)


# Build dataset with different distributions
data <- data.frame(
  type = c( rep("variable 1", 1000), rep("variable 2", 1000) ),
  value = c( rnorm(1000), rnorm(1000, mean=4) )
)

# Represent it
p <- data %>%
  ggplot( aes(x=value, fill=type)) +
  geom_histogram( color="#e9ecef", alpha=0.6, position = 'identity') +
  scale_fill_manual(values=c("#69b3a2", "#404080")) +
  theme_ipsum() +
  labs(fill="")
p

setwd("C:/Users/aidan/OneDrive/Desktop/aidan-jack-collab")

coco_IS = read.csv("better_correlation_data/cocomac_for_corr_IS.csv")
coco_RW = read.csv("better_correlation_data/cocomac_for_corr_RW.csv")
monkey91_IS = read.csv("better_correlation_data/monkey91_for_corr_IS.csv")
monkey91_RW = read.csv("better_correlation_data/monkey91_for_corr_RW.csv")
threshmouse_IS = read.csv("better_correlation_data/threshmouse_for_corr_IS.csv")
threshmouse_RW = read.csv("better_correlation_data/threshmouse_for_corr_RW.csv")

data <- data.frame(
  type = c( rep("L=1", 184), rep("L=0.01", 184), rep("L=0.05", 184), rep("L=0.1", 184), rep("L=0.2", 184)),
  value = c( coco_IS$influence_mean_0, coco_IS$influence_mean_1, coco_IS$influence_mean_2, coco_IS$influence_mean_3, coco_IS$influence_mean_4)
)

p <- data %>%
  ggplot(aes(x=value, fill=type)) +
  geom_histogram(color="#ffffff", alpha=0.3, position="identity") +
  scale_fill_manual(values=c("#f00000", "#0f0000", "#00f000", "#000f00", "#0000f0")) +
  theme_ipsum() +
  labs(fill="")
p
