import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('example_data_6.txt')

F_df = data[data['Sex'] == 'F']
M_df = data[data['Sex'] == 'M']
I_df = data[data['Sex'] == 'I']

#Male; x - Length, y - weight
seria = M_df["Length"] 
x1 = seria.tolist()
seria = M_df["Whole weight"] 
y1 = seria.tolist()
seria = M_df["Rings"] 
z1 = seria.tolist()

#Female; x - Length, y - weight
seria = F_df["Length"] 
x2 = seria.tolist()
seria = F_df["Whole weight"] 
y2 = seria.tolist()
seria = F_df["Rings"] 
z2 = seria.tolist()


#Infant; x - Length, y - weight
seria = I_df["Length"] 
x3 = seria.tolist()
seria = I_df["Whole weight"] 
y3 = seria.tolist()
seria = I_df["Rings"] 
z3 = seria.tolist()

figure, axes = plt.subplots(2,2, figsize=(10, 6), layout='constrained')
figure.suptitle('Dependence of weight on length for different categories')
figure.tight_layout()
figure.set_dpi(120)

axes[0,0].scatter(x1, y1, s = z1, color='red', label = 'Male')
axes[0,0].set_title('Male')

axes[0,1].scatter(x2, y2, s = z2, color='green', label = 'Female')
axes[0,1].set_title('Female')

axes[1,0].scatter(x3, y3, s = z3, color='yellow', label = 'Infant')
axes[1,0].set_title('Infant')

axes[1,1].scatter(x1, y1, s = z1, color='red', label = 'Male')
axes[1,1].set_title('All')

axes[1,1].scatter(x2, y2, s = z2, color='yellow', label = 'Female')
axes[1,1].set_title('All')

axes[1,1].scatter(x3, y3, s = z3, color='green', label = 'Infant')
axes[1,1].set_title('All')


plt.tight_layout()
plt.savefig('Example_6', dpi=(250))
plt.show()