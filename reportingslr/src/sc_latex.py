# -*- coding: utf-8 -*-
'''
Created on 8 jul. 2020

@author: reinaqu_2
'''
from sc_utils import *

def generate_languages_by_blockchain(languages_list, filter=None):
    
    dict=group_languages_names_by_blockchain(languages_list, filter)
    txt='''\\textsf{{ {0} }} & {1} \\\\ 
            \\tabucline{{1-2}}'''
    print (txt)
    for blockchain, languages in dict:
        str_langs= str(languages).replace("[","").replace("]","").replace("'","")
        print(txt.format(blockchain, str_langs))