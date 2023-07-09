import matplotlib.pyplot as plt
import pandas as pd

# Data 
data = pd.read_csv('example_data_11.txt')

seria = data["Solution"]
seria = seria.iloc[::4]
x = seria.tolist()

seria = data["set1"] 
seria = seria.iloc[::4]
y1 = seria.tolist()

seria = data["set2"]
seria = seria.iloc[::4]
y2 = seria.tolist()

seria = data["set3"] 
seria = seria.iloc[::4]
y3 = seria.tolist()

def point_size(y):
    if y <= 0.25:
        return 25
    elif y <= 0.5:
        return 50
    elif y <= 0.75:
        return 75
    else:
        return 100

figure, axes = plt.subplots()
axes.scatter(x, y1, s = [point_size(y) for y in y1], color='red', label = 'set1')
axes.scatter(x, y2, s = [point_size(y) for y in y2], color='green', label = 'set2')
axes.scatter(x, y3, s = [point_size(y) for y in y2], color='blue', label = 'set')
axes.set(xlim = (-10, 110), xlabel = 'Solution',
       ylabel = 'Accuracy')

figure.tight_layout()
plt.savefig('Example_11', dpi=(250))
figure.set_dpi(120)