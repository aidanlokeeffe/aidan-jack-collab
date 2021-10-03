% Correlation of Influence and In Degree vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [-0.5067358  , -0.5230909 , -0.5290222 , -0.5298036 , -0.5128546]
y2 = [ 0.010302763, -0.07644392, -0.3418042 , -0.4502610 , -0.5505172]
y3 = [-0.9356863  , -0.9353327 , -0.8944474 , -0.8574319 , -0.8419666]
y4 = [-0.8205764  , -0.8476014 , -0.9809867 , -0.9914599 , -0.9942884]
y5 = [-0.2742300  , -0.2721152 , -0.2432232 , -0.2395987 , -0.1791202]
y6 = [-0.15104882 , -0.14528687,  -0.5469349, -0.62912568, -0.70037160]

figure
plot(x,y1, "- ro",...
	"LineWidth", 2,...
	"MarkerFaceColor", [1 1 1],... 
	"MarkerEdgeColor", "r",...
	'MarkerSize', 10)
title("Pearson Correlation Between Mean Visitation and In Degree", "FontSize", 16)
xlabel("Load", "FontSize", 13)
ylabel("Correlation", "FontSize", 13)
hold on

plot([0, 0.01], [-0.5067358  , -0.5230909], "- wo", ...
	"LineStyle", "none",...
	"MarkerFaceColor", "r",...
	"MarkerEdgeColor", "r",...
	"MarkerSize", 10)

hold on






plot(x,y2, "-. .", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-. .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-. .", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off

% Correlation of Influence and Out Degree vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [ -0.2247399,       -0.2514445,       -0.2532274,       -0.2553200,       -0.2433915]
y2 = [0.122039789,       0.06420708,       -0.1664006,       -0.2540701,       -0.3557957]
y3 = [  0.1048528,        0.1177743,        0.2234229,        0.2921050,        0.3154193]
y4 = [ -0.1276368,       -0.1313422,       -0.1640887,       -0.1554060,       -0.1453444]
y5 = [  0.5741205,        0.5436752,        0.5852051,        0.5926335,        0.6480436]
y6 = [ 0.11328087,       0.10575753,        0.1442159,       0.09711735,       0.05672981]

figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("Correlation of Influence and Out Degree vs. Load")
hold on
plot(x,y2, "-..", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-..", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-..", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off

% Correlation of Influence and Closeness Centrality vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [  -0.3039420,       -0.3699783,       -0.3272261,       -0.3298805,       -0.3103323]
y2 = [-0.009921724,      -0.14879753,       -0.3029159,       -0.3735418,       -0.4459092]
y3 = [  -0.9659972,       -0.9633755,       -0.9235640,       -0.8895754,       -0.8765357]
y4 = [  -0.8085760,       -0.8375720,       -0.9721879,       -0.9861216,       -0.9915606]
y5 = [  -0.4873877,       -0.5015311,       -0.5014187,       -0.4988201,       -0.4378934]
y6 = [ -0.05731103,      -0.09942469,       -0.4270962,      -0.49794224,      -0.56766939]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("Correlation of Influence and Closeness Centrality vs. Load")
hold on
plot(x,y2, "-..", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-..", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-..", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off

% Correlation of Influence and Betweenness Centrality vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [  -0.3508149,       -0.3588430,       -0.3699330,       -0.3757980,       -0.3721378]
y2 = [-0.007000943,      -0.08247554,       -0.2731688,       -0.3613984,       -0.4548799]
y3 = [  -0.8001684,       -0.8027371,       -0.7671172,       -0.7328259,       -0.7173447]
y4 = [  -0.7524747,       -0.7829376,       -0.8895612,       -0.8945713,       -0.8978071]
y5 = [   0.1078196,        0.1138621,        0.1525914,        0.1666392,        0.2280848]
y6 = [ -0.05277648,      -0.12212434,       -0.2598447,      -0.31211641,      -0.36486320]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("Correlation of Influence and Betweenness Centrality vs. Load")
hold on
plot(x,y2, "-..", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-..", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-..", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off



% Correlation of Redundancy and In Degree vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [ -0.24333100, -0.27308107,  -0.3774390, -0.3317767,   -0.2948405]
y2 = [ -0.1918469, -0.20556154, -0.20025659, -0.1983024,  -0.19619122]
y3 = [ -0.2939908,  -0.2895031,  -0.3939538, -0.2274509,   -0.1586831]
y4 = [ -0.13367106, -0.12058874, -0.01858502, 0.23312942,   0.39534604]
y5 = [ -0.22951251,  -0.1920637, -0.26126995,-0.27642189,-0.2651383523]
y6 = [ -0.2555538, -0.21192803,  -0.2158502, -0.2304797,   -0.2475533]

figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("Correlation of Redundancy and In Degree vs. Load")
hold on
plot(x,y2, "-..", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-..", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-..", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off

% Correlation of Redundancy and Out Degree vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [-0.09399936,       -0.09267755,        -0.2891839,        -0.2958910,        -0.2929902]
y2 = [ -0.2505736,       -0.26321626,       -0.26580215,        -0.2695894,       -0.27322963]
y3 = [ -0.4845775,        -0.4968789,         0.5572738,         0.4638722,         0.3948188]
y4 = [ 0.17392868,       -0.02212622,       -0.17722073,        0.04923206,       -0.05026488]
y5 = [ 0.24825252,         0.4223051,        0.33501486,        0.28514956,      0.1516078898]
y6 = [ -0.1947523,       -0.18517240,        -0.2164653,        -0.2398338,        -0.2704498]

figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("Correlation of Redundancy and Out Degree vs. Load")
hold on
plot(x,y2, "-..", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-..", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-..", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off

% Correlation of Redundancy and Closeness Centrality vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [-0.14726562,       -0.16380381,        -0.1513601,        -0.1409418,        -0.1298159]
y2 = [ -0.0943929,       -0.11179886,       -0.10239536,        -0.1006665,       -0.09947802]
y3 = [ -0.3006911,        -0.2980780,        -0.4091046,        -0.2367899,        -0.1653795]
y4 = [-0.17472306,       -0.14760921,       -0.03850992,        0.24326186,        0.42607529]
y5 = [-0.44935883,        -0.3284467,       -0.58740768,       -0.60358114,     -0.6086910998]
y6 = [ -0.3010494,       -0.25504504,        -0.2616799,        -0.2723077,        -0.2861147]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("Correlation of Redundancy and Closeness Centrality vs. Load")
hold on
plot(x,y2, "-..", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-..", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-..", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off

% Correlation of Redundancy and Betweenness Centrality vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [-0.16376719,       -0.11303694,        -0.2261289,        -0.1823132,        -0.1582083]
y2 = [ -0.1019096,       -0.09260325,       -0.09654876,        -0.0992894,       -0.10149816]
y3 = [ -0.2586955,        -0.2507910,        -0.3322763,        -0.1930321,        -0.1347971]
y4 = [-0.08273519,       -0.04536504,        0.03420807,        0.21630407,        0.32344974]
y5 = [ 0.06172298,         0.2119542,        0.08414061,        0.08149186,     -0.0006642717]
y6 = [ -0.1301438,       -0.08831286,        -0.1240174,        -0.1476674,        -0.1666233]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("Correlation of Redundancy and Betweenness Centrality vs. Load")
hold on
plot(x,y2, "-..", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-..", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-..", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off


% Correlation of Average Death Age and In Degree vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [ -0.2614684,        -0.26071517,         -0.3977303,         -0.4187877,         -0.4259857]
y2 = [0.028489847,        -0.06702100,         -0.3258901,         -0.4344256,         -0.5388244]
y3 = [ -0.6574890,         -0.6300683,        -0.98075827,        -0.97740811,        -0.96265542]
y4 = [-0.72780618,         -0.7839169,         -0.9761173,         -0.9913232,         -0.9944400]
y5 = [ -0.2501584,         -0.2287045,         -0.2906410,         -0.2992532,         -0.3547251]
y6 = [-0.31636758,         -0.4082094,       -0.799210579,        -0.81611277,        -0.84614523]

figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("Correlation of Average Death Age and In Degree vs. Load")
hold on
plot(x,y2, "-..", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-..", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-..", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off

% Correlation of Average Death Age and Out Degree vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [ -0.0727589,        -0.07698143,         -0.1462093,         -0.1770087,         -0.2083388]
y2 = [0.134280438,         0.06993540,         -0.1551688,         -0.2423644,         -0.3484298]
y3 = [ -0.5046112,         -0.5240890,        -0.06075574,        -0.09302298,        -0.09137593]
y4 = [-0.08204975,         -0.1167699,         -0.1749655,         -0.1573104,         -0.1467109]
y5 = [  0.3513096,          0.4274068,          0.5061510,          0.4225783,          0.2808995]
y6 = [-0.02044945,         -0.1030166,        0.006743801,        -0.02356464,        -0.05303991]

figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("Correlation of Average Death Age and Out Degree vs. Load")
hold on
plot(x,y2, "-..", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-..", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-..", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off

% Correlation of Average Death Age and Closeness Centrality vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [ -0.1264543,        -0.11728033,         -0.1387071,         -0.1822090,         -0.1852727]
y2 = [0.009921943,        -0.15515856,         -0.2896176,         -0.3554145,         -0.4326713]
y3 = [ -0.6659244,         -0.6381105,        -0.98039963,        -0.98395705,        -0.98991174]
y4 = [-0.71648371,         -0.7737665,         -0.9660585,         -0.9850248,         -0.9911495]
y5 = [ -0.4554238,         -0.3121843,         -0.3508704,         -0.3410205,         -0.3864189]
y6 = [-0.23839109,         -0.3825953,       -0.680113133,        -0.68678721,        -0.71491946]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("Correlation of Average Death Age and Closeness Centrality vs. Load")
hold on
plot(x,y2, "-..", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-..", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-..", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off

% Correlation of Average Death Age and Betweenness Centrality vs. Load
x = [0, 0.01, 0.05, 0.1, 0.2]
y1 = [  -0.1780979,-0.12630194,  -0.3083128,-0.3008154,-0.3105920]
y2 = [-0.003896564,-0.07028126,  -0.2660579,-0.3560658,-0.4529000]
y3 = [  -0.5893024, -0.5770562, -0.86307497,-0.85996942,-0.82792866]
y4 = [ -0.66792234, -0.7194834,  -0.8862460,-0.8954229,-0.8986117]
y5 = [   0.1199852,  0.1878187,   0.2655507, 0.2845748, 0.2177334]
y6 = [ -0.13785646, -0.2734073,-0.405775942,-0.42817611,-0.46153983]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("Correlation of Average Death Age and Betweenness Centrality vs. Load")
hold on
plot(x,y2, "-..", 'MarkerSize', 20, "color", "red")
hold on
plot(x,y3, "- .", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y4, "-..", 'MarkerSize', 20, "color", "green")
hold on
plot(x,y5, "- .", 'MarkerSize', 20, "color", "blue")
hold on
plot(x, y6, "-..", 'MarkerSize', 20, "color", "blue")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([-1, 1])
hold off

