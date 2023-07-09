import matplotlib.pyplot as plt
import pandas as pd

"""
Given a set of 2000 investment portfolios described by (Mean)
and risk (Variance) and a set of 225 instruments included in
composition of portfolios also described with return and risk I've done the following
steps:
load the data available in the file and then draw based on them
scatterplot for assets and portfolios.
use text labels to mark on the chart: high-risk area
and high return, low risk and low return area,
the neighborhood of Sharpe's portfolio (the area can be indicated by dividing the range
returns in half and taking the center of that as the reference point
scope);
mark the 500 portfolios with the lowest return in green;
use red to mark the 500 portfolios with the highest return;
save the drawing to a file.
"""
# Financial instruments - assets; financial portfolios - Pareto Front

data_A = pd.read_csv('assets.txt')
data_PF = pd.read_csv('Pareto Front.txt')

# Financial instruments
seria = data_A["Mean"] 
x1 = seria.tolist()
seria = data_A["Variance"] 
y1 = seria.tolist()

# financial portfolios
seria = data_PF["Mean"] 
x2 = seria.tolist()
seria = data_PF["Variance"] 
y2 = seria.tolist()


figure, axes = plt.subplots()
figure.set_dpi(100)
figure.tight_layout()

axes.scatter(x1, y1)
axes.scatter(x2, y2)
axes.set(xlim=(-0.01, 0.005), ylim=(0, 0.005))

axes.set_xlabel('refund')
axes.set_ylabel('Risk level')

axes.axhline(y=0.0025, color='gray', linestyle='--')
axes.axvline(x=-0.003, color='gray', linestyle='--')


axes.text(0.25, 0.25, 'low risk and low return',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=10, color='red',
        transform=axes.transAxes)


axes.text(0.75, 0.75, 'high risk and high return',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=10, color='green',
        transform=axes.transAxes)

axes.text(0.25, 0.75, 'high risk and low return',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=10, color='black',
        transform=axes.transAxes)

axes.text(0.75, 0.25, 'low risk and high return',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=10, color='black',
        transform=axes.transAxes)

plt.tight_layout()
plt.savefig('Example_3', dpi=(250))
plt.show()