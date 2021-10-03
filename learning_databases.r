setwd("C:/Users/aidan/OneDrive/Desktop/aidan-jack-collab")

coco_IS_1 = read.csv("cocomac_IS_stact/cocomac_IS_stact_stats_1.csv")

in_names = c("cocomac_IS_stact/cocomac_IS_stact_stats_1.csv",
             "cocomac_IS_stact/cocomac_IS_stact_stats_1.csv",
             "cocomac_IS_stact/cocomac_IS_stact_stats_2.csv",
             "cocomac_IS_stact/cocomac_IS_stact_stats_3.csv",
             "cocomac_IS_stact/cocomac_IS_stact_stats_4.csv",
             "cocomac_RW_stact/cocomac_RW_stact_stats_0.csv",
             "cocomac_RW_stact/cocomac_RW_stact_stats_1.csv",
             "cocomac_RW_stact/cocomac_RW_stact_stats_2.csv",
             "cocomac_RW_stact/cocomac_RW_stact_stats_3.csv",
             "cocomac_RW_stact/cocomac_RW_stact_stats_4.csv",
             "monkey91_IS_stact/monkey91_IS_stact_stats_0.csv",
             "monkey91_IS_stact/monkey91_IS_stact_stats_1.csv",
             "monkey91_IS_stact/monkey91_IS_stact_stats_2.csv",
             "monkey91_IS_stact/monkey91_IS_stact_stats_3.csv",
             "monkey91_IS_stact/monkey91_IS_stact_stats_4.csv",
             "monkey91_RW_stact/monkey91_RW_stact_stats_0.csv",
             "monkey91_RW_stact/monkey91_RW_stact_stats_1.csv",
             "monkey91_RW_stact/monkey91_RW_stact_stats_2.csv",
             "monkey91_RW_stact/monkey91_RW_stact_stats_3.csv",
             "monkey91_RW_stact/monkey91_RW_stact_stats_4.csv",
             "mouse_IS_stact/mouse_IS_stact_stats_0.csv",
             "mouse_IS_stact/mouse_IS_stact_stats_1.csv",
             "mouse_IS_stact/mouse_IS_stact_stats_2.csv",
             "mouse_IS_stact/mouse_IS_stact_stats_3.csv",
             "mouse_IS_stact/mouse_IS_stact_stats_4.csv",
             "mouse_RW_stact/mouse_RW_stact_stats_0.csv",
             "mouse_RW_stact/mouse_RW_stact_stats_1.csv",
             "mouse_RW_stact/mouse_RW_stact_stats_2.csv",
             "mouse_RW_stact/mouse_RW_stact_stats_3.csv",
             "mouse_RW_stact/mouse_RW_stact_stats_4.csv")

prefixes = c("Cocomac, IS, L=1",
             "Cocomac, IS, L=0.01",
             "Cocomac, IS, L=0.05",
             "Cocomac, IS, L=0.1",
             "Cocomac, IS, L=0.2",
             "Cocomac, RW, L=1",
             "Cocomac, RW, L=0.01",
             "Cocomac, RW, L=0.05",
             "Cocomac, RW, L=0.1",
             "Cocomac, RW, L=0.2",
             "Monkey91, IS, L=1",
             "Monkey91, IS, L=0.01",
             "Monkey91, IS, L=0.05",
             "Monkey91, IS, L=0.1",
             "Monkey91, IS, L=0.2",
             "Monkey91, RW, L=1",
             "Monkey91, RW, L=0.01",
             "Monkey91, RW, L=0.05",
             "Monkey91, RW, L=0.1",
             "Monkey91, RW, L=0.2",
             "Mouse, IS, L=1",
             "Mouse, IS, L=0.01",
             "Mouse, IS, L=0.05",
             "Mouse, IS, L=0.1",
             "Mouse, IS, L=0.2",
             "Mouse, RW, L=1",
             "Mouse, RW, L=0.01",
             "Mouse, RW, L=0.05",
             "Mouse, RW, L=0.1",
             "Mouse, RW, L=0.2")


# This method reads in the file named in_name, and outputs 
# some graphics into a folder

# Let's just make one directory and store the number in the prefix

make_plots_and_data <- function(in_name, prefix, dir_name) {
  # Load the data in
  data_set <- read.csv(in_name)
  
  # Make all the header names
  influence_name = paste(prefix, "Influence Dsbn", sep = " ")
  redundancy_name = paste(prefix, "Redundancy Dsbn", sep = " ")
  avgdeathage_name = paste(prefix, "AvgDeathAge", sep = " ")
  
  dir.create(dir_name)
  
  # make the file names
  influence_file = paste(dir_name, "/influence.svg", sep="")
  redundancy_file = paste(dir_name, "/redundancy.svg", sep="")
  avgdeathage_file = paste(dir_name, "/avgdeathage.svg", sep="")
  pair_file = paste(dir_name, "/pairs.svg", sep="")
  
  # Plot these distributions
  svg(influence_file)
  hist(data_set$Influence, xlab = "Influence", main = influence_name)
  dev.off()
  
  svg(redundancy_file)
  hist(data_set$Redundancy, xlab = "Redundancy", main = redundancy_name)
  dev.off()
  
  svg(avgdeathage_file)
  hist(data_set$AvgDeathAge, xlab = "AvgDeathAge", main = avgdeathage_name)
  dev.off()
  
  svg(pair_file)
  pairs(data_set[-1], pch=19)
  dev.off()
  
  
  # go back to the parent directory
  setwd("C:/Users/aidan/OneDrive/Desktop/aidan-jack-collab")
}


for (i in 1:30){
  name = paste("graphics", i, sep="_")
  make_plots_and_data(in_names[i], prefixes[i], name)
}

plots.dir.path <- list.files(tempdir(), pattern="rs-graphics", full.names = TRUE); 
plots.png.paths <- list.files(plots.dir.path, pattern=".png", full.names = TRUE)
file.copy(from=plots.png.paths, to="cor_plots")














