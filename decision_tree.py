"""
LAB 5: Decision trees
Course: AI
Author: Eduardo Vaca
"""

class Attribute(object):
    """Class that represents an attribute from the dataset
    """

    def __init__(self, att_str):
        parts = att_str.split('{')
        self.name, values_str = parts[0].split(' ')[1].strip(), parts[1]
        for ch in ['}', ' ']:
            values_str = values_str.replace(ch, '')
        self.values = values_str.split(',')

    def __str__(self):
        return '{}: {}'.format(self.name, self.values)


class Dataset(object):
    """Class that represents the dataset tables with list of lists
    """
    def __init__(self):
        self.dataset = []

    def add_data(self, data_str):
        """Adds new data row to the dataset
        """
        self.dataset.append(data_str.split(','))


def read_attributes():
    """Reads and obtain attributes of the data
    RETURNS:
    - dictionary of index->attribute
    """
    value = input()
    attributes = {}
    while '@attribute' not in value:
        value = input()
    count = 0
    while '@attribute' in value:
        attribute = Attribute(value)
        attributes[count] = attribute
        count += 1
        value = input()
    return attributes

def read_data():
    """Reads and creates the dataset tables
    RETURNS:
    - New dataset
    """
    value = input()
    while '@data' in value:
        value = input()
    while '%' in value:
        value = input()
    dataset = Dataset()
    while True:
        dataset.add_data(value)
        try:
            value = input()
        except EOFError:
            return dataset
    return dataset

def main():
    """Main program
    """
    attributes = read_attributes()
    for k, v in attributes.items():
        print('{} -> {}'.format(k, v))
    dataset = read_data()
    print(dataset.dataset)

if __name__ == '__main__':
    main()

