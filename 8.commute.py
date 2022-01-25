# Sample ALT2 - Commute times
import statistics
import re
import plotly.plotly
from plotly.graph_objs import Bar, Layout

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

# Determine and display the averages
mean_value = statistics.mean(int_array)
median_value = statistics.median_grouped(int_array, 1)
mode_value = statistics.mode(int_array)
print("Mean: %.2f, Median %d, Mode %d" %(mean_value, median_value, mode_value))

plotly.offline.plot({"data": [Bar(y=int_array)],
    "layout": Layout(title="word count")
})
