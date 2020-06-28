# -*- coding: utf-8 -*-
'''
Created on 28 jun. 2020

@author: reinaqu_2
'''
import pandas as pd
from csvbib_utils import *

def create_references_by_year_dataframe(references):
    dict_wl = count_references_by_year(references, lambda r:is_white_literature(r))
    dict_gl = count_references_by_year(references, lambda r:is_grey_literature(r))

    union =dict_wl.keys() | dict_gl.keys()
    years = sorted(union)
    wl_count=[]
    gl_count=[]
    for year in years:
        wl_count.append(dict_wl.get(year,0))
        gl_count.append(dict_gl.get(year,0))
        
    d ={'year': years,
        'white literature': wl_count,
        'grey literature':gl_count}
    return pd.DataFrame(data=d)