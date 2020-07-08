# -*- coding: utf-8 -*-
'''
Created on 8 jul. 2020

@author: reinaqu_2
'''
from sc_utils import *
from csvbib_utils import *

def generate_languages_by_blockchain(languages_list, filter=None):
    
    dict=group_languages_names_by_blockchain(languages_list, filter)
    txt='''\\textsf{{{0}}} & {1} \\\\ 
            \\tabucline{{1-2}}'''
    for blockchain, languages in dict:
        str_langs= str(languages).replace("[","").replace("]","").replace("'","")
        print(txt.format(blockchain, str_langs))
        
def generate_venues_ordered_by_num_studies(studies, limit=None):
    
    dict=group_studies_by_venue(studies)
    #      1 &\textsf{Computing Research Repository (CoRR)}  & Other & 5 \\ 
    lista=sorted(dict.items(), key=lambda item:(len(item[1]),item[0]), reverse=True)
    if limit!=None:
        lista=lista[:limit]
    txt='''{} & \\textsf{{{}}} & {} & {}\\\\'''
    i=1
    for venue, list_studies in lista:
        type=list_studies[0][TYPE].lower().replace("paper","").strip()
        print(txt.format(i,venue, type, len(list_studies)))
        i=i+1