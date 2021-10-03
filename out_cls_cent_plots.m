% Influence vs. Out Close Cent 


x = [0, 0.01, 0.05, 0.1, 0.2]
%  Monkey1 IS
y1 = [-0.8001684, -0.8027371, -0.7671172, -0.7328259, -0.7173447]
% Monkey1 RW
y2 = [-0.7524747, -0.7829376, -0.8895612, -0.8945713, -0.8978071]
% Monkey2 IS
y3 = [-0.3508149, -0.3588430, -0.3699330, -0.3757980, -0.3721378]
% Monkey2 RW
y4 = [-0.007000943, -0.082475541, -0.273168753, -0.361398449, -0.454879881]
% Mouse IS
y5 = [0.1078196, 0.1138621, 0.1525914, 0.1666392, 0.2280848]
% Mouse RW
y6 = [-0.05277648, -0.12212434, -0.25984469, -0.31211641, -0.36486320]


y1 = [-0.8001684, -0.8027371, -0.7671172, -0.7328259, -0.7173447]
y2 = [-0.7524747, -0.7829376, -0.8895612, -0.8945713, -0.8978071]
y3 = [-0.3508149, -0.3588430, -0.3699330, -0.3757980, -0.3721378]
y4 = [-0.007000943, -0.082475541, -0.273168753, -0.361398449, -0.454879881]
y5 = [ 0.1078196, 0.1138621, 0.1525914, 0.1666392, 0.2280848]
y6 = [ -0.05277648, -0.12212434, -0.25984469, -0.31211641, -0.36486320]


figure
plot(x, y1, "- ro", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "r", ...
	"MarkerEdgeColor", "r", ...
	"MarkerSize", 7)
title("Pearson Correlation Between Mean Visitation and Closeness Centrality", "FontSize", 25)
xlabel("Load", "FontSize", 16)
ylabel("Correlation", "FontSize", 16)

hold on
plot(x, y2, "-- ro", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "r", ...
	"MarkerEdgeColor", "r", ...
	"MarkerSize", 7)

hold on
plot(x, y3, "- go", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "g", ...
	"MarkerEdgeColor", "g", ...
	"MarkerSize", 7)

hold on
plot(x, y4, "-- go", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "g", ...
	"MarkerEdgeColor", "g", ...
	"MarkerSize", 7)

hold on

plot(x, y5, "- bo", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "b", ...
	"MarkerEdgeColor", "b", ...
	"MarkerSize", 7)

hold on
plot(x, y6, "-- bo", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "b", ...
	"MarkerEdgeColor", "b", ...
	"MarkerSize", 7)

legend("Monkey2, IS", "Monkey2, RW", "Monkey1, IS", "Monkey1, RW", "Mouse, IS", "Mouse, RW")
ylim([-1, 1])	
hold off



% Redundancy vs. Out Close Cent

x = [0, 0.01, 0.05, 0.1, 0.2]
% Monkey1 IS
y1 = [-0.2586955, -0.2507910, -0.3322763, -0.1930321, -0.1347971]
% Monkey1 RW
y2 = [-0.08273519, -0.04536504,  0.03420807,  0.21630407,  0.32344974]
% Monkey2 IS
y3 = [-0.1637672, -0.1130369, -0.2261289, -0.1823132, -0.1582083]
% Monkey2 RW
y4 = [-0.10190957, -0.09260325, -0.09654876, -0.09928940, -0.10149816]
% Mouse IS
y5 = [ 0.0617229846,  0.2119541863,  0.0841406107,  0.0814918586, -0.0006642717]
% Mouse RW
y6 = [-0.13014377, -0.08831286, -0.12401741, -0.14766742, -0.16662328]

y1 = [-0.2586955, -0.2507910, -0.3322763, -0.1930321, -0.1347971]
y2 = [-0.08273519, -0.04536504,  0.03420807,  0.21630407,  0.32344974]
y3 = [-0.1637672, -0.1130369, -0.2261289, -0.1823132, -0.1582083]
y4 = [-0.10190957, -0.09260325, -0.09654876, -0.09928940, -0.10149816]
y5 = [0.0617229846,  0.2119541863,  0.0841406107,  0.0814918586, -0.0006642717]
y6 = [-0.13014377, -0.08831286, -0.12401741, -0.14766742, -0.16662328]



figure
plot(x, y1, "- ro", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "r", ...
	"MarkerEdgeColor", "r", ...
	"MarkerSize", 7)
title("Pearson Correlation Between Mean Overstay and Closeness Centrality", "FontSize", 25)
xlabel("Load", "FontSize", 16)
ylabel("Correlation", "FontSize", 16)

hold on
plot(x, y2, "-- ro", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "r", ...
	"MarkerEdgeColor", "r", ...
	"MarkerSize", 7)

hold on
plot(x, y3, "- go", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "g", ...
	"MarkerEdgeColor", "g", ...
	"MarkerSize", 7)

hold on
plot(x, y4, "-- go", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "g", ...
	"MarkerEdgeColor", "g", ...
	"MarkerSize", 7)

hold on

plot(x, y5, "- bo", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "b", ...
	"MarkerEdgeColor", "b", ...
	"MarkerSize", 7)

hold on
plot(x, y6, "-- bo", ...
	"LineWidth", 2, ...
	"MarkerFaceColor", "b", ...
	"MarkerEdgeColor", "b", ...
	"MarkerSize", 7)

legend("Monkey2, IS", "Monkey2, RW", "Monkey1, IS", "Monkey1, RW", "Mouse, IS", "Mouse, RW")
ylim([-1, 1])	
hold off


% Vis 










