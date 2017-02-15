#!/usr/bin/python3

'''
This is an example of how to deal with namespace issues when parsing XML
in python
'''

import lxml.etree # for parse

root = lxml.etree.parse('demo_namespace.xml')

# this will find nothing as we are searching without a namespace
list_of_bars = root.xpath('//bar')
assert(len(list_of_bars)==0)

# lets search with the right namespace
namespace_map = {
        "x": "http://fubar",
}
list_of_bars = root.xpath('//x:bar', namespaces=namespace_map)
assert(len(list_of_bars)>0)

# we could also register the namespace so we don't need to always
# search with the namespaces= parameter
# this does not work currently...
"""
lxml.etree.register_namespace("bar", "x")
list_of_bars = root.xpath('//x:bar')
assert(len(list_of_bars)>0)
"""
