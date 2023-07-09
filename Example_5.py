import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('example_data_5.txt')

F_count = data['sex'].value_counts()['F']
M_count = data['sex'].value_counts()['M']
I_count = data['sex'].value_counts()['I']

F_df = data[data['sex'] == 'F']
M_df = data[data['sex'] == 'M']
I_df = data[data['sex'] == 'I']

mean_rings_F = F_df.mean()
mean_rings_M = M_df.mean()
mean_rings_I = I_df.mean()

print(mean_rings_F)
print(mean_rings_M)
print(mean_rings_I)

"""
mean_rings_F=11
mean_rings_M=11
mean_rings_I=8
"""

#Data Number of individuals belonging to each category (M, F and I)
x = ['Male', 'Female', 'Infant']
y = [1528, 1307, 1342]
#Chart
figure, axes = plt.subplots()
axes.bar(x, y, width = 0.8, edgecolor = 'black', linewidth = 2)
axes.set(xlim = (-1, 3), xticks = np.arange(0,3), 
         ylim = (0, 2000), yticks = np.arange(0, 2100, 100),
         xlabel = 'Sex', ylabel = 'Number of individuals')
axes.set_title('The number of individuals belonging to each category')
plt.savefig('Example_5A', dpi=(250))
plt.show()

# Average number of rings for each category (M, F and I).
y2 = [11, 11, 8]
#Chart
figure, axes = plt.subplots()
axes.bar(x, y2, width = 0.8, edgecolor = 'black', linewidth = 2)
axes.set(xlim = (-1, 3), xticks = np.arange(0,3), 
         ylim = (0, 12), yticks = np.arange(0, 12, 1),
         xlabel = 'Sex', ylabel = 'Number of rings')
axes.set_title('The average number of rings for each category')
plt.savefig('Example_5B', dpi=(250))
plt.show()
