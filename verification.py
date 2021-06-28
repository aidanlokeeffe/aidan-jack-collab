from Package import Package
from Container import Container
from Experiment import Experiment 
import random

def main():
	#a = Experiment(fileName, load, T, choice=0):

	monkey_experiment_rw = Experiment("monkey91.csv", 9, 1000, 0)
	monkey_experiment_is = Experiment("monkey91.csv", 9, 1000, 1)
	mouse_experiment_rw = Experiment("mouseunweighted.csv", 22, 1000, 0)
	mouse_experiment_is = Experiment("mouseunweighted.csv", 22, 1000, 1)


	monkey_experiment_rw.execute()
	monkey_experiment_is.execute()
	mouse_experiment_rw.execute()
	mouse_experiment_is.execute()

	monkey_experiment_rw.write_verif_output_1("monkey_rw_verif_1.csv")
	monkey_experiment_is.write_verif_output_1("monkey_is_verif_1.csv")
	mouse_experiment_rw.write_verif_output_1("mouse_rw_verif_1.csv")
	mouse_experiment_is.write_verif_output_1("mouse_is_verif_1.csv")


	monkey_experiment_rw.write_verif_output_2("monkey_rw_verif_2.csv")
	monkey_experiment_is.write_verif_output_2("monkey_is_verif_2.csv")
	mouse_experiment_rw.write_verif_output_2("mouse_rw_verif_2.csv")
	mouse_experiment_is.write_verif_output_2("mouse_is_verif_2.csv")

main()



