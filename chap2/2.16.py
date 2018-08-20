# Reformatting Text to a Fixed Number of Columns

words = [
    "look", "into", "my", "eyes", "look", "into", "my", "eyes",
    "the", "eyes", "the", "eyes", "the", "eyes", "not", "around", "the",
    "eyes", "don't", "look", "around", "the", "eyes", "look", "into",
    "my", "eyes", "you're", "under"
]

s = ' '.join(words)
import re
s = re.sub('eyes', 'eyes,', s)
s = re.sub('under', 'under.', s)
s

w = s.split(' ')
w[0] = w[0].capitalize()
w

s = ' '.join(w)
s


import textwrap
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent='    '))


# Discussion

import os
os.get_terminal_size().columns