# -*- coding: utf-8 -*-
'''
Created on 28 jun. 2020

@author: reinaqu_2
This module contains functions to create dataframes that are
related to slrs or mapping studies in general
'''
import pandas as pd
from csvbib_utils import *

def create_dataframe_studies_by_literature_type(studies):
    '''
    INPUT:
        - studies: Dict{id_paper:DictReaderEntry(reference)}
    OUTPUT:
        - dataframe: panda.Dataframe with the following structure:
           * index: type of literature (white or grey)
           * number of studies: number of studies per literature type
    '''

    dict_lit_types= count_studies_by_literature_type(studies)
    
    types, studies_count = zip(*dict_lit_types.items())
    d ={'number of studies': studies_count}
    return pd.DataFrame(data=d, index=types)

def create_dataframe_studies_by_type(studies,filter=None):
    '''
    INPUT:
        - studies: Dict{id_paper:DictReaderEntry(reference)}
    OUTPUT:
        - dataframe: panda.Dataframe with the following structure:
           * index: type of literature (white or grey)
           * number of studies: number of studies per literature type
    '''
    dict=count_studies_by_publication_type(studies,filter)
    sorted_items =sorted(dict.items(),key=lambda it:it[1], reverse=True)
        
    types, studies_count = zip(*sorted_items)
    d ={'number of studies': studies_count}
    return pd.DataFrame(data=d, index=types)

def create_dataframe_studies_by_year(studies):
    '''
    INPUT:
        - studies: Dict{id_paper:DictReaderEntry(reference)}
    OUTPUT:
        - dataframe: panda.Dataframe with the following structure:
           * year: year of publication of the study
           * white literature: number of studies of white literature per year
           * grey literature: number of studies of grey literature per year
           * total: total number of studies per year
    '''
    dict_wl = count_studies_by_year(studies, lambda s:is_white_literature(s))
    dict_gl = count_studies_by_year(studies, lambda s:is_grey_literature(s))

    years = sorted(dict_wl.keys() | dict_gl.keys())
    wl_count=[]
    gl_count=[]
    l_count =[]
    for year in years:
        wl_count.append(dict_wl.get(year,0))
        gl_count.append(dict_gl.get(year,0))
        l_count.append(dict_wl.get(year,0)+dict_gl.get(year,0))
        
    d ={'year': years,
        'white literature': wl_count,
        'grey literature':gl_count,
        'total': l_count}
    return pd.DataFrame(data=d)

def create_dataframe_studies_by_country(studies):
    dict = count_studies_by_country(studies, lambda s:not is_country_null(s))

    countries, studies_count = zip(*dict.items())
    d ={'countries': countries,
        'number of studies': studies_count}
    return pd.DataFrame(data=d)


def create_dataframe_studies_quality(studies, filter=None):
    dict_qualities = calculate_studies_quality(studies, filter)
    
    studies_ids = dict_qualities.keys()
    studies_information_quality,studies_publication_quality = zip(*dict_qualities.values())
          
    d ={'information quality':studies_information_quality,
        'publication quality': studies_publication_quality}
    return pd.DataFrame(data=d, index=studies_ids)

    