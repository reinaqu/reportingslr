# -*- coding: utf-8 -*-
'''
Created on 29 jun. 2020

@author: reinaqu_2
'''
from commons import *

BLOCKCHAIN ="Blockchain platform"
ID_LANG ="Language (ids studies)"

def count_languages_by_blockchain(languages, filter=None):
    return count_by_property(languages, lambda l:l[BLOCKCHAIN], filter)