# Event: Phase 3 NW3 (Jan. 2022)
# Author: PDST 
# A simple program to calculate and display averages
from statistics import *

# Initialise a list of values
values = [2,3,5,2,4] 

# Compute the 3 averages
arithmetic_mean = mean(values)
median_value = median(values)
modal_value = mode(values)

# Display the answers
print("The mean is ", arithmetic_mean)
print("The median and mode are %d and %d" %(median_value, modal_value))




