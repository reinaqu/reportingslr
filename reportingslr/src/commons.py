# -*- coding: utf-8 -*-
'''
Created on 29 jun. 2020

@author: reinaqu_2
'''
import csv
from csv import DictReader
from collections import Counter, defaultdict
from _collections import OrderedDict

def load_report_csv(filename,id_name,enc='utf-8'):
    ''' Read the csv springer file and returns a dictionary with the ID_PAPER as key and
        a DicReader entry as values 
    '''
    with open(filename,encoding=enc) as f:
        lector = csv.DictReader(f,delimiter=';')
        return {record[id_name].strip():record for record in lector}


def count_by_property(items, property, filter=None):
    if (filter == None):
        types=[property(item_tuple) for item_tuple in items.values()]
    else:
        types=[property(item_tuple) for item_tuple in items.values() if filter(item_tuple)]
    return Counter(types)

def group_by_property(items, property, filter=None):
    dict=defaultdict(list)
    for item_tuple in items.values():
        if filter ==None or filter(item_tuple):
            dict[property(item_tuple)].append(item_tuple)
    return dict

def count_by_property_pairs(items, property1,property2, filter=None):
    if (filter == None):
        types=[(property1(item_tuple), property2(item_tuple)) for item_tuple in items.values()]
    else:
        types=[(property1(item_tuple), property2(item_tuple)) for item_tuple in items.values() if filter(item_tuple)]
    return Counter(types)

def create_dict(items, function_key, function_value, filter=None):
    if (filter == None):
        dict= { function_key(item_tuple): function_value(item_tuple) for item_tuple in items.values()}
    else:
        dict={ function_key(item_tuple): function_value(item_tuple) for item_tuple in items.values() if filter(item_tuple)}
    return OrderedDict(dict)

def unzip_pairs_dict(dict_pairs):
    '''
    INPUT:
        dict_pairs:  (k1,k2):value  Dictionary whose keys are sequences of two elements.
    OUTPUT:
        - list1: list with all the k1 elements
        - list2: list with all the k2 elements
        - list3: list with all the value elements.
    Example:
        Input: {(k1,a1): v1, (k1,a2):v2, (k2,a1):v3, (k2,a2):,v4}
        Output: 
            list_1 = {k1,k1,k2,k2}
            list_2 = {a1,a2,a1,a2}
            list_3 = {v1,v2,v3,v4}
    '''
    list_1=[]
    list_2 =[]
    list_3 =[]
    for item in dict_pairs.items():
        list_1.append(item[0][0])
        list_2.append(item[0][1])
        list_3.append(item[1])
    return list_1, list_2, list_3    

def normalize(s):
    return s.strip().lower().capitalize()