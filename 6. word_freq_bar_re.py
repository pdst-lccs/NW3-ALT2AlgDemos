# Event: Phase 3 NW3 (Jan. 2022)
# Author: PDST 
# A program to visualise the most common words in a file
from matplotlib import pyplot as plt
from collections import Counter
import re

# IMPORTANT: Make sure book.txt exists in runtime directory
bookFile = open("book.txt","r") # Open the file
text = bookFile.read() # read the file
bookFile.close() # close the file

text = re.sub('[^a-zA-Z0-9 \n]', ' ', text)
text = re.sub(r'\b\w{1,4}\b', '', text)

text_list = text.split() # create a list

# use counter to return the most common words
# format is .... [('the', 1507), ('and', 714), etc
most_common_words = Counter(text_list).most_common(10)

words = [] # an empty list of words
word_count = [] # an empty list of counts

# Build up the lists
for word, count in most_common_words:
    words.append(word) # append the word to the words list
    word_count.append(count)
    
# Create the chart
plt.bar(words, word_count)
plt.title("Word Count Demo") # graph title
plt.ylabel("Frequency") # label the y-axis
# put the words on the x-axis
plt.xticks(range(len(words)), words, rotation=45)
plt.show() # display the chart

# Alternative way to build the list of words from the list of tuple ini most_common_words ...
# most_common_words: [('the', 1507), ('and', 714), ('to', 703), ('a', 606), ('of', 490), ('she', 484), ('said', 416), ('it', 346), ('in', 345), ('was', 328)]
# words = [most_common_words[0] for most_common_words in lst]
# or 
# words = list(zip(*most_common_words)[0])


