#parsing/parser:
#xml: extensible markup language
#rss: rich site summary

import xml.etree.ElementTree as ET

def extract(file):
    tree= ET.parse(file)
    root= tree.getroot() #the first tag/ annotation

data=[]
for data1 in root.findall('307')    