# Writing to a File That Doesn't Alrady Exist

with open('somefile', 'wt') as f:
    f.write('Hello\n')

with open('somefile', 'xt') as f:
    f.write('Hello\n')


# Discussion

import os
if not os.path.exists('somefie'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')
