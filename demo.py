#!/usr/bin/python3

'''
This is an example of how to read XML in python using the built in
lxml.etree module.

Note that there are two libraries in python: xml.etree and lxml.etree.
use the latter, and beware of mixing them.
'''

import lxml.etree # for parse

root = lxml.etree.parse('demo.xml')

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
e_a = root.xpath('//person[re:match(text(),"^Mark")]', namespaces={"re": "http://exslt.org/regular-expressions"})
for x in e_a:
    print(lxml.etree.tostring(x, pretty_print=True, encoding='unicode').strip())
