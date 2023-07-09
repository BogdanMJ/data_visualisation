import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('example_data_7.txt')

series = data["Series"] 
x = series.tolist()
series = data["Algorithm 1"] 
y1 = series.tolist()
series = data["Algorithm 2"] 
y2 = series.tolist()
series = data["Algorithm 3"] 
y3 = series.tolist()
series = data["Algorithm 4"] 
y4 = series.tolist()
series = data["Algorithm 5"] 
y5 = series.tolist()
series = data["Algorithm 6"] 
y6 = series.tolist()
series = data["Algorithm 7"] 
y7 = series.tolist()
series = data["Algorithm 8"] 
y8 = series.tolist()


fig = plt.figure()
fig.set_dpi(120)

ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y1, label = '1')
ax.plot(x, y2, label = '2')
ax.plot(x, y3, label = '3')
ax.plot(x, y4, label = '4')
ax.plot(x, y5, label = '5')
ax.plot(x, y6, label = '6')
ax.plot(x, y7, label = '7')
ax.plot(x, y8, label = '8')


ax.set(xlim = (0, 100), xlabel = 'Series',
       ylabel = 'Rating')
ax.set_title('Continuous function optimization')
ax.legend(title='Algorithm')

ax.axvline(x=5, color='red', linestyle='--', )

plt.tight_layout()
plt.savefig('Example_7', dpi=(250))
plt.show()