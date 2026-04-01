import xml.etree.ElementTree as ET

data = {}

# open and read file
file = open("data.txt", "r")

for line in file:
    line = line.strip()
    key, value = line.split("=")
    data[key] = value

file.close()

# create root tag
root = ET.Element("Car")

# add data to XML
for key in data:
    child = ET.SubElement(root, key)
    child.text = data[key]

# make XML readable
ET.indent(root)

# save XML file
tree = ET.ElementTree(root)
tree.write("car_data.xml")

print("XML file created successfully")