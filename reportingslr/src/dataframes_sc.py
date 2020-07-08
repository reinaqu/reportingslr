# -*- coding: utf-8 -*-
'''
Created on 29 jun. 2020

@author: reinaqu_2
This module contains functions to create dataframes that are
related to the smart contract domain
'''
import pandas as pd
from sc_utils import *

def create_dataframe_languages_by_blokchain_platform(languages):
    '''
    INPUT:
        - studies: Dict(language: [Dict{id_paper:DictReaderEntry(reference)}])
    OUTPUT:
        - dataframe: panda.Dataframe with the following structure:
           * index: blockain platform
           * number of languages: number of languages per blockchain platform
    '''

    dict_lang_bc= count_languages_by_blockchain(languages, lambda l:is_not_blockchain_null_or_na(l))

    ordered =sorted(dict_lang_bc.items(),key=lambda it:it[1], reverse=True)
    bc_platforms, languages_count = zip(*ordered)
    d ={'number of languages': languages_count}
    return pd.DataFrame(data=d, index=bc_platforms)


def create_dataframe_languages_by_context_and_kind(languages):
    dict_pairs = count_languages_by_context_and_kind(languages)
    
    bc_academia,languages_kind,languages_count = unzip_pairs_dict(dict_pairs)
          
    d ={'kind of language':languages_kind,
        'number of languages': languages_count}
    return pd.DataFrame(data=d, index=bc_academia)

def create_dataframe_languages_by_context_and_type(languages):
    dict_pairs = count_languages_by_context_and_type(languages)
    
    bc_academia,languages_type,languages_count = unzip_pairs_dict(dict_pairs)
          
    d ={'type of language':languages_type,
        'number of languages': languages_count}
    return pd.DataFrame(data=d, index=bc_academia)

def create_dataframe_languages_by_kind_and_type(languages):
    dict_pairs = count_languages_by_kind_and_type(languages)
    
    languages_kind,languages_type,languages_count = unzip_pairs_dict(dict_pairs)
          
    d ={'type of language':languages_type,
        'number of languages': languages_count}
    return pd.DataFrame(data=d, index=languages_kind)


