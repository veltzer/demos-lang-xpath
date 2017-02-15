#!/usr/bin/python3

"""
This is a demo of how to navigate the xml tree in lxml
"""

import lxml.etree # for parse

parsed = lxml.etree.parse('demo_navigation.xml')

# lets get the root element
root = parsed.getroot()

# do something with all children, all elements are lists
for child in root:
    print(child.tag)
print("================")

# all elements of a tag
for child in root.iter("a"):
    print(child.text)
print("================")

# get the single element of a tag
print(list(root.iter("single"))[0].text)
print("================")

for x in root.findall("single"):
    print(x.text)
print("================")
