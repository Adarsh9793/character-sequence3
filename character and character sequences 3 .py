# [a,e,i,o,u] - matches a single characterfrom the set.
#[^xyz] - matches a single character .
# [a-z 0-9] - matches a single character from the set of range.
# {} - set of characters can include a range

'''import re
string = "Hello Worlddd 123"
pattern = "World{3}"
print(re.findall(pattern, string))  # Finds all occurrences of 'python' followed by exactly three 'n's in the string'''

import re

string = "from HackerRank import @ re"
pattern = "([^ ]*)"
print(re.findall(pattern, string))  # Finds all occurrences of non-space characters in the string