from Experiment import Experiment
import math

'''
RETHINK, WE NEED TO COMPUTE THE CENTRALITY FOR EACH NETWORK EXACTLY ONE TIME, JUST ONE TIME,
AND THEN WE CAN COMPUTE THE ACTIVITY, AND IT WILL BE MUCH FASTER TO RUN THIS STUFF. THE LAST
ATTEMPT WAS PRETTY SAD. POOT
'''


def main():
	ms_size = 213
	mk_size = 91
	cm_size = 184

	# FOR RANDOM WALK
	mouse_exp = Experiment("mouseunweighted.csv", 1, 1000, 0)
	monkey91_exp = Experiment("monkey91.csv", 1, 1000, 0)
	cocomac_exp = Experiment("undircoco.csv", 1, 1000, 0)

	mouse_exp.execute()
	monkey91_exp.execute()
	cocomac_exp.execute()

	mouse_exp.write_structure_activity_1_csv("mouse_st_act_RW_1.csv")
	monkey91_exp.write_structure_activity_1_csv("monkey91_st_act_RW_1.csv")
	cocomac_exp.write_structure_activity_1_csv("cocomac_st_act_RW_1.csv")

	
	load_proportions = [0.0125, 0.025, 0.05, 0.1, 0.2, 0.4]
	for k in range(2, 8):
		t = load_proportions[k-2]
		mouse_exp = Experiment("mouseunweighted.csv", math.floor(t*ms_size), 1000, 1)
		monkey91_exp = Experiment("monkey91.csv", math.floor(t*mk_size), 1000, 1)
		cocomac_exp = Experiment("undircoco.csv", math.floor(t*cm_size), 1000, 1)

		mouse_exp.execute()
		monkey91_exp.execute()
		cocomac_exp.execute()

		mouse_exp.write_structure_activity_1_csv("mouse_st_act_RW_" + str(k) + ".csv")
		monkey91_exp.write_structure_activity_1_csv("monkey91_st_act_RW_" + str(k) + ".csv" )
		cocomac_exp.write_structure_activity_1_csv("cocomac_st_act_RW_" + str(k) + ".csv")


	# FOR INFORMATION SPREADING
	mouse_exp = Experiment("mouseunweighted.csv", 1, 1000, 1)
	monkey91_exp = Experiment("monkey91.csv", 1, 1000, 1)
	cocomac_exp = Experiment("undircoco.csv", 1, 1000, 1)

	mouse_exp.execute()
	monkey91_exp.execute()
	cocomac_exp.execute()

	mouse_exp.write_structure_activity_1_csv("mouse_st_act_IS_1.csv")
	monkey91_exp.write_structure_activity_1_csv("monkey91_st_act_IS_1.csv")
	cocomac_exp.write_structure_activity_1_csv("cocomac_st_act_IS_1.csv")

	load_proportions = [0.0125, 0.025, 0.05, 0.1, 0.2, 0.4]

	for k in range(2, 8):
		t = load_proportions[k-2]
		mouse_exp = Experiment("mouseunweighted.csv", math.floor(t*ms_size), 1000, 1)
		monkey91_exp = Experiment("monkey91.csv", math.floor(t*mk_size), 1000, 1)
		cocomac_exp = Experiment("undircoco.csv", math.floor(t*cm_size), 1000, 1)

		mouse_exp.execute()
		monkey91_exp.execute()
		cocomac_exp.execute()

		mouse_exp.write_structure_activity_1_csv("mouse_st_act_IS_" + str(k) + ".csv")
		monkey91_exp.write_structure_activity_1_csv("monkey91_st_act_IS_" + str(k) + ".csv" )
		cocomac_exp.write_structure_activity_1_csv("cocomac_st_act_IS_" + str(k) + ".csv")








main()