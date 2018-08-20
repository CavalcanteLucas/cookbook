# Handling HTML and XML Entities in Text

s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))

# Disable escaping of quotes
print(html.escape(s, quote=False))


s = 'Spicy Japaleño'
s.encode('ascii', errors='xmlcharrefreplace')

s = 'Spicy &quot;Japale&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
p.unescape(s)

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
unescape(t)
