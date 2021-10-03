from Experiment import Experiment

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
	merge_files("dir_cocomac_struct_stats.csv", "dir_cocomac_act_stats.csv", "dir_cocomac_struct_act_stats.csv")
	merge_files("dir_monkey91_struct_stats.csv", "dir_monkey91_act_stats.csv", "dir_monkey91_struct_act_stats.csv")
	merge_files("dir_mouse_struct_stats.csv", "dir_mouse_act_stats.csv", "dir_mouse_struct_act_stats.csv")



main()