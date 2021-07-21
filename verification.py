from Package import Package
from Container import Container
from Experiment import Experiment 
import random
import numpy as np
import math
from matplotlib import pyplot as plt

#This function can be used to easily create a bidirectional version of a directed network
def makeUndirected(matrix): 
    if math.isnan(matrix[0][0]):
        matrix = matrix[1:,1:]
    N= len(matrix)
    for i in range(N):
        for _ in range(N):
            if matrix[i][_]==1:
                matrix[_][i]=1

########################################################
#matrix=np.genfromtxt('threshmouse.csv', delimiter=',')

#makeUndirected(matrix)

#np.savetxt("undirmousethresh.csv", matrix, delimiter=",")
#########################################################
#matrix=np.genfromtxt('monkey91.csv', delimiter=',')

#makeUndirected(matrix)

#np.savetxt("undirmonkey91.csv", matrix, delimiter=",")
########################################################
#matrix=np.genfromtxt('cocoadj.csv', delimiter=',')

#makeUndirected(matrix)

#np.savetxt("undircoco.csv", matrix, delimiter=",")




def main(load, monkey=True, coco=True, mouse=True, og = True, bidir = True, barcharts=True, traffic=True):
#load determines the proportion of activated nodes per timestep
#monkey, coco, and mouse just determine if we run the experiment on those networks
#og is if we run it on the original versions
#bidir is if we run it on the bidirectional versions
#barcharts is if we want to show the histograms of message age at termination
#traffic is if we want to analyze the traffic on each edge

#first, determine the load for each experiment (this is based off of our connectomes, could be automated)
	if load == 1:
		monkeyload = 1
		cocoload = 1
		mouseload = 1
	else:
		monkeyload = math.floor(load * 91)
		cocoload = math.floor(load * 184)
		mouseload = math.floor(load * 213)

#Here, we just create and run the experiments for whatever is activated (set to True)
	if monkey:
		if og:
			monkey_experiment_rw = Experiment("monkey91.csv", monkeyload, 3000, 0)
			monkey_experiment_rw.execute()
			monkey_experiment_rw.write_verif_output_1("monkey_rw_verif_1.csv")
			ages = np.genfromtxt("monkey_rw_verif_1.csv", delimiter=',')
			#ages tells us the age of each message when it had died
			ages = ages[1:,0:3]
			count = 0
			summy = 0
			for a in ages:
				#get rid of transitional period
				if a[0]>=100:
					count+=1
					summy += a[2]
			#find average age of these messages, save it
			avg = summy/count
			print("Monkey RW " + str(avg))
			monkeyRwAges = (ages, avg)

			monkey_experiment_is = Experiment("monkey91.csv", monkeyload, 3000, 1)
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

		if bidir:
			monkey_undir_rw = Experiment("undirmonkey91.csv", monkeyload, 3000, 0)
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


			monkey_undir_is = Experiment("undirmonkey91.csv", monkeyload, 3000, 1)
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

	if coco:
		if og:
			coco_experiment_rw = Experiment("cocoadj.csv", cocoload, 3000, 0)
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


			coco_experiment_is = Experiment("cocoadj.csv", cocoload, 3000, 1)
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
		if bidir:
			coco_undir_rw = Experiment("undircoco.csv", cocoload, 3000, 0)
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


			coco_undir_is = Experiment("undircoco.csv", cocoload, 3000, 1)
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

	if mouse:
		if og:
			mouse_experiment_rw = Experiment("threshmouse.csv", mouseload, 3000, 0)
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


			mouse_experiment_is = Experiment("threshmouse.csv", mouseload, 3000, 1)
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

		if bidir:
			mouse_undir_rw = Experiment("undirmousethresh.csv", mouseload, 3000, 0)
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


			mouse_undir_is = Experiment("undirmousethresh.csv", mouseload, 3000, 1)
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

	if barcharts:
		if monkey:
			if og:
				#clear any figure (good practice)
				plt.clf()
				#set the x axis to end at the maximum age
				maxy = max(monkeyRwAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				#plot the message ages
				plt.hist(monkeyRwAges[0][:,2], bins=bins)
				#make it pretty
				plt.suptitle("Monkey RW Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(monkeyRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(monkeyRwAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				#show the figure
				plt.show()
				#clear it for the next one!
				plt.clf()
				#when you click X, it will go to the next figure.
				#you must X out of all figures to continue the program.

				maxy = max(monkeyIsAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				plt.hist(monkeyIsAges[0][:,2], bins=bins)
				plt.suptitle("Monkey IS Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(monkeyIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(monkeyIsAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				plt.show()
				plt.clf()

			if bidir:
				maxy = max(undirMonkeyRwAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				plt.hist(undirMonkeyRwAges[0][:,2], bins=bins)
				plt.suptitle("Bidirectional Monkey RW Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(undirMonkeyRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(undirMonkeyRwAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				plt.show()
				plt.clf()

				maxy = max(undirMonkeyIsAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				plt.hist(undirMonkeyIsAges[0][:,2], bins=bins)
				plt.suptitle("Bidirectional Monkey IS Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(undirMonkeyIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(undirMonkeyIsAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				plt.show()
				plt.clf()

		if coco:
			if og:
				maxy = max(cocoRwAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				plt.hist(cocoRwAges[0][:,2], bins=bins)
				plt.suptitle("CoCoMac RW Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(cocoRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(cocoRwAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				plt.show()
				plt.clf()

				maxy = max(cocoIsAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				plt.hist(cocoIsAges[0][:,2], bins=bins)
				plt.suptitle("CoCoMac IS Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(cocoIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(cocoIsAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				plt.show()
				plt.clf()

			if bidir:
				maxy = max(undirCocoRwAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				plt.hist(undirCocoRwAges[0][:,2], bins=bins)
				plt.suptitle("Bidirectional CoCoMac RW Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(undirCocoRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(undirCocoRwAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				plt.show()
				plt.clf()

				maxy = max(UndirCocoIsAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				plt.hist(UndirCocoIsAges[0][:,2], bins=bins)
				plt.suptitle("Bidirectional CoCoMac IS Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(UndirCocoIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(UndirCocoIsAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				plt.show()
				plt.clf()

		if mouse:
			if og:
				maxy = max(mouseRwAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				plt.hist(mouseRwAges[0][:,2], bins=bins)
				plt.suptitle("Mouse RW Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(mouseRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(mouseRwAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				plt.show()
				plt.clf()

				maxy = max(mouseIsAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				plt.hist(mouseIsAges[0][:,2], bins=bins)
				plt.suptitle("Mouse IS Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(mouseIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(mouseIsAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				plt.show()
				plt.clf()

			if bidir:
				maxy = max(undirMouseRwAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				plt.hist(undirMouseRwAges[0][:,2], bins=bins)
				plt.suptitle("Bidirectional Mouse RW Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(undirMouseRwAges[1]) + " , Failed Injections: " + str(np.count_nonzero(undirMouseRwAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				plt.show()
				plt.clf()

				maxy = max(undirMouseIsAges[0][:,2])
				maxy = int(maxy)
				bins = [x for x in range(maxy)]
				plt.hist(undirMouseIsAges[0][:,2], bins=bins)
				plt.suptitle("Bidirectional Mouse IS Ages: Histogram of Message Age at Termination")
				plt.title("Load: " + str(load) + ", Average Age: " + str(undirMouseIsAges[1]) + " , Failed Injections: " + str(np.count_nonzero(undirMouseIsAges[0][:,2] == 1)), size='small')
				plt.xlabel('Message Age at Termination')
				plt.ylabel('No. of Messages')
				plt.show()
				plt.clf()


	if traffic:	
		if monkey:
			if og:
				edgesTraffic = [[[] for _ in range(91)] for _ in range(91)]
				histories = []
				for tally in monkey_experiment_rw.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*91 for _ in range(91)]
				edgeUses = [[0]*91 for _ in range(91)]
				for i in range(91):
					for j in range(91):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				np.savetxt("monkeyRWTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("monkeyRWEdgeAge.csv", edgeAvgAge, delimiter=',')

				edgesTraffic = [[[] for _ in range(91)] for _ in range(91)]
				histories = []
				for tally in monkey_experiment_is.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*91 for _ in range(91)]
				edgeUses = [[0]*91 for _ in range(91)]
				for i in range(91):
					for j in range(91):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				np.savetxt("monkeyISTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("monkeyISEdgeAge.csv", edgeAvgAge, delimiter=',')

			if bidir:
				edgesTraffic = [[[] for _ in range(91)] for _ in range(91)]
				histories = []
				for tally in monkey_undir_rw.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*91 for _ in range(91)]
				edgeUses = [[0]*91 for _ in range(91)]
				for i in range(91):
					for j in range(91):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				ratesMatrix = [[0]*91 for _ in range(91)]
				for i in range(91):
					for j in range(91):
						divisor = edgeUses[i][j]+edgeUses[j][i]
						if divisor != 0:
							ratesMatrix[i][j]=edgeUses[i][j]/divisor
				monkeymap = np.genfromtxt('monkey91.csv', dtype=int, delimiter=',')
				for i in range(91):
					for j in range(91):
						if monkeymap[i][j] == 0:
							ratesMatrix[i][j] = -1 * ratesMatrix[i][j]
				origHighTraffic = 0
				newHighTraffic = 0
				for i in range(91):
					for j in range(91):
						if ratesMatrix[i][j] > .85:
							origHighTraffic += 1
						elif ratesMatrix[i][j] < -.85:
							newHighTraffic += 1
				print("monkey RW High traffic original links: " + str(origHighTraffic) + ", High traffic new links: " + str(newHighTraffic))
				np.savetxt('undirmonkeyRWTrafficRates.csv', ratesMatrix, delimiter=',')
				np.savetxt("undirmonkeyRWTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("undirmonkeyRWEdgeAge.csv", edgeAvgAge, delimiter=',')

				edgesTraffic = [[[] for _ in range(91)] for _ in range(91)]
				histories = []
				for tally in monkey_undir_is.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*91 for _ in range(91)]
				edgeUses = [[0]*91 for _ in range(91)]
				for i in range(91):
					for j in range(91):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				ratesMatrix = [[0]*91 for _ in range(91)]
				for i in range(91):
					for j in range(91):
						divisor = edgeUses[i][j]+edgeUses[j][i]
						if divisor != 0:
							ratesMatrix[i][j]=edgeUses[i][j]/divisor
				for i in range(91):
					for j in range(91):
						if monkeymap[i][j] == 0:
							ratesMatrix[i][j] = -1 * ratesMatrix[i][j]
				origHighTraffic = 0
				newHighTraffic = 0
				for i in range(91):
					for j in range(91):
						if ratesMatrix[i][j] > .85:
							origHighTraffic += 1
						elif ratesMatrix[i][j] < -.85:
							newHighTraffic += 1
				print("monkey IS High traffic original links: " + str(origHighTraffic) + ", High traffic new links: " + str(newHighTraffic))
				np.savetxt('undirmonkeyISTrafficRates.csv', ratesMatrix, delimiter=',')
				np.savetxt("undirmonkeyISTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("undirmonkeyISEdgeAge.csv", edgeAvgAge, delimiter=',')






		if coco:
			if og:
				edgesTraffic = [[[] for _ in range(184)] for _ in range(184)]
				histories = []
				for tally in coco_experiment_rw.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*184 for _ in range(184)]
				edgeUses = [[0]*184 for _ in range(184)]
				for i in range(184):
					for j in range(184):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				np.savetxt("cocoRWTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("cocoRWEdgeAge.csv", edgeAvgAge, delimiter=',')

				edgesTraffic = [[[] for _ in range(184)] for _ in range(184)]
				histories = []
				for tally in coco_experiment_is.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*184 for _ in range(184)]
				edgeUses = [[0]*184 for _ in range(184)]
				for i in range(184):
					for j in range(184):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				np.savetxt("cocoISTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("cocoISEdgeAge.csv", edgeAvgAge, delimiter=',')

			if bidir:
				edgesTraffic = [[[] for _ in range(184)] for _ in range(184)]
				histories = []
				for tally in coco_undir_rw.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*184 for _ in range(184)]
				edgeUses = [[0]*184 for _ in range(184)]
				for i in range(184):
					for j in range(184):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				ratesMatrix = [[0]*184 for _ in range(184)]
				for i in range(184):
					for j in range(184):
						divisor = edgeUses[i][j]+edgeUses[j][i]
						if divisor != 0:
							ratesMatrix[i][j]=edgeUses[i][j]/divisor
				cocomap = np.genfromtxt('cocoadj.csv', dtype=int, delimiter=',')
				for i in range(184):
					for j in range(184):
						if cocomap[i][j] == 0:
							ratesMatrix[i][j] = -1 * ratesMatrix[i][j]
				origHighTraffic = 0
				newHighTraffic = 0
				for i in range(184):
					for j in range(184):
						if ratesMatrix[i][j] > .85:
							origHighTraffic += 1
						elif ratesMatrix[i][j] < -.85:
							newHighTraffic += 1
				print("coco RW High traffic original links: " + str(origHighTraffic) + ", High traffic new links: " + str(newHighTraffic))
				np.savetxt('undircocoRWTrafficRates.csv', ratesMatrix, delimiter=',')
				np.savetxt("undircocoRWTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("undircocoRWEdgeAge.csv", edgeAvgAge, delimiter=',')

				edgesTraffic = [[[] for _ in range(184)] for _ in range(184)]
				histories = []
				for tally in coco_undir_is.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*184 for _ in range(184)]
				edgeUses = [[0]*184 for _ in range(184)]
				for i in range(184):
					for j in range(184):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				ratesMatrix = [[0]*184 for _ in range(184)]
				for i in range(184):
					for j in range(184):
						divisor = edgeUses[i][j]+edgeUses[j][i]
						if divisor != 0:
							ratesMatrix[i][j]=edgeUses[i][j]/divisor
				for i in range(184):
					for j in range(184):
						if cocomap[i][j] == 0:
							ratesMatrix[i][j] = -1 * ratesMatrix[i][j]
				origHighTraffic = 0
				newHighTraffic = 0
				for i in range(184):
					for j in range(184):
						if ratesMatrix[i][j] > .85:
							origHighTraffic += 1
						elif ratesMatrix[i][j] < -.85:
							newHighTraffic += 1
				print("coco IS High traffic original links: " + str(origHighTraffic) + ", High traffic new links: " + str(newHighTraffic))
				np.savetxt('undircocoISTrafficRates.csv', ratesMatrix, delimiter=',')
				np.savetxt("undircocoISTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("undircocoISEdgeAge.csv", edgeAvgAge, delimiter=',')


		if mouse:
			if og:
				edgesTraffic = [[[] for _ in range(213)] for _ in range(213)]
				histories = []
				for tally in mouse_experiment_rw.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*213 for _ in range(213)]
				edgeUses = [[0]*213 for _ in range(213)]
				for i in range(213):
					for j in range(213):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				np.savetxt("mouseRWTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("mouseRWEdgeAge.csv", edgeAvgAge, delimiter=',')

				edgesTraffic = [[[] for _ in range(213)] for _ in range(213)]
				histories = []
				for tally in mouse_experiment_is.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*213 for _ in range(213)]
				edgeUses = [[0]*213 for _ in range(213)]
				for i in range(213):
					for j in range(213):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				np.savetxt("mouseISTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("mouseISEdgeAge.csv", edgeAvgAge, delimiter=',')

			if bidir:
				edgesTraffic = [[[] for _ in range(213)] for _ in range(213)]
				histories = []
				for tally in mouse_undir_rw.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*213 for _ in range(213)]
				edgeUses = [[0]*213 for _ in range(213)]
				for i in range(213):
					for j in range(213):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				ratesMatrix = [[0]*213 for _ in range(213)]
				for i in range(213):
					for j in range(213):
						divisor = edgeUses[i][j]+edgeUses[j][i]
						if divisor != 0:
							ratesMatrix[i][j]=edgeUses[i][j]/divisor
				mousemap = np.genfromtxt('threshmouse.csv', dtype=int, delimiter=',')
				for i in range(213):
					for j in range(213):
						if mousemap[i][j] == 0:
							ratesMatrix[i][j] = -1 * ratesMatrix[i][j]
				origHighTraffic = 0
				newHighTraffic = 0
				for i in range(213):
					for j in range(213):
						if ratesMatrix[i][j] > .85:
							origHighTraffic += 1
						elif ratesMatrix[i][j] < -.85:
							newHighTraffic += 1
				print("mouse RW High traffic original links: " + str(origHighTraffic) + ", High traffic new links: " + str(newHighTraffic))
				np.savetxt('undirmouseRWTrafficRates.csv', ratesMatrix, delimiter=',')
				np.savetxt("undirmouseRWTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("undirmouseRWEdgeAge.csv", edgeAvgAge, delimiter=',')

				edgesTraffic = [[[] for _ in range(213)] for _ in range(213)]
				histories = []
				for tally in mouse_undir_is.deaths:
					for pkg in tally:
						N = len(pkg.vals[0])
						for i in range(N):
							histories.append(pkg.vals[1][i])
				for hist in histories:
					if len(hist)>1:
						for age in range(len(hist)-1):
							edgesTraffic[hist[age]][hist[age+1]].append(age+1)
				edgeAvgAge = [[0]*213 for _ in range(213)]
				edgeUses = [[0]*213 for _ in range(213)]
				for i in range(213):
					for j in range(213):
						edgeAvgAge[i][j] = np.mean(edgesTraffic[i][j])
						edgeUses[i][j] = len(edgesTraffic[i][j])
				ratesMatrix = [[0]*213 for _ in range(213)]
				for i in range(213):
					for j in range(213):
						divisor = edgeUses[i][j]+edgeUses[j][i]
						if divisor != 0:
							ratesMatrix[i][j]=edgeUses[i][j]/divisor
				for i in range(213):
					for j in range(213):
						if mousemap[i][j] == 0:
							ratesMatrix[i][j] = -1 * ratesMatrix[i][j]
				origHighTraffic = 0
				newHighTraffic = 0
				for i in range(213):
					for j in range(213):
						if ratesMatrix[i][j] > .85:
							origHighTraffic += 1
						elif ratesMatrix[i][j] < -.85:
							newHighTraffic += 1
				print("mouse IS High traffic original links: " + str(origHighTraffic) + ", High traffic new links: " + str(newHighTraffic))
				np.savetxt('undirmouseISTrafficRates.csv', ratesMatrix, delimiter=',')
				np.savetxt("undirmouseISTraffic.csv", edgeUses, delimiter=',')
				np.savetxt("undirmouseISEdgeAge.csv", edgeAvgAge, delimiter=',')

print('load.05')
main(.05, barcharts=False, monkey=False, coco=False, traffic=False)
main(.05, barcharts=False, monkey=False, coco=False, traffic=False)
main(.05, barcharts=False, monkey=False, coco=False, traffic=False)
main(.05, barcharts=False, monkey=False, coco=False, traffic=False)
main(.05, barcharts=False, monkey=False, coco=False, traffic=False)

print('load .1')
main(.1, barcharts=False, monkey=False, coco=False, traffic=False)
main(.1, barcharts=False, monkey=False, coco=False, traffic=False)
main(.1, barcharts=False, monkey=False, coco=False, traffic=False)
main(.1, barcharts=False, monkey=False, coco=False, traffic=False)
main(.1, barcharts=False, monkey=False, coco=False, traffic=False)

print('load .15')
main(.15, barcharts=False, monkey=False, coco=False, traffic=False)
main(.15, barcharts=False, monkey=False, coco=False, traffic=False)
main(.15, barcharts=False, monkey=False, coco=False, traffic=False)
main(.15, barcharts=False, monkey=False, coco=False, traffic=False)
main(.15, barcharts=False, monkey=False, coco=False, traffic=False)

print('load .2')
main(.2, barcharts=False, monkey=False, coco=False, traffic=False)
main(.2, barcharts=False, monkey=False, coco=False, traffic=False)
main(.2, barcharts=False, monkey=False, coco=False, traffic=False)
main(.2, barcharts=False, monkey=False, coco=False, traffic=False)
main(.2, barcharts=False, monkey=False, coco=False, traffic=False)


#What exactly is to be compared on the (bi)directional versions?
#collect a matrix of the nodes and 
#normalize, by adding transpose to matrix, divide each entry of traffic matrix by the value of A+A^T
#monkey is just frontal cortex, mouse is whole brain (fundamental differences, could just be true for cortex)
#brain works by inhibiting other cells, not by exciting other cells  exactly. what do these links mean? excitation passages? do we need inhibition passages?
#run correlation between traffic ratios and original weights
