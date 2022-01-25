# Event: Phase 3 NW3 (Jan. 2022)
# Author: NCCA Sample ALT2 - Commute times
# Modified by: PDST
import statistics
import re
#import plotly.plotly
#from plotly.graph_objs import Bar, Layout
from matplotlib import pyplot as plt

# Open and read the data file
file = open("data.txt","r")
string = file.read()
file.close()

# Scrub the data
clean_string = re.sub(' minutes', '', string)
clean_string = re.sub(' ', '', clean_string)
string_array = clean_string.split('\n')

# Convert all the strings to integers
int_array = [int(i) for i in string_array]

# Determine the averages
mean_value = statistics.mean(int_array)
median_value =(statistics.median_grouped(int_array, 1))
mode_value =(statistics.mode(int_array))

print("Mean: %.2f, Median %d, Mode %d" %(mean_value, median_value, mode_value))

'''
plotly.offline.plot({           #https://plot.ly/python/getting-started/#initialization-for-offline-plotting
    "data": [Bar(y=int_array)],
    "layout": Layout(title="word count")
})
'''

# Initialise the values to display on the x-axis
x_axis = [0] * len(int_array)
for i in range(len(int_array)):
    x_axis[i] = i   
x_axis = [i for i in range(len(int_array))]
# x_axis = [i for i in range(len(int_array))] # alternative

# Plot a bar chart
plt.bar(x_axis, int_array)

plt.title("Bar Chart Demo") # graph title
plt.ylabel("Average Commute Times") # label the y-axis
# put the names of the subjects on the x-axis
#plt.xticks(range(len(subjects)), subjects, rotation=45)

plt.show() # Display the plot


