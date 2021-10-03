setwd("C:/Users/aidan/OneDrive/Desktop/aidan-jack-collab")

threshmouse_IS = read.csv("better_correlation_data/threshmouse_for_corr_IS.csv")

# I need a function that
# 1) Takes a file name
# 1.5) Takes an output directory name
# 2) Reads the data in
# 3) Plots the distributions needed
# 4) Saves those files as needed

# I need another function that plots only the pairs I'm interested in
hist(threshmouse_IS$InDeg)
hist(threshmouse_IS$OutDeg)
hist(threshmouse_IS$CloseCent)
hist(threshmouse_IS$BetwnCent)





pairs(threshmouse_IS[2:10], pch=19)
pairs(threshmouse_IS[c(2:5, 16:20)], pch=19)
pairs(threshmouse_IS[c(2:5, 26:30)], pch=19)

























make_corr_p_value_matrix <- function(in_name, method="spearman"){
  in_data = read.csv(in_name)
  
  a0 <- cor.test(in_data$InDeg, in_data$influence_mean_0, method=method)
  a1 <- cor.test(in_data$InDeg, in_data$influence_mean_1, method=method)
  a2 <- cor.test(in_data$InDeg, in_data$influence_mean_2, method=method)
  a3 <- cor.test(in_data$InDeg, in_data$influence_mean_3, method=method)
  a4 <- cor.test(in_data$InDeg, in_data$influence_mean_4, method=method)
  b0 <- cor.test(in_data$OutDeg, in_data$influence_mean_0, method=method)
  b1 <- cor.test(in_data$OutDeg, in_data$influence_mean_1, method=method)
  b2 <- cor.test(in_data$OutDeg, in_data$influence_mean_2, method=method)
  b3 <- cor.test(in_data$OutDeg, in_data$influence_mean_3, method=method)
  b4 <- cor.test(in_data$OutDeg, in_data$influence_mean_4, method=method)
  c0 <- cor.test(in_data$CloseCent, in_data$influence_mean_0, method = method)
  c1 <- cor.test(in_data$CloseCent, in_data$influence_mean_1, method = method)
  c2 <- cor.test(in_data$CloseCent, in_data$influence_mean_2, method = method)
  c3 <- cor.test(in_data$CloseCent, in_data$influence_mean_3, method = method)
  c4 <- cor.test(in_data$CloseCent, in_data$influence_mean_4, method = method)
  d0 <- cor.test(in_data$BetwnCent, in_data$influence_mean_0, method = method)
  d1 <- cor.test(in_data$BetwnCent, in_data$influence_mean_1, method = method)
  d2 <- cor.test(in_data$BetwnCent, in_data$influence_mean_2, method = method)
  d3 <- cor.test(in_data$BetwnCent, in_data$influence_mean_3, method = method)
  d4 <- cor.test(in_data$BetwnCent, in_data$influence_mean_4, method = method)
  
  e0 <- cor.test(in_data$InDeg, in_data$redundancy_mean_0, method=method)
  e1 <- cor.test(in_data$InDeg, in_data$redundancy_mean_1, method=method)
  e2 <- cor.test(in_data$InDeg, in_data$redundancy_mean_2, method=method)
  e3 <- cor.test(in_data$InDeg, in_data$redundancy_mean_3, method=method)
  e4 <- cor.test(in_data$InDeg, in_data$redundancy_mean_4, method=method)
  f0 <- cor.test(in_data$OutDeg, in_data$redundancy_mean_0, method=method)
  f1 <- cor.test(in_data$OutDeg, in_data$redundancy_mean_1, method=method)
  f2 <- cor.test(in_data$OutDeg, in_data$redundancy_mean_2, method=method)
  f3 <- cor.test(in_data$OutDeg, in_data$redundancy_mean_3, method=method)
  f4 <- cor.test(in_data$OutDeg, in_data$redundancy_mean_4, method=method)
  g0 <- cor.test(in_data$CloseCent, in_data$redundancy_mean_0, method=method)
  g1 <- cor.test(in_data$CloseCent, in_data$redundancy_mean_1, method=method)
  g2 <- cor.test(in_data$CloseCent, in_data$redundancy_mean_2, method=method)
  g3 <- cor.test(in_data$CloseCent, in_data$redundancy_mean_3, method=method)
  g4 <- cor.test(in_data$CloseCent, in_data$redundancy_mean_4, method=method)
  h0 <- cor.test(in_data$BetwnCent, in_data$redundancy_mean_0, method=method)
  h1 <- cor.test(in_data$BetwnCent, in_data$redundancy_mean_1, method=method)
  h2 <- cor.test(in_data$BetwnCent, in_data$redundancy_mean_2, method=method)
  h3 <- cor.test(in_data$BetwnCent, in_data$redundancy_mean_3, method=method)
  h4 <- cor.test(in_data$BetwnCent, in_data$redundancy_mean_4, method=method)
  
  i0 <- cor.test(in_data$InDeg, in_data$avgdeathage_mean_0, method=method)
  i1 <- cor.test(in_data$InDeg, in_data$avgdeathage_mean_1, method=method)
  i2 <- cor.test(in_data$InDeg, in_data$avgdeathage_mean_2, method=method)
  i3 <- cor.test(in_data$InDeg, in_data$avgdeathage_mean_3, method=method)
  i4 <- cor.test(in_data$InDeg, in_data$avgdeathage_mean_4, method=method)
  j0 <- cor.test(in_data$OutDeg, in_data$avgdeathage_mean_0, method=method)
  j1 <- cor.test(in_data$OutDeg, in_data$avgdeathage_mean_1, method=method)
  j2 <- cor.test(in_data$OutDeg, in_data$avgdeathage_mean_2, method=method)
  j3 <- cor.test(in_data$OutDeg, in_data$avgdeathage_mean_3, method=method)
  j4 <- cor.test(in_data$OutDeg, in_data$avgdeathage_mean_4, method=method)
  k0 <- cor.test(in_data$CloseCent, in_data$avgdeathage_mean_0, method=method)
  k1 <- cor.test(in_data$CloseCent, in_data$avgdeathage_mean_1, method=method)
  k2 <- cor.test(in_data$CloseCent, in_data$avgdeathage_mean_2, method=method)
  k3 <- cor.test(in_data$CloseCent, in_data$avgdeathage_mean_3, method=method)
  k4 <- cor.test(in_data$CloseCent, in_data$avgdeathage_mean_4, method=method)
  l0 <- cor.test(in_data$BetwnCent, in_data$avgdeathage_mean_0, method=method)
  l1 <- cor.test(in_data$BetwnCent, in_data$avgdeathage_mean_1, method=method)
  l2 <- cor.test(in_data$BetwnCent, in_data$avgdeathage_mean_2, method=method)
  l3 <- cor.test(in_data$BetwnCent, in_data$avgdeathage_mean_3, method=method)
  l4 <- cor.test(in_data$BetwnCent, in_data$avgdeathage_mean_4, method=method)
  
  out_vals = c(a0["estimate"][1], a1["estimate"][1], a2["estimate"][1], a3["estimate"][1], a4["estimate"][1],
               a0["p.value"][1], a1["p.value"][1], a2["p.value"][1], a3["p.value"][1], a4["p.value"][1],
               b0["estimate"][1], b1["estimate"][1], b2["estimate"][1], b3["estimate"][1], b4["estimate"][1],
               b0["p.value"][1], b1["p.value"][1], b2["p.value"][1], b3["p.value"][1], b4["p.value"][1],
               c0["estimate"][1], c1["estimate"][1], c2["estimate"][1], c3["estimate"][1], c4["estimate"][1],
               c0["p.value"][1], c1["p.value"][1], c2["p.value"][1], c3["p.value"][1], c4["p.value"][1],
               d0["estimate"][1], d1["estimate"][1], d2["estimate"][1], d3["estimate"][1], d4["estimate"][1],
               d0["p.value"][1], d1["p.value"][1], d2["p.value"][1], d3["p.value"][1], d4["p.value"][1],
               e0["estimate"][1], e1["estimate"][1], e2["estimate"][1], e3["estimate"][1], e4["estimate"][1],
               e0["p.value"][1], e1["p.value"][1], e2["p.value"][1], e3["p.value"][1], e4["p.value"][1],
               f0["estimate"][1], f1["estimate"][1], f2["estimate"][1], f3["estimate"][1], f4["estimate"][1],
               f0["p.value"][1], f1["p.value"][1], f2["p.value"][1], f3["p.value"][1], f4["p.value"][1],
               g0["estimate"][1], g1["estimate"][1], g2["estimate"][1], g3["estimate"][1], g4["estimate"][1],
               g0["p.value"][1], g1["p.value"][1], g2["p.value"][1], g3["p.value"][1], g4["p.value"][1],
               h0["estimate"][1], h1["estimate"][1], h2["estimate"][1], h3["estimate"][1], h4["estimate"][1],
               h0["p.value"][1], h1["p.value"][1], h2["p.value"][1], h3["p.value"][1], h4["p.value"][1],
               i0["estimate"][1], i1["estimate"][1], i2["estimate"][1], i3["estimate"][1], i4["estimate"][1],
               i0["p.value"][1], i1["p.value"][1], i2["p.value"][1], i3["p.value"][1], i4["p.value"][1],
               j0["estimate"][1], j1["estimate"][1], j2["estimate"][1], j3["estimate"][1], j4["estimate"][1],
               j0["p.value"][1], j1["p.value"][1], j2["p.value"][1], j3["p.value"][1], j4["p.value"][1],
               k0["estimate"][1], k1["estimate"][1], k2["estimate"][1], k3["estimate"][1], k4["estimate"][1],
               k0["p.value"][1], k1["p.value"][1], k2["p.value"][1], k3["p.value"][1], k4["p.value"][1],
               l0["estimate"][1], l1["estimate"][1], l2["estimate"][1], l3["estimate"][1], l4["estimate"][1],
               l0["p.value"][1], l1["p.value"][1], l2["p.value"][1], l3["p.value"][1], l4["p.value"][1])
  
  out = matrix(out_vals, ncol=5, byrow=TRUE)
  return(out)
}

make_corr_p_value_matrix("better_correlation_data/cocomac_for_corr_IS.csv", method="pearson")
make_corr_p_value_matrix("better_correlation_data/cocomac_for_corr_RW.csv", method="pearson")
make_corr_p_value_matrix("better_correlation_data/monkey91_for_corr_IS.csv", method="pearson")
make_corr_p_value_matrix("better_correlation_data/monkey91_for_corr_RW.csv", method="pearson")
make_corr_p_value_matrix("better_correlation_data/threshmouse_for_corr_IS.csv", method="pearson")
make_corr_p_value_matrix("better_correlation_data/threshmouse_for_corr_RW.csv", method="pearson")














make_corr_p_value_matrix("thresh_er_0_anly/mouse_er_0_IS_stact_stats.csv", method="pearson")
make_corr_p_value_matrix("thresh_er_0_anly/mouse_er_0_RW_stact_stats.csv", method="pearson")
make_corr_p_value_matrix("thresh_er_1_anly/mouse_er_1_IS_stact_stats.csv", method="pearson")
make_corr_p_value_matrix("thresh_er_1_anly/mouse_er_1_RW_stact_stats.csv", method="pearson")
make_corr_p_value_matrix("thresh_ms_0_anly/mouse_ms_0_IS_stact_stats.csv", method="pearson")
make_corr_p_value_matrix("thresh_ms_0_anly/mouse_ms_0_RW_stact_stats.csv", method="pearson")
make_corr_p_value_matrix("thresh_ms_1_anly/mouse_ms_1_IS_stact_stats.csv", method="pearson")
make_corr_p_value_matrix("thresh_ms_1_anly/mouse_ms_1_RW_stact_stats.csv", method="pearson")
make_corr_p_value_matrix("thresh_sf_0_anly/mouse_sf_0_IS_stact_stats.csv", method="pearson")
make_corr_p_value_matrix("thresh_sf_0_anly/mouse_sf_0_RW_stact_stats.csv", method="pearson")
make_corr_p_value_matrix("thresh_sf_1_anly/mouse_sf_1_IS_stact_stats.csv", method="pearson")
make_corr_p_value_matrix("thresh_sf_1_anly/mouse_sf_1_RW_stact_stats.csv", method="pearson")

make_corr_p_value_matrix("better_correlation_data/threshmouse_for_corr_IS.csv", method="spearman")
make_corr_p_value_matrix("better_correlation_data/threshmouse_for_corr_RW.csv", method="spearman")
make_corr_p_value_matrix("thresh_er_0_anly/mouse_er_0_IS_stact_stats.csv", method="spearman")
make_corr_p_value_matrix("thresh_er_0_anly/mouse_er_0_RW_stact_stats.csv", method="spearman")
make_corr_p_value_matrix("thresh_er_1_anly/mouse_er_1_IS_stact_stats.csv", method="spearman")
make_corr_p_value_matrix("thresh_er_1_anly/mouse_er_1_RW_stact_stats.csv", method="spearman")
make_corr_p_value_matrix("thresh_ms_0_anly/mouse_ms_0_IS_stact_stats.csv", method="spearman")
make_corr_p_value_matrix("thresh_ms_0_anly/mouse_ms_0_RW_stact_stats.csv", method="spearman")
make_corr_p_value_matrix("thresh_ms_1_anly/mouse_ms_1_IS_stact_stats.csv", method="spearman")
make_corr_p_value_matrix("thresh_ms_1_anly/mouse_ms_1_RW_stact_stats.csv", method="spearman")
make_corr_p_value_matrix("thresh_sf_0_anly/mouse_sf_0_IS_stact_stats.csv", method="spearman")
make_corr_p_value_matrix("thresh_sf_0_anly/mouse_sf_0_RW_stact_stats.csv", method="spearman")
make_corr_p_value_matrix("thresh_sf_1_anly/mouse_sf_1_IS_stact_stats.csv", method="spearman")
make_corr_p_value_matrix("thresh_sf_1_anly/mouse_sf_1_RW_stact_stats.csv", method="spearman")





















