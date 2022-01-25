# Event: Phase 3 NW3 (Jan. 2022)
# Author: PDST 
# A simple program to demonstrate use of matplotlib
from matplotlib import pyplot as plt

# Initialise a list of values
values = [2,3,5,2,4] 

# Intervals for the x-axis
x_axis = [0, 1, 2, 3, 4]

plt.plot(x_axis, values, color='blue', linestyle='solid', marker='o')

plt.title("Demo")
plt.ylabel("Values")

plt.show()





