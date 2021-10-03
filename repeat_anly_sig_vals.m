x = [0, 0.01, 0.05, 0.1, 0.2]
alpha = [0.05, 0.05, 0.05, 0.05, 0.05]

% "t-stats, influence vs. indegree"
y1 = [2.145664e-13, 2.584427e-14, 1.165875e-14, 1.048582e-14, 9.849393e-14]
y2 = [8.896044e-01, 3.023630e-01, 2.047583e-06, 1.428414e-10, 5.695435e-16]
y3 = [4.873947e-42, 6.172698e-42, 7.338825e-33, 2.049944e-27, 1.406549e-25]
y4 = [2.435328e-23, 3.182030e-26, 3.659853e-65, 1.559207e-80, 2.784477e-88]
y5 = [5.185603e-05, 5.953350e-05, 3.512060e-04, 4.325452e-04, 8.954582e-03]
y6 = [2.788267e-02, 3.450398e-02, 6.153620e-18, 9.173702e-25, 1.384198e-32]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Influence, In Degree) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off

% "t-stats, influence vs. outdegree"
y1 = [0.0021616267, 0.0005752990, 0.0005238840, 0.0004689681, 0.0008708580]
y2 = [9.887722e-02, 3.865418e-01, 2.397385e-02, 5.010909e-04, 7.176901e-07]
y3 = [0.322597242, 0.266207452, 0.033267104, 0.004961299, 0.002323268]
y4 = [0.2279392, 0.2146100, 0.1201313, 0.1413079, 0.1692424]
y5 = [5.512302e-20, 1.052860e-17, 7.089861e-21, 1.715706e-21, 1.227349e-26]
y6 = [0.09998180, 0.12476986, 0.03587138, 0.15882849, 0.41120382]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Influence, Out Degree) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off

% "t-stats, influence vs. closeness"
y1 = [2.735492e-05, 2.353069e-07, 5.790093e-06, 4.810555e-06, 1.809449e-05]
y2 = [8.936628e-01, 4.381366e-02, 2.920582e-05, 1.762990e-07, 2.247585e-10]
y3 = [4.545171e-54, 1.170446e-52, 8.114161e-39, 4.900388e-32, 5.245647e-30]
y4 = [3.281990e-22, 4.308035e-25, 6.785793e-58, 3.367615e-71, 9.217246e-81]
y5 = [4.769581e-14, 6.640796e-15, 6.748104e-15, 9.759333e-15, 2.415254e-11]
y6 = [4.064199e-01, 1.491153e-01, 8.264427e-11, 1.104703e-14, 1.755533e-19]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Influence, Closeness Centrality) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off

% "t-stats, influence vs. betweenness"
y1 = [1.048428e-06, 5.673356e-07, 2.361668e-07, 1.465826e-07, 1.976199e-07]
y2 = [9.248554e-01, 2.656973e-01, 1.755688e-04, 4.649455e-07, 8.766946e-11]
y3 = [1.824700e-21, 1.089854e-21, 7.565009e-19, 1.492603e-16, 1.253152e-15]
y4 = [8.026466e-18, 4.818450e-20, 4.926938e-32, 6.984466e-33, 1.875600e-33]
y5 = [0.1175450218, 0.0982419519, 0.0263066277, 0.0151419521, 0.0008212309]
y6 = [4.446129e-01, 7.601495e-02, 1.297290e-04, 3.588379e-06, 4.478718e-08]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Influence, Betweenness Centrality) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off

% "t-stats, redundancy vs. indegree"
y1 = [8.735302e-04, 1.764484e-04, 1.280535e-07, 4.209530e-06, 4.847857e-05]
y2 = [0.009083839, 0.005120900, 0.006419141, 0.006966851, 0.007604988]
y3 = [0.0046764245, 0.0053796504, 0.0001117296, 0.0301393856, 0.1330064683]
y4 = [0.2065206497, 0.2548693004, 0.8611943231, 0.0261545861, 0.0001051119]
y5 = [7.597555e-04, 5.014063e-03, 1.187360e-04, 4.488802e-05, 9.313331e-05]
y6 = [0.0001688483, 0.0019170168, 0.0015690551, 0.0007205510, 0.0002727019]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Redundancy, In Degree) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off

% "t-stats, influence vs. outdegree"
y1 = [2.043725e-01, 2.108370e-01, 6.852441e-05, 4.542440e-05, 5.433256e-05]
y2 = [0.0006020727, 0.0003062249, 0.0002655609, 0.0002149858, 0.0001749613]
y3 = [1.132083e-06, 5.451111e-07, 9.620274e-09, 3.639109e-06, 1.075740e-04]
y4 = [0.09918230, 0.83508972, 0.09285267, 0.64305416, 0.63609391]
y5 = [2.616748e-04, 1.407006e-10, 5.910413e-07, 2.496264e-05, 2.730238e-02]
y6 = [0.0044247936, 0.0068586217, 0.0015200519, 0.0004267805, 0.0000663186]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Redundancy, Out Degree) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off

% "t-stats, redundancy vs. closeness"
y1 = [0.04605545, 0.02629480, 0.04026809, 0.05634783, 0.07902902]
y2 = [0.2024758, 0.1308090, 0.1666247, 0.1739383, 0.1791021]
y3 = [3.778340e-03, 4.108417e-03, 5.664993e-05, 2.383075e-02, 1.172036e-01]
y4 = [9.762480e-02, 1.626247e-01, 7.170402e-01, 2.015175e-02, 2.544137e-05]
y5 = [6.232320e-12, 1.006656e-06, 4.672805e-21, 1.980725e-22, 7.025913e-23]
y6 = [8.143916e-06, 1.741557e-04, 1.157393e-04, 5.879274e-05, 2.336600e-05]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Redundancy, Closeness Centrality) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off

% "t-stats, redundancy vs. betweenness"
y1 = [0.026328863, 0.126572344, 0.002025017, 0.013250733, 0.031957298]
y2 = [0.1686561, 0.2112047, 0.1923106, 0.1799320, 0.1703910]
y3 = [0.013286851, 0.016494957, 0.001291586, 0.066767484, 0.202688360]
y4 = [0.43558453, 0.66938479, 0.74752288, 0.03946239, 0.00176371]
y5 = [0.371193622, 0.001914479, 0.222454541, 0.237407981, 0.992328650]
y6 = [0.05852129, 0.20027931, 0.07154421, 0.03162220, 0.01515177]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Redundancy, Betweenness Centrality) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off

% "t-stats, avgdeathage vs. indegree"
y1 = [3.369078e-04, 3.509903e-04, 2.261831e-08, 3.294531e-09, 1.653073e-09]
y2 = [7.010530e-01, 3.660280e-01, 6.352039e-06, 7.211761e-10, 3.022103e-15]
y3 = [1.447592e-12, 2.209170e-11, 6.196382e-65, 7.292917e-62, 2.740725e-52]
y4 = [3.023289e-16, 4.032798e-20, 8.407472e-61, 3.151633e-80, 8.438295e-89]
y5 = [2.336895e-04, 7.940053e-04, 1.708247e-05, 9.273566e-06, 1.108580e-07]
y6 = [2.596005e-06, 6.418455e-10, 2.557982e-48, 6.538110e-52, 2.609915e-59]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Average Death Age, In Degree) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off

% "t-stats, avgdeathage vs. outdegree"
y1 = [0.326333681, 0.298966207, 0.047656432, 0.016229552, 0.004539785]
y2 = [6.917199e-02, 3.455067e-01, 3.544619e-02, 9.172585e-04, 1.254205e-06]
y3 = [3.392668e-07, 9.742281e-08, 5.672612e-01, 3.804761e-01, 3.890040e-01]
y4 = [0.43941013, 0.27033512, 0.09715331, 0.13643740, 0.16522618]
y5 = [1.493873e-07, 7.981901e-11, 3.418673e-15, 1.365264e-10, 3.330063e-05]
y6 = [0.7672155, 0.1348996, 0.9222406, 0.7330094, 0.4423400]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Average Death Age, Out Degree) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off

% "t-stats, avgdeathage vs. closeness"
y1 = [0.08717468, 0.11285212, 0.06041130, 0.01330429, 0.01180662]
y2 = [8.936605e-01, 3.545847e-02, 6.674728e-05, 7.389823e-07, 8.584988e-10]
y3 = [5.909517e-13, 1.021731e-11, 1.398591e-64, 2.033416e-68, 2.501840e-77]
y4 = [1.404727e-15, 2.443130e-19, 4.200040e-54, 9.707294e-70, 7.585601e-80]
y5 = [2.981568e-12, 3.570015e-06, 1.551892e-07, 3.592700e-07, 5.858019e-09]
y6 = [4.633107e-04, 8.495213e-09, 3.895398e-30, 6.392983e-31, 1.783630e-34]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Average Death Age, Closeness Centrality) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off

% "t-stats, avgdeathage vs. betweenness"
y1 = [1.557423e-02, 8.755922e-02, 2.064049e-05, 3.336909e-05, 1.778950e-05]
y2 = [9.581338e-01, 3.431206e-01, 2.618246e-04, 7.029596e-07, 1.081717e-10]
y3 = [7.990184e-10, 2.135458e-09, 3.864500e-28, 9.767957e-28, 4.488332e-24]
y4 = [4.759358e-13, 9.419547e-16, 1.705373e-31, 4.962217e-33, 1.343353e-33]
y5 = [8.133636e-02, 6.088683e-03, 9.073322e-05, 2.596185e-05, 1.423415e-03]
y6 = [4.496990e-02, 5.472482e-05, 8.282339e-10, 7.321899e-11, 1.396634e-12]
figure
plot(x,y1, "- .",  'MarkerSize', 20, "color", "red")
title("p-values for Cor(Average Death Age, Betweenness Centrality) vs. Load")
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
plot(x, alpha, "--", "color", "black")
legend("Cocomac, IS", "Cocomac, RW", "Monkey91, IS", "Monkey91, RW", "Thres. Mouse, IS", "Thres. Mouse, RW")
ylim([0, 1])
hold off
