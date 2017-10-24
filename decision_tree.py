"""
LAB 5: Decision trees
Course: AI
Author: Eduardo Vaca
"""

class Attribute:
    
    def __init__(self, att_str):
        parts = att_str.split('{')
        self.name, values_str = parts[0].split(' ')[1].strip(), parts[1]
        for ch in ['}', ' ']:
            values_str = values_str.replace(ch, '')
        self.values = values_str.split(',')

    def __str__(self):
        return '{}: {}'.format(self.name, self.values)


def read_attributes():
    """Reads and obtain attributes of the data
    RETURNS:
    - dictionary of name->attribute
    """
    value = input()
    attributes = {}
    while '@attribute' not in value:
        value = input()
    while '@attribute' in value:
        attribute = Attribute(value)
        attributes[attribute.name] = attribute
        value = input()
    return attributes

def main():
    """Main program
    """
    attributes = read_attributes()
    for k, v in attributes.items():
        print('{} -> {}'.format(k, v))

if __name__ == '__main__':
    main()

