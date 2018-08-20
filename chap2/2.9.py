# Normalizing Unicode Text to a Standard Representation

s1 = 'Spice Jalape\u00f1o'
s2 = 'Spice Jalapen\u0303o'
s1
s2
s1 == s2
len(s1)
len(s2)


import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
t1 == t2
t1
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
t3 == t4
print(ascii(t3))


s = '\ufb01' # A single character
s
unicodedata.normalize('NFD', s)

# Notice the combined letters are broken apart here
unicodedata.normalize('NFKD', s)
unicodedata.normalize('NFKC', s)


# Discussion
t1 = unicodedata.normalize('NFD', s1)
t1
''.join(c for c in t1 if not unicodedata.combining(c))