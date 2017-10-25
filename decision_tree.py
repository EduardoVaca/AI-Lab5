"""
LAB 5: Decision trees
Course: AI
Author: Eduardo Vaca
"""
import math

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

    def entropy(self, values):
        """Compute the entropy of an attribute from dataset
        PARAMS:
        - index : index of the attribute to calculate entropy
        RETURNS:
        - entropy of attribute
        """
        attributes = {}
        for val in values:
            attributes[val] = attributes.get(val, 0) + 1
        result = 0
        for _, v in attributes.items():
            result -= v/len(values)*math.log(v/len(values), 2)
        return result

    def information_gain(self, prev_entropy, attribute, index):
        """Compute information gain of a given attribute
        PARAMS:
        - prev_entropy : previous entropy gotten
        - attribute : Attribute object to obtain its information gain
        - index : index of that attribute in each row of dataset
        RETURN:
        - information gain value
        """
        ig = prev_entropy
        for value in attribute.values:
            results = [data[-1] for data in self.dataset if data[index] == value]
            ig -= len(results)/len(self.dataset)*self.entropy(results)
        return ig

    def best_attribute(self, prev_entropy, attributes):
        """Get the best attribute to split on
        PARAMS:
        - prev_entropy : previous entropy gotten
        RETURNS:
        - index of the best attribute to split
        """
        attr_ig = {i: self.information_gain(prev_entropy, attributes[i], i) for i in range(len(self.dataset[0])-1)}
        return max(attr_ig.keys(), key=(lambda k: attr_ig[k]))


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
    ds_entropy = dataset.entropy([ds[i] for ds in dataset.dataset for i in range(len(ds)) if i == len(attributes)-1 ])
    print(ds_entropy)
    print('should split attr: {}'.format(dataset.best_attribute(ds_entropy, attributes)))

if __name__ == '__main__':
    main()

