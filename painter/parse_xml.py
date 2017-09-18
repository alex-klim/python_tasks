import xml.etree.ElementTree as ET


tree = ET.parse('menu.xml')
root = tree.getroot()

for child in root:
  print(child.tag, ":")
  for childd in child:
    print(childd.tag)