from Ensemble import Ensemble

def main():
	helper = Ensemble()
	helper.er_graph_write(10, 0.3, "er_10.csv")
	helper.er_graph_write(50, 0.3, "er_50.csv")
	helper.er_graph_write(100, 0.3, "er_100.csv")
	helper.er_graph_write(200, 0.3, "er_200.csv")
	helper.er_graph_write(400, 0.3, "er_400.csv")

main()