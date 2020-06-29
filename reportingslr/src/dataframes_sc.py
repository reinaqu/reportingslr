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
        - studies: Dict{id_paper:DictReaderEntry(reference)}
    OUTPUT:
        - dataframe: panda.Dataframe with the following structure:
           * index: type of literature (white or grey)
           * number of studies: number of studies per literature type
    '''

    dict_lang_bc= count_languages_by_blockchain(languages)

    ordered =sorted(dict_lang_bc.items(),key=lambda it:it[1], reverse=True)
    bc_platforms, languages_count = zip(*ordered)
    d ={'number of languages': languages_count}
    return pd.DataFrame(data=d, index=bc_platforms)
