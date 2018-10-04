# Reading and Writing Compressed Datafiles

text_in = "this is a text"

# gzip compression
import gzip
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text_in)

with gzip.open('somefile.gz', 'rt') as f:
    text_out_gz = f.read()

# bz2 compression
import gzip
with gzip.open('somefile.bz2', 'wt') as f:
    f.write(text_in)

with gzip.open('somefile.bz2', 'rt') as f:
    text_out_bz2 = f.read()


# Discussion

f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text_disc = g.read()

print(text_disc)