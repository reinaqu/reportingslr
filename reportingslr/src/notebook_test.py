# -*- coding: utf-8 -*-
'''
Created on 28 jun. 2020

@author: reinaqu_2
'''
from csvbib_utils import *
from graphics_utils import *
from dataframes import *

if __name__ == "__main__":
    references=load_report_csv("../data/report.0.0.92-utf8.csv",)
    #print_report_items(references)
    dict_lit_types= count_references_by_literature_type(references)
    print(dict_lit_types)
    #create_piechart(dict_lit_types)
    dict_pub_type=count_references_by_publication_type(references)
    print(dict_pub_type)
    #create_piechart(dict_pub_type)
    
    dict_pub_type_wl=count_references_by_publication_type(references,lambda r:is_white_literature(r))
    print(dict_pub_type_wl)
    #create_piechart(dict_pub_type_wl)
  
    dict_pub_type_gl=count_references_by_publication_type(references,lambda r:is_grey_literature(r))
    print(dict_pub_type_gl)
    #create_piechart(dict_pub_type_gl)
    
    dict_pub_year = count_references_by_year(references)
    print(dict_pub_year)
  
    dict_pub_year_wl = count_references_by_year(references,lambda r:is_white_literature(r))
    print(dict_pub_year_wl)
  
    dict_pub_year_gl = count_references_by_year(references,lambda r:is_grey_literature(r))
    print(dict_pub_year_gl)
    
    df = create_references_by_year_dataframe(references)
    col_names=['white literature','grey literature']
    colours =['orange','grey']
    markers =[MARKER_SQUARE,MARKER_CIRCLE]
    create_line_plot_multiple_colums(df,'year', col_names, colours ,markers)