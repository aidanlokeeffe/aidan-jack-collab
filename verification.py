from Package import Package
from Container import Container
from Experiment import Experiment 
import random
import numpy as np
import math
from matplotlib import pyplot as plt

def makeUndirected(matrix):
    if math.isnan(matrix[0][0]):
        matrix = matrix[1:,1:]
    N= len(matrix)
    for i in range(N):
        for _ in range(N):
            if matrix[i][_]==1:
                matrix[_][i]=1
########################################################
#matrix=np.genfromtxt('mouseunweighted.csv', delimiter=',')

#makeUndirected(matrix)

#np.savetxt("undirmouse.csv", matrix, delimiter=",")
########################################################
#matrix=np.genfromtxt('monkey91.csv', delimiter=',')

#makeUndirected(matrix)

#np.savetxt("undirmonkey91.csv", matrix, delimiter=",")
########################################################
#matrix=np.genfromtxt('cocoadj.csv', delimiter=',')

#makeUndirected(matrix)

#np.savetxt("undircoco.csv", matrix, delimiter=",")




def main():
	#a = Experiment(fileName, load, T, choice=0):

	monkey_experiment_rw = Experiment("monkey91.csv", 1, 1000, 0)
	monkey_experiment_rw.execute()
	monkey_experiment_rw.write_verif_output_1("monkey_rw_verif_1.csv")
	ages = np.genfromtxt("monkey_rw_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("Monkey RW " + str(avg))
	monkeyRwAges = (ages, avg)

	monkey_experiment_is = Experiment("monkey91.csv", 1, 1000, 1)
	monkey_experiment_is.execute()
	monkey_experiment_is.write_verif_output_1("monkey_is_verif_1.csv")
	ages = np.genfromtxt("monkey_is_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("Monkey IS "+str(avg))
	monkeyIsAges = (ages, avg)


	monkey_undir_rw = Experiment("undirmonkey91.csv", 1, 1000, 0)
	monkey_undir_rw.execute()
	monkey_undir_rw.write_verif_output_1("monkey_rw_undir_verif_1.csv")
	ages = np.genfromtxt("monkey_rw_undir_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("UNDIR MONKEY RW "+ str(avg))
	undirMonkeyRwAges = (ages, avg)


	monkey_undir_is = Experiment("undirmonkey91.csv", 1, 1000, 1)
	monkey_undir_is.execute()
	monkey_undir_is.write_verif_output_1("monkey_is_undir_verif_1.csv")
	ages = np.genfromtxt("monkey_is_undir_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("UNDIR MONKEY IS " + str(avg))
	undirMonkeyIsAges = (ages, avg)


	coco_experiment_rw = Experiment("cocoadj.csv", 36, 1000, 0)
	coco_experiment_rw.execute()
	coco_experiment_rw.write_verif_output_1("coco_rw_verif_1.csv")
	ages = np.genfromtxt("coco_rw_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("coco RW " + str(avg))
	cocoRwAges = (ages, avg)


	coco_experiment_is = Experiment("cocoadj.csv", 36, 1000, 1)
	coco_experiment_is.execute()
	coco_experiment_is.write_verif_output_1("coco_is_verif_1.csv")
	ages = np.genfromtxt("coco_is_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("coco IS " + str(avg))
	cocoIsAges = (ages, avg)

	coco_undir_rw = Experiment("undircoco.csv", 36, 1000, 0)
	coco_undir_rw.execute()
	coco_undir_rw.write_verif_output_1("coco_rw_undir_verif_1.csv")
	ages = np.genfromtxt("coco_rw_undir_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("UNDIR coco RW "+ str(avg))
	undirCocoRwAges = (ages, avg)


	coco_undir_is = Experiment("undircoco.csv", 36, 1000, 1)
	coco_undir_is.execute()
	coco_undir_is.write_verif_output_1("coco_is_undir_verif_1.csv")
	ages = np.genfromtxt("coco_is_undir_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("UNDIR coco IS " + str(avg))
	UndirCocoIsAges = (ages, avg)


	mouse_experiment_rw = Experiment("mouseunweighted.csv", 42, 1000, 0)
	mouse_experiment_rw.execute()
	mouse_experiment_rw.write_verif_output_1("mouse_rw_verif_1.csv")
	ages = np.genfromtxt("mouse_rw_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("Mouse RW " + str(avg))
	mouseRwAges = (ages, avg)


	mouse_experiment_is = Experiment("mouseunweighted.csv", 42, 1000, 1)
	mouse_experiment_is.execute()
	mouse_experiment_is.write_verif_output_1("mouse_is_verif_1.csv")
	ages = np.genfromtxt("mouse_is_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("Mouse IS " + str(avg))
	mouseIsAges = (ages, avg)

	mouse_undir_rw = Experiment("undirmouse.csv", 42, 1000, 0)
	mouse_undir_rw.execute()
	mouse_undir_rw.write_verif_output_1("mouse_rw_undir_verif_1.csv")
	ages = np.genfromtxt("mouse_rw_undir_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("UNDIR mouse RW "+ str(avg))
	undirMouseRwAges = (ages, avg)


	mouse_undir_is = Experiment("undirmouse.csv", 42, 1000, 1)
	mouse_undir_is.execute()
	mouse_undir_is.write_verif_output_1("mouse_is_undir_verif_1.csv")
	ages = np.genfromtxt("mouse_is_undir_verif_1.csv", delimiter=',')
	ages = ages[1:,0:3]
	count = 0
	summy = 0
	for a in ages:
		if a[0]>=100:
			count+=1
			summy += a[2]
	avg = summy/count
	print("UNDIR mouse IS " + str(avg))	
	undirMouseIsAges = (ages, avg)

	#monkey_experiment_rw.write_verif_output_2("monkey_rw_verif_2.csv")
	#monkey_experiment_is.write_verif_output_2("monkey_is_verif_2.csv")
	#mouse_experiment_rw.write_verif_output_2("mouse_rw_verif_2.csv")
	#mouse_experiment_is.write_verif_output_2("mouse_is_verif_2.csv")

	bins = [x for x in range(50)]

	plt.clf()
	plt.hist(monkeyRwAges[0][:,2], bins=bins)
	plt.suptitle("Monkey RW Ages")
	plt.title("Load = 1, Average Age: " + str(monkeyRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(monkeyRwAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()

	plt.hist(monkeyIsAges[0][:,2], bins=bins)
	plt.suptitle("Monkey IS Ages")
	plt.title("Load = 1, Average Age: " + str(monkeyIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(monkeyIsAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()

	plt.hist(undirMonkeyRwAges[0][:,2], bins=bins)
	plt.suptitle("Bidirectional Monkey RW Ages")
	plt.title("Load = 1, Average Age: " + str(undirMonkeyRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(undirMonkeyRwAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()

	plt.hist(undirMonkeyIsAges[0][:,2], bins=bins)
	plt.suptitle("Bidirectional Monkey IS Ages")
	plt.title("Load = 1, Average Age: " + str(undirMonkeyIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(undirMonkeyIsAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()

	plt.hist(cocoRwAges[0][:,2], bins=bins)
	plt.suptitle("CoCoMac RW Ages")
	plt.title("Load = 1, Average Age: " + str(cocoRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(cocoRwAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()

	plt.hist(cocoIsAges[0][:,2], bins=bins)
	plt.suptitle("CoCoMac IS Ages")
	plt.title("Load = 1, Average Age: " + str(cocoIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(cocoIsAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()

	plt.hist(undirCocoRwAges[0][:,2], bins=bins)
	plt.suptitle("Bidirectional CoCoMac RW Ages")
	plt.title("Load = 1, Average Age: " + str(undirCocoRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(undirCocoRwAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()

	plt.hist(UndirCocoIsAges[0][:,2], bins=bins)
	plt.suptitle("Bidirectional CoCoMac IS Ages")
	plt.title("Load = 1, Average Age: " + str(UndirCocoIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(UndirCocoIsAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()

	plt.hist(mouseRwAges[0][:,2], bins=bins)
	plt.suptitle("Mouse RW Ages")
	plt.title("Load = 1, Average Age: " + str(mouseRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(mouseRwAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()

	plt.hist(mouseIsAges[0][:,2], bins=bins)
	plt.suptitle("Mouse IS Ages")
	plt.title("Load = 1, Average Age: " + str(mouseIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(mouseIsAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()

	plt.hist(undirMouseRwAges[0][:,2], bins=bins)
	plt.suptitle("Bidirectional Mouse RW Ages")
	plt.title("Load = 1, Average Age: " + str(undirMouseRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(undirMouseRwAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()

	plt.hist(undirMouseIsAges[0][:,2], bins=bins)
	plt.suptitle("Bidirectional Mouse IS Ages")
	plt.title("Load = 1, Average Age: " + str(undirMouseIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(undirMouseIsAges[0][:,2] == 1)), size='small')
	plt.show()
	plt.clf()




main()