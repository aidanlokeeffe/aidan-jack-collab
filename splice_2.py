def extract_moments(act_name):
	act_file = open(act_name, "r")
	header = act_file.readline()
	header = header.strip()

	header = header.split(", ")

	M = len(header)

	#print(header)

	# We know the 0th string is the empty string, so let's move on
	'''
	for i in range(1, M):
		if header[i][0] == " ":
			header[i] = header[i][1:]
	'''

	wanted = ["influence_mean", "redundancy_mean", "avgdeathage_mean", "influence_std", "redundancy_std", "avgdeathage_std"]
	indices = []

	for i in range(len(header)):
		if header[i] in wanted:
			indices.append(i)

	out = []
	for line in act_file:
		line = line.strip()
		line = line.split(", ")
		out.append( [line[i] for i in indices] )

	act_file.close()

	return out


def repack_moments(prefix, num_files):
	N = -1
	count_file = open(prefix + "0.csv")
	for line in count_file:
		N += 1

	out = [[] for _ in range(N)]

	data = []
	for i in range(num_files):
		data.append( extract_moments(prefix + str(i) +".csv") )

	for j in range(N):
		for p in range(6):
			for L in range(5):
				out[j].append(data[L][j][p])

	return out

def write_data(struct_name, prefix, num_files, out_name):
	lines = []

	

	struct_file = open(struct_name, "r")

	header = struct_file.readline()
	header = header.strip()
	header = header.split(", ")
	header = header[1:]

	N = 0
	for line in struct_file:
		line = line.strip()
		line = line.split(", ")
		lines.append(line)
		N +=1



	struct_file.close()

	header += ["influence_mean_0","influence_mean_1","influence_mean_2","influence_mean_3","influence_mean_4",
               "influence_std_0","influence_std_1","influence_std_2","influence_std_3","influence_std_4",
	           "redundancy_mean_0","redundancy_mean_1","redundancy_mean_2","redundancy_mean_3","redundancy_mean_4",
	           "redundancy_std_0","redundancy_std_1","redundancy_std_2","redundancy_std_3","redundancy_std_4",
               "avgdeathage_mean_0","avgdeathage_mean_1","avgdeathage_mean_2","avgdeathage_mean_3","avgdeathage_mean_4",
               "avgdeathage_std_0","avgdeathage_std_1","avgdeathage_std_2","avgdeathage_std_3","avgdeathage_std_4",]

	activity_data = repack_moments(prefix, num_files)

	out_file = open(out_name, "w")


	st = "Node, "
	for word in header:
		st += word + ", "
	out_file.write(st[:-2] + "\n")


	for i in range(N):
		st = ""
		for word in lines[i]:
			st += str(word) + ", "
		for val in activity_data[i]:
			st += str(val) + ", "
		out_file.write(st[:-2] + "\n")

	out_file.close()








def main():
	
	'''
	write_data("dir_cocomac_struct_stats.csv", "repeat_cocomac_IS/cocomac_act_stats_IS_", 5, "better_correlation_data/cocomac_for_corr_IS.csv")
	write_data("dir_cocomac_struct_stats.csv", "repeat_cocomac_RW/cocomac_act_stats_RW_", 5, "better_correlation_data/cocomac_for_corr_RW.csv")
	write_data("dir_monkey91_struct_stats.csv", "repeat_monkey91_IS/monkey91_act_stats_IS_", 5, "better_correlation_data/monkey91_for_corr_IS.csv")
	write_data("dir_monkey91_struct_stats.csv", "repeat_monkey91_RW/monkey91_act_stats_RW_", 5, "better_correlation_data/monkey91_for_corr_RW.csv")
	write_data("dir_threshmouse_struct_stats.csv", "repeat_threshmouse_IS/threshmouse_act_stats_IS_", 5, "better_correlation_data/threshmouse_for_corr_IS.csv")
	write_data("dir_threshmouse_struct_stats.csv", "repeat_threshmouse_RW/threshmouse_act_stats_RW_", 5, "better_correlation_data/threshmouse_for_corr_RW.csv")
	'''

	# write_data(struct_name, prefix, num_files, out_name)

	# ER 0
	write_data("thresh_er_0_anly/thresh_mouse_er_0_struct.csv",
		       "thresh_er_0_anly/thresh_er_0_IS/mouse_er_0_act_stats_IS_", 5,
		       "thresh_er_0_anly/mouse_er_0_IS_stact_stats.csv")
	write_data("thresh_er_0_anly/thresh_mouse_er_0_struct.csv",
		       "thresh_er_0_anly/thresh_er_0_RW/mouse_er_0_act_stats_RW_", 5,
		       "thresh_er_0_anly/mouse_er_0_RW_stact_stats.csv")

	# ER 1
	write_data("thresh_er_1_anly/thresh_mouse_er_1_struct.csv",
		       "thresh_er_1_anly/thresh_er_1_IS/mouse_er_1_act_stats_IS_", 5,
		       "thresh_er_1_anly/mouse_er_1_IS_stact_stats.csv")
	write_data("thresh_er_1_anly/thresh_mouse_er_1_struct.csv",
		       "thresh_er_1_anly/thresh_er_1_RW/mouse_er_1_act_stats_RW_", 5,
		       "thresh_er_1_anly/mouse_er_1_RW_stact_stats.csv")

	# MS 0
	write_data("thresh_ms_0_anly/thresh_mouse_ms_0_struct.csv",
		       "thresh_ms_0_anly/thresh_ms_0_IS/mouse_ms_0_act_stats_IS_", 5,
		       "thresh_ms_0_anly/mouse_ms_0_IS_stact_stats.csv")
	write_data("thresh_ms_0_anly/thresh_mouse_ms_0_struct.csv",
		       "thresh_ms_0_anly/thresh_ms_0_RW/mouse_ms_0_act_stats_RW_", 5,
		       "thresh_ms_0_anly/mouse_ms_0_RW_stact_stats.csv")

	# MS 1
	write_data("thresh_ms_1_anly/thresh_mouse_ms_1_struct.csv",
		       "thresh_ms_1_anly/thresh_ms_1_IS/mouse_ms_1_act_stats_IS_", 5,
		       "thresh_ms_1_anly/mouse_ms_1_IS_stact_stats.csv")
	write_data("thresh_ms_1_anly/thresh_mouse_ms_1_struct.csv",
		       "thresh_ms_1_anly/thresh_ms_1_RW/mouse_ms_1_act_stats_RW_", 5,
		       "thresh_ms_1_anly/mouse_ms_1_RW_stact_stats.csv")

	# SF 0
	write_data("thresh_sf_0_anly/thresh_mouse_sf_0_struct.csv",
		       "thresh_sf_0_anly/thresh_sf_0_IS/mouse_sf_0_act_stats_IS_", 5,
		       "thresh_sf_0_anly/mouse_sf_0_IS_stact_stats.csv")
	write_data("thresh_sf_0_anly/thresh_mouse_sf_0_struct.csv",
		       "thresh_sf_0_anly/thresh_sf_0_RW/mouse_sf_0_act_stats_RW_", 5,
		       "thresh_sf_0_anly/mouse_sf_0_RW_stact_stats.csv")

	# SF 1
	write_data("thresh_sf_1_anly/thresh_mouse_sf_1_struct.csv",
		       "thresh_sf_1_anly/thresh_sf_1_IS/mouse_sf_1_act_stats_IS_", 5,
		       "thresh_sf_1_anly/mouse_sf_1_IS_stact_stats.csv")
	write_data("thresh_sf_1_anly/thresh_mouse_sf_1_struct.csv",
		       "thresh_sf_1_anly/thresh_sf_1_RW/mouse_sf_1_act_stats_RW_", 5,
		       "thresh_sf_1_anly/mouse_sf_1_RW_stact_stats.csv")

main()