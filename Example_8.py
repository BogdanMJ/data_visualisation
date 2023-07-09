import matplotlib.pyplot as plt


# A - 1; B - 26; C - 51; D - 76

Algorithm_A = (2.38729,2.328662,4.231087,2.209522,1.176968,3.1967,
              2.273016,3.249281)
Algorithm_B = (0.538459,0.257165,0.274095,0.219281,0.221804,0.270092,
              0.172984,0.0860803)
Algorithm_C = (0.328015,0.292987,0.25361,0.207544,0.262962,0.151578,
              0.255272,0.156909)
Algorithm_D = (0.196328,0.344952,0.30918,0.402479,0.208477,0.332364,
              0.325413,0.450263)

Algorithm_all = [Algorithm_A, Algorithm_B, Algorithm_C, Algorithm_D]

fig, axes = plt.subplots()
fig.set_dpi(120)

axes.boxplot(Algorithm_all)
axes.set_title("Algorithm operation", fontsize=20)
axes.set(xlabel = 'Algorithm', ylabel = 'Rating')

plt.savefig('Example_8', dpi=(250))
plt.show()