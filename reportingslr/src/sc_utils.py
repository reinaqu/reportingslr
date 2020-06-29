# -*- coding: utf-8 -*-
'''
Created on 29 jun. 2020

@author: reinaqu_2
'''
from commons import *

BLOCKCHAIN ="Blockchain platform"
ID_LANG ="Language (ids studies)"
IMPLEMENTATION_KIND= "Kind:Implementation"
SPECIFICATION_KIND= "Kind:Specification"
ACADEMIA_CONTEXT="Academia"
INDUSTRY_CONTEXT="Industry"
STANDALONE_TYPE ="DSL Type:Standalone"
EXTENSION_TYPE="DSL Type:Extension"
IMPLEMENTATION_LABEL="Implementation"
SPECIFICATION_LABEL="Specification"
ACADEMIA_LABEL="Academia"
INDUSTRY_LABEL="Industry" 
STANDALONE_LABEL="Standalone"
EXTENSION_LABEL="Extension"

def count_languages_by_blockchain(languages, filter=None):
    return count_by_property(languages, lambda l:l[BLOCKCHAIN], filter)

def count_languages_by_context_and_kind(languages, filter=None):
    return count_by_property_pairs(languages, lambda l:language_context(l), lambda l:language_kind(l),  filter)

def count_languages_by_kind_and_type(languages, filter=None):
    return count_by_property_pairs(languages, lambda l:language_kind(l), lambda l:language_type(l),  filter)

def count_languages_by_context_and_type(languages, filter=None):
    return count_by_property_pairs(languages, lambda l:language_context(l), lambda l:language_type(l),  filter)

def language_kind (language):
    if language[IMPLEMENTATION_KIND]=='Y' and  language[SPECIFICATION_KIND]=='N':
        res=IMPLEMENTATION_LABEL
    elif language[IMPLEMENTATION_KIND]=='N' and  language[SPECIFICATION_KIND]=='Y':
        res=SPECIFICATION_LABEL
    return res

def language_context (language):
    if language[ACADEMIA_CONTEXT]=='Y' and  language[INDUSTRY_CONTEXT]=='N':
        res=ACADEMIA_LABEL
    elif language[ACADEMIA_CONTEXT]=='N' and  language[INDUSTRY_CONTEXT]=='Y':
        res=INDUSTRY_LABEL
    return res

def language_type(language):
    if language[EXTENSION_TYPE]=='Y' and  language[STANDALONE_TYPE]=='N':
        res=EXTENSION_LABEL
    elif language[EXTENSION_TYPE]=='N' and  language[STANDALONE_TYPE]=='Y':
        res=STANDALONE_LABEL
    return res