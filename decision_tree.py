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


def entropy(values):
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

def information_gain(dataset, prev_entropy, attribute, index):
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
        results = [data[-1] for data in dataset if data[index] == value]
        ig -= len(results)/len(dataset)*entropy(results)
    return ig

def best_attribute(dataset, prev_entropy, attributes):
    """Get the best attribute to split on
    PARAMS:
    - prev_entropy : previous entropy gotten
    RETURNS:
    - index of the best attribute to split
    """
    attr_ig = {i: information_gain(dataset, prev_entropy, attributes[i], i) for i in range(len(dataset[0])-1)}
    return max(attr_ig.keys(), key=(lambda k: attr_ig[k]))

def split_on_attribute(dataset, attribute_index, attribute):
    """Split dataset based on attribute
    PARAMS:
    - dataset : dataset to be splitted
    - attribute_index : index of the attribute to be splitted
    - attribute : attribute used to split
    RETURNS:
    - list of split datasets
    """
    split_datasets = []
    for value in attribute.values:
        split_datasets.append([data for data in dataset if data[attribute_index] == value])
    return split_datasets

def id3(dataset, attributes, depth):
    """ID3 Algorithm for decision trees
    Instead of buidling the structure, prints it
    """
    depth += 1
    ds_entropy = entropy([ds[i] for ds in dataset for i in range(len(ds)) if i == len(attributes)-1 ])
    if ds_entropy == 0:
        print(''.join([' ' for _ in range(depth*2)]) + 'ANSWER: ' + dataset[0][-1])
        return
    best_attr = best_attribute(dataset, ds_entropy, attributes)
    attr_index = 0
    for ds in split_on_attribute(dataset, best_attr, attributes[best_attr]):
        if ds:
            print(''.join([' ' for _ in range(depth*2)]) + attributes[best_attr].name + ': ' + attributes[best_attr].values[attr_index])
            id3(ds, attributes, depth)
        attr_index += 1

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
    dataset = []
    while True:
        dataset.append(value.split(','))
        try:
            value = input()
        except EOFError:
            return dataset
    return dataset

def main():
    """Main program
    """
    attributes = read_attributes()
    dataset = read_data()
    id3(dataset, attributes, -1)

if __name__ == '__main__':
    main()

