# -*- coding: utf-8 -*-
'''
Created on 27 may. 2020

@author: reinaqu_2
'''
import csv
from csv import DictReader
from collections import Counter, defaultdict
from commons import *
import logging
from _collections import OrderedDict

ID_PAPER ="ID Paper"
TITLE ="Title"
TYPE = "Type"
YEAR = "Year"
GREY_LITERATURE=["blog", "wiki page", "website", "github page", "white paper"]
WHITE_LITERATURE=["journal paper", "conference paper", "workshop paper","book chapter","report","arxiv", "master thesis", "phd thesis"]
WHITE_LITERATURE_LABEL = "White literature"
GREY_LITERATURE_LABEL = "Grey literature"
UNKNOWN_LABEL = "Unknown"
ISO_CODE='ISO-alpha3 code'
COUNTRY='Zone'

def print_report_items(report_items):
    print("Number of items...", len(report_items))
    for item in report_items.items():
        print(item)
        
def print_items(report_items):
    print("Number of items...", len(report_items))
    for item in report_items:
        print(item)        
        
def group_by_title(studies):       
    dicres = defaultdict(list)
    #Group the studies by title, the values are the paper ID's   
    for ref in studies.items():
        dkey= ref[1][TITLE].lower()
        dicres[dkey].append(ref[0])
    return dicres    

def filter_duplicates(studies):       
    dic = group_by_title(studies)
    #Filter duplicates. Duplicates are those ones that have more than one element in the values list
    dicres = defaultdict(list)
    for item in dic.items():
        if(is_duplicated(studies, item[1])):
            dkey= item[0]
            dicres[dkey].append(item[1])
    return sorted(dicres.items())
    
def is_duplicated(studies, list_ids):
    res = False
    if len(list_ids)>1 and at_least_one_not_mark_as_duplicated(studies, list_ids):
        res=True
    return res

def at_least_one_not_mark_as_duplicated(studies,list_ids):
    return any( not mark_as_duplicated(studies, id) for id in list_ids)

def mark_as_duplicated(studies, id):
    ref_tuple =studies.get(id)
    res= ref_tuple['Status/Selection']=='DUPLICATED'
    if res==False:
        logging.info(id+ref_tuple['Status/Selection']+str(res))
    return res

def count_studies_by_literature_type(studies, filter=None):
    return count_by_property(studies, lambda s:literature_type(s), filter)
    

def count_studies_by_publication_type(studies, filter=None):
    return count_by_property(studies, lambda s:normalize(s[TYPE]), filter)
    
def count_studies_by_year(studies, filter=None):
    c= count_by_property(studies, lambda s:s[YEAR], filter)
    return OrderedDict(sorted(c.items()))


def literature_type(study_tuple):
    type = study_tuple[TYPE].strip().lower()
    if type in WHITE_LITERATURE:
        res=WHITE_LITERATURE_LABEL
    elif type in GREY_LITERATURE:
        res=GREY_LITERATURE_LABEL
    else:
        res=UNKNOWN_LABEL
    return res     
        
def is_white_literature(study_tuple):
    type = study_tuple[TYPE].strip().lower()
    return type in WHITE_LITERATURE

def is_grey_literature(study_tuple):
    type = study_tuple[TYPE].strip().lower()
    return type in GREY_LITERATURE

def count_studies_by_country(studies, filter=None):
    '''
    INPUT: 
        -studies : {Paper ID,{Paper Id: id, Zone: country_name}==>{str,OrderedDict}
    '''
    return count_by_property(studies, lambda s:country(s), filter)

def country(study_dict):
    '''
        INPUT
         study_dict: OrderedDict(('Paper ID':id), ('Zone', Country_name)
    '''
    return study_dict[COUNTRY].strip()
    
