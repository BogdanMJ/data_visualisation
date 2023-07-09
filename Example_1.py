import matplotlib.pyplot as plt

#Warsaw
x1 = ['I', 'II','III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
y1 = [-1.9, -0.8, 3.2, 9.3, 14.6, 18, 20.1, 19.5, 14.7, 9.3, 4.8, 0.5]

#Miami
y2 = [20.5, 21.4, 22.3, 24, 25.6, 27, 27.8, 28, 27.2 ,25.8, 23.4, 22]


fig, axes = plt.subplots(2)
fig.suptitle("Average monthly temperatures", fontsize = 14)
fig.set_dpi(120)
fig.tight_layout()

# Warszawa
axes[0].plot(x1, y1, linewidth = 2.5, color = 'orange')
axes[0].set(xlim = (0,12), ylim = (-2,25))
axes[0].set_title('Warsaw')
axes[0].set(ylabel='Temperature[*C]')

#Miami
axes[1].plot(x1, y2, linewidth = 2.5, color = 'red')
axes[1].set(xlim = (0,12), ylim = (20,30))
axes[1].set_title('Miami')
axes[1].set(ylabel='Temperature[*C]')

plt.savefig('Example_1', dpi=(250))

plt.show()