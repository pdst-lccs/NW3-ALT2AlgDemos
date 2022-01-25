# Event: Phase 3 NW3 (Jan. 2022)
# Author: PDST 
# A simple program to demonstrate use of matplotlib
from matplotlib import pyplot as plt

# Initialise a list of subjects
subjects = ['Irish', 'English', 'Maths', 'LCCS', 'Ag. Sc.']

percentages = [60, 72, 68, 83, 76] # Average percentages

# Plot a bar chart
plt.bar(subjects, percentages)

plt.title("Bar Chart Demo") # graph title
plt.ylabel("Average Percentages") # label the y-axis
# put the names of the subjects on the x-axis
plt.xticks(range(len(subjects)), subjects, rotation=45)

plt.show() # Display the plot


'''
ax = plt.subplots()
ax.barh(range(len(subjects)), subjects)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
'''




