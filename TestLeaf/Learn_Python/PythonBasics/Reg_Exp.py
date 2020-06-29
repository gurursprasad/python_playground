import re

test_string = "There are 2a apples for 4 persons"

print("The original string : " + test_string)
temp = re.findall(r'\d+', test_string)
res = list(map(int, temp))

print("The numbers list is : " + str(res))
