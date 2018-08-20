# Specifying a Regular Expression for the Shortest Match

import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1)
text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2)

str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)