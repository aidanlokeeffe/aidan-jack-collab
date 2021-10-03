from Experiment import Experiment

def main():
	mouse_exp = Experiment("mouseunweighted.csv", 1, 1000, 0)
	monkey91_exp = Experiment("monkey91.csv", 1, 1000, 0)
	cocomac_exp = Experiment("cocoadj.csv", 1, 1000, 0)

	mouse_exp.write_structure_1_csv("dir_mouse_struct_stats.csv")
	monkey91_exp.write_structure_1_csv("dir_monkey91_struct_stats.csv")
	cocomac_exp.write_structure_1_csv("dir_cocomac_struct_stats.csv")

main()