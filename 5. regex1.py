# Event: Phase 3 NW3 (Jan. 2022)
# Author: PDST 
import re

text1 = "THERE are 99 RED balloons"
print(re.sub('[0-9]', '', text1)) # remove digits
print(re.sub('[A-Z]', '', text1)) # remove uppercase
print(re.sub('[A-Z0-9]', '', text1)) # remove uppercase and digits
print(re.sub('[^a-z]', '', text1)) # leave lowercase
print(re.sub('[^a-zA-Z ]', '', text1)) # leave letters and spaces
print(re.sub('[^a-zA-Z0-9]', ' ', text1)) # leave letters and digits
print(re.sub(r'\b\w{1,4}\b', '', text1)) # remove words of length 1-3

text1 = "$%**$%joe*&$%^&"
print(re.sub('[^a-zA-Z0-9]', '', text1))

# using re to validate
phone_nos = ["0861234567", "1234567"]
for phone_no in phone_nos:
    # 1) Begins with 083, 086 or 087
    # 2) Then contains 8 digits
    if re.match("(083|086|087)?[0-9]{7}", phone_no):
        print(phone_no, "Match")
    else:
        print(phone_no, "No Match")


'''
# 1) Begins with 0 or 91 
# 2) Then contains 7 or 8 or 9. 
# 3) Then contains 9 digits
    
if re.match("(0|91)?[7-9][0-9]{9}", "07111111111"):
    print("Match")
else:
    print("No Match")

print( re.match("(0|91)?[7-9][0-9]{9}", "07111111111") )
'''


'''
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)


if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")
'''