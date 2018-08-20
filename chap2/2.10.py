# Working with Unicode Characters in Regular Expressions

import re
num = re.compile(r'\d+')
# ASCII digit
num.match('123')
# Arabic digit
num.match('\u0661\u0662\u0663')

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
arabic


pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s)         # Matches
pat.match(s.upper()) # Doesn't match
s.upper()            # Case folds
