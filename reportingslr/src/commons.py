# -*- coding: utf-8 -*-
'''
Created on 29 jun. 2020

@author: reinaqu_2
'''
import csv
from csv import DictReader
from collections import Counter, defaultdict

def load_report_csv(filename,id_name,enc='utf-8'):
    ''' Read the csv springer file and returns a dictionary with the ID_PAPER as key and
        a DicReader entry as values 
    '''
    with open(filename,encoding=enc) as f:
        lector = csv.DictReader(f,delimiter=';')
        return {record[id_name]:record for record in lector}


def count_by_property(items, property, filter=None):
    if (filter == None):
        types=[property(item_tuple) for item_tuple in items.values()]
    else:
        types=[property(item_tuple) for item_tuple in items.values() if filter(item_tuple)]
    return Counter(types)

def normalize(s):
    return s.strip().lower().capitalize()