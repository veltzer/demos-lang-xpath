#!/usr/bin/python3

'''
This is an example of how to read XML in python using the built in
lxml.etree module.

Note that there are two libraries in python: xml.etree and lxml.etree.
use the latter, and beware of mixing them.

References:
- http://stackoverflow.com/questions/2755950/how-to-use-regular-expression-in-lxml-xpath
- http://stackoverflow.com/questions/22718101/pretty-print-option-in-tostring-not-working-in-lxml
- http://lxml.de/tutorial.html
- http://stackoverflow.com/questions/23727696/list-can-not-be-serialized-error-when-using-xpath-with-lxml-etree
'''

import lxml.etree # for parse

root = lxml.etree.parse('demo_misc.xml')

# this means that we can use regular expression functions like 'match'
# by specifying 're:match' in our xpath expressions
ns = lxml.etree.FunctionNamespace("http://exslt.org/regular-expressions")
ns.prefix = 're'

# for bar at any level
for e in root.xpath('//bar'):
    print(e.get('title'))

# look for any person whose text contains "Mark"
e_a = root.xpath('//person[contains(text(),"Mark")]')
for x in e_a:
    print(lxml.etree.tostring(x, pretty_print=True, encoding='unicode').strip())

# look for any person whose text starts with "Mark"
e_a = root.xpath('//person[starts-with(text(),"Mark")]')
for x in e_a:
    print(lxml.etree.tostring(x, pretty_print=True, encoding='unicode').strip())

# look for any person whose text starts with "Mark" (regexp)
# this will work even without the registration of the namespace above...
#e_a = root.xpath('//person[re:match(text(),"^Mark")]', namespaces={"re": "http://exslt.org/regular-expressions"})
e_a = root.xpath('//person[re:match(text(),"^Mark")]')
for x in e_a:
    print(lxml.etree.tostring(x, pretty_print=True, encoding='unicode').strip())

# look for a span whose id is productTitle and return its text
e_a = root.xpath('//span[@id="productTitle"]/text()')[0].strip()
print('the text you want stripped is [{}]'.format(e_a))
#for x in e_a:
#   print(lxml.etree.tostring(x, pretty_print=True, encoding='unicode').strip())

# This example shows that if xpath cannot find elements that match your expression
# then you just get an empty list
e_a = root.xpath('//span[@id="this does not exist"]/text()')
assert len(e_a)==0
assert type(e_a) is list
