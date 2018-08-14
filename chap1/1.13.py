# Sorting a List of Dictionaries by a Common Key

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003,},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002,},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001,},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004,},
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# DISCUSSION

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lname = sorted(rows, key=lambda r: r['lname'])
print(rows_by_lname)

min(rows, key=itemgetter('uid'))
max(rows, key=itemgetter('uid'))


