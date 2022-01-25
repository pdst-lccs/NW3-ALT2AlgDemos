# Event: Phase 3 NW3 (Jan. 2022)
# Author: PDST 
# Using pandas - recommended for larger files
import statistics
import pandas

# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('FIFA21-player-list.csv')

# Filter out the column, value_eur
player_values = df['value_eur']

# Compute and display the mean
mean_value = round(statistics.mean(player_values), 2)
print("Mean Value:", mean_value)

# Compute and display the median
median_value = statistics.median(player_values)
print("Median Value:", median_value)

# Compute and display the min and max values
print("Min: €%f, Max: €%f" %(min(player_values),max(player_values)))

# Second smallest unique value
s1 = list(set(sorted(player_values)))
s2 = sorted(s1)
print("Min:", s2[1])
print("Max:", s2[len(s2)-1])



