import xml.etree.ElementTree as ET


tree = ET.parse('menu.xml')
root = tree.getroot()

def cli(node):
    #while True:
    print('im in cli')
    print(node.attrib.get('prompt'))

    action = input()

    if node.attrib.get('function'):
            print(node.attrib.get('function'))
    else:
        for child_of_node in node:
            if child_of_node.tag == 'siblings':
                for sibling in child_of_node:
                    if sibling.tag == action:
                        yield cli(sibling)

        yield cli(node)
print('something')
print(root.tag)
cli(root)