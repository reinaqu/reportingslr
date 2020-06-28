# -*- coding: utf-8 -*-
'''
Created on 27 may. 2020

@author: reinaqu_2
'''
import csv
from csv import DictReader
from collections import Counter, defaultdict
from _sre import ascii_tolower
import logging
from graphicsutils import *

ID_PAPER ="ID Paper"
TITLE = "Title"
TYPE = "Type"
GREY_LITERATURE=["blog", "wiki page", "website", "github page", "white paper"]
WHITE_LITERATURE=["journal paper", "conference paper", "workshop paper","book chapter","report","arxiv", "master thesis", "phd thesis"]
WHITE_LITERATURE_LABEL = "White literature"
GREY_LITERATURE_LABEL = "Grey literature"
UNKNOWN_LABEL = "Unknown"

def load_report_csv(filename):
    ''' Read the csv springer file and returns a dictionary with the ID_PAPER as key and
        a DicReader entry as values 
    '''
    with open(filename) as f:
        lector = csv.DictReader(f,delimiter=';')
        return {record[ID_PAPER]:record for record in lector}



def print_report_items(report_items):
    print("Number of items...", len(report_items))
    for item in report_items.items():
        print(item)
        
def print_items(report_items):
    print("Number of items...", len(report_items))
    for item in report_items:
        print(item)        
        
def group_by_title(references):       
    dicres = defaultdict(list)
    #Group the references by title, the values are the paper ID's   
    for ref in references.items():
        dkey= ref[1][TITLE].lower()
        dicres[dkey].append(ref[0])
    return dicres    

def filter_duplicates(references):       
    dic = group_by_title(references)
    #Filter duplicates. Duplicates are those ones that have more than one element in the values list
    dicres = defaultdict(list)
    for item in dic.items():
        if(is_duplicated(references, item[1])):
            dkey= item[0]
            dicres[dkey].append(item[1])
    return sorted(dicres.items())
    
def is_duplicated(references, list_ids):
    res = False
    if len(list_ids)>1 and at_least_one_not_mark_as_duplicated(references, list_ids):
        res=True
    return res

def at_least_one_not_mark_as_duplicated(references,list_ids):
    return any( not mark_as_duplicated(references, id) for id in list_ids)

def mark_as_duplicated(references, id):
    ref_tuple =references.get(id)
    res= ref_tuple['Status/Selection']=='DUPLICATED'
    if res==False:
        logging.info(id+ref_tuple['Status/Selection']+str(res))
    return res

def count_references_by_type_of_literature(references):
    types=[  literature_type(ref_tuple) for ref_tuple in references.values()]
    return Counter(types)
    
    

def literature_type(ref_tuple):
    type = ref_tuple[TYPE].strip().lower()
    if type in WHITE_LITERATURE:
        res=WHITE_LITERATURE_LABEL
    elif type in GREY_LITERATURE:
        res=GREY_LITERATURE_LABEL
    else:
        res=UNKNOWN_LABEL
    return res     
        
def is_white_literature(ref_tuple):
    type = ref_tuple[TYPE].strip().lower()
    return type in WHITE_LITERATURE

def is_grey_literature(ref_tuple):
    type = ref_tuple[TYPE].strip().lower()
    return type in GREY_LITERATURE

    

if __name__ == "__main__":
    references=load_report_csv("../data/report.0.0.92.csv")
    #print_report_items(references)
    dict_types= count_references_by_type_of_literature(references)
    print(dict_types)
    create_piechart(dict_types)