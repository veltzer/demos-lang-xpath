#!/usr/bin/python3

'''
This is an example of how to use xpath when you have a full path
'''

import lxml.etree # for parse

root = lxml.etree.parse('demo_full_path.xml')

# for bar at any level
for e in root.xpath('/html/head/title'):
    print(e.text)
