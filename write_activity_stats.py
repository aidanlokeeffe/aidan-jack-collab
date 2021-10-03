from Experiment import Experiment

def main():
	mouse_exp = Experiment("mouseunweighted.csv", 1, 1000, 0)
	monkey91_exp = Experiment("monkey91.csv", 1, 1000, 0)
	cocomac_exp = Experiment("cocoadj.csv", 1, 1000, 0)

	mouse_exp.execute()
	monkey91_exp.execute()
	cocomac_exp.execute()

	mouse_exp.write_activity_1_csv("dir_mouse_act_stats.csv")
	monkey91_exp.write_activity_1_csv("dir_monkey91_act_stats.csv")
	cocomac_exp.write_activity_1_csv("dir_cocomac_act_stats.csv")

main()