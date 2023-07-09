import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('example_data_10.txt')

# F1 - feathers yes F0 - feathers no
F1_count = data['feathers'].value_counts()[1]
F0_count = data['feathers'].value_counts()[0]

labels1 = ['Feathers', 'Others']
sizes1 = [(F1_count), (F0_count)]
cuts = (0, 0)

# E1 - eggs yes E0 - eggs no
E1_count = data['eggs'].value_counts()[1]
E0_count = data['eggs'].value_counts()[0]

labels2 = ['oviparous', 'Others']
sizes2 = [(E1_count), (E0_count)]
cuts = (0, 0)

# A1 - fly A0 - don't fly
A1_count = data['airborne'].value_counts()[1]
A0_count = data['airborne'].value_counts()[0]

labels3 = ['Fly', 'Others']
sizes3 = [(A1_count), (A0_count)]
cuts = (0, 0)

# P1 - predatory P0 -  no predatory 
P1_count = data['predator'].value_counts()[1]
P0_count = data['predator'].value_counts()[0]

labels4 = ['Predatory', 'Others']
sizes4 = [(P1_count), (P0_count)]
cuts = (0, 0)

# V1 - jadowite tak V0 - jadowite nie
V1_count = data['venomous'].value_counts()[1]
V0_count = data['venomous'].value_counts()[0]

labels5 = ['Jadowite', 'Pozostałe']
sizes5 = [(V1_count), (V0_count)]
cuts = (0, 0)

# T1 - tail T0 - no tail
T1_count = data['tail'].value_counts()[1]
T0_count = data['tail'].value_counts()[0]

labels6 = ['Tail', 'No tail']
sizes6 = [(T1_count), (T0_count)]
cuts = (0, 0)

fig, axes = plt.subplots(2, 3)
fig.set_dpi(150)
fig.suptitle("Types of animals in the zoo", fontsize = 14)

axes[0][0].pie(sizes1, explode=cuts, labels=labels1, 
         autopct='%1.1f%%', textprops={'fontsize': 5})
axes[0][0].set_title("Distribution of individuals with and without feathers", fontsize=5)

axes[0][1].pie(sizes2, explode=cuts, labels=labels2, 
         autopct='%1.1f%%', textprops={'fontsize': 5})
axes[0][1].set_title("Distribution of egg-laying individuals", fontsize=5)

axes[0][2].pie(sizes3, explode=cuts, labels=labels3, 
         autopct='%1.1f%%', textprops={'fontsize': 5})
axes[0][2].set_title("Distribution of flying individuals", fontsize=5)

axes[1][0].pie(sizes4, explode=cuts, labels=labels4, 
         autopct='%1.1f%%', textprops={'fontsize': 5})
axes[1][0].set_title("Distribution of predatory individuals", fontsize=5)

axes[1][1].pie(sizes5, explode=cuts, labels=labels5, 
         autopct='%1.1f%%', textprops={'fontsize': 5})
axes[1][1].set_title("Distribution of venomous individuals", fontsize=5)

axes[1][2].pie(sizes6, explode=cuts, labels=labels6, 
         autopct='%1.1f%%', textprops={'fontsize': 5})
axes[1][2].set_title("Distribution of individuals with a tail", fontsize=5)

fig.tight_layout()
plt.savefig('Example_10', dpi=(250))
plt.show()
