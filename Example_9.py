import matplotlib.pyplot as plt

# Strategy 1

ST_1_1 = (0.0216,0.0519,0.0714,0.0942,0.1050)
ST_1_2 = (0.0382,0.0475,0.0526,0.0768,0.1173)
ST_1_3 = (0.0297,0.0561,0.0822,0.0834,0.1321)
ST_1_4 = (0.1179,0.1233,0.1351,0.1369,0.1669)
ST_1_5 = (0.0143,0.0256,0.0294,0.0366,0.0461)
ST_1_6 = (0.03300,0.0535,0.0832,0.0867,0.1014)
ST_1_7 = (0.0661,0.0921,0.1205,0.1398,0.1650)
ST_1_8 = (0.0629,0.08316,0.1210,0.1467,0.1642)

# Strategy 2

ST_2_1 = (0.0594,0.0691,0.0797,0.1020,0.1134)
ST_2_2 = (0.0613,0.0737,0.1075,0.1160,0.1299)
ST_2_3 = (0.1082,0.1216,0.1343,0.1410,0.1495)
ST_2_4 = (0.0949,0.1086,0.1288,0.1506,0.1583)
ST_2_5 = (0.0371,0.0498,0.0571,0.0688,0.0961)
ST_2_6 = (0.0752,0.0962,0.1056,0.1218,0.1465)
ST_2_7 = (0.0849,0.1209,0.1321,0.1574,0.1663)
ST_2_8 = (0.0737,0.1216,0.1498,0.1793,0.1923)

Strategy_1_all = [ST_1_1, ST_1_2,ST_1_3, ST_1_4, ST_1_5, ST_1_6,
                   ST_1_7, ST_1_8]

Strategy_2_all = [ST_2_1, ST_2_2,ST_2_3, ST_2_4, ST_2_5, ST_2_6,
                   ST_2_7, ST_2_8]

fig, (axes1, axes2) = plt.subplots(1, 2)
fig.set_dpi(150)

axes1.boxplot(Strategy_1_all)
axes1.set_title("Strategy 1", fontsize=15)
axes1.set(xlabel = 'Algorithm', ylabel = 'Solution')

axes2.boxplot(Strategy_2_all)
axes2.set_title("Strategy 1", fontsize=15)
axes2.set(xlabel = 'Algorithm', ylabel = 'Solution')

plt.tight_layout()
plt.savefig('Example_9', dpi=(250))
plt.show()