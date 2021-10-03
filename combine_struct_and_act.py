import os
import sys
import shutil


def merge_files(struct, act, out_name):
	lines = []
	struct_file = open(struct, "r")
	for line in struct_file:
		line = line.strip()
		lines.append(line + ", ")

	struct_file.close()

	act_file = open(act, "r")

	M = len(lines)

	for i in range(M):
		line = act_file.readline()
		line = line.strip()
		line = line.split(",")
		to_concat = ""
		for st in line[1:]:
			to_concat += st + ","
		lines[i] += to_concat[:-1] + "\n"

	act_file.close()

	out_file = open(out_name, "w")
	for line in lines:
		out_file.write(line)
	out_file.close()

def main():
	directories = ["cocomac_act_stats_IS", "monkey91_act_stats_IS", "mouse_act_stats_IS", 
	"cocomac_act_stats_RW", "monkey91_act_stats_RW", "mouse_act_stats_RW"]
	bases = ["dir_cocomac_act_stats_IS_", "dir_monkey91_act_stats_IS_", "dir_mouse_act_stats_IS_",
	"dir_cocomac_act_stats_RW_", "dir_monkey91_act_stats_RW_", "dir_mouse_act_stats_RW_"]
	structs = ["dir_cocomac_struct_stats.csv", "dir_monkey91_struct_stats.csv", "dir_mouse_struct_stats.csv"]

	out_dirs = ["cocomac_IS_stact", "monkey91_IS_stact", "mouse_IS_stact",
	"cocomac_RW_stact", "monkey91_RW_stact", "mouse_RW_stact",]

	out_name_bases = [""]

	# Use mod 3 to make it easier
	for i in range(6):
		# figure out what folder we need to go into
		directory = directories[i]

		# figure out which structure file to splice
		struct_file = structs[i%3]

		out_dir = out_dirs[i]

		# make the directory to store the things 
		try:
			os.mkdir(out_dir)
		except FileExistsError:
			shutil.rmtree(out_dir)
			os.mkdir(out_dir)


		for j in range(5):
			# get the name of the next activity file to splice
			act_file = directory + "/" + bases[i] + str(j) + ".csv"

			# get the out_name
			out_name = out_dirs[i] + "/" + out_dirs[i] + "_stats_" + str(j) + ".csv"

			# perform the merge
			merge_files(struct_file, act_file, out_name)



main()