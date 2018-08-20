# Sanitizing and Cleaning Up Text

s = 'pýtĥöñ\fis\tawesome\r\n'
s

remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None    # Deleted
}

a = s.translate(remap)
a


import unicodedata
import sys
sys.maxunicode
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
b
b.translate(cmb_chrs)


digitmap = { c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}

len(digitmap)
# Arabic digits
x = '\u0661\u0662\u0663'
x
x.translate(digitmap)


a
b = unicodedata.normalize('NFD', a)
b
b.encode('ascii', 'ignore').decode('ascii')


# Discussion

# on text processing; the simpler, the faster.
def clean_space(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s

