# -*- coding: utf-8 -*-
'''
Created on 28 jun. 2020

@author: reinaqu_2
'''
from csvbib_utils import *
from graphics_utils import *
from dataframes import *

if __name__ == "__main__":
    studies=load_report_csv("../data/report.0.0.92-utf8.csv",)
    #print_report_items(studies)
    df= create_dataframe_studies_by_literature_type(studies)
    print(df)
    create_piechart(df,'number of studies')
   
    df=create_dataframe_studies_by_type(studies,labels=False)
    print(df)
    create_piechart(df, 'number of studies')
    
    df=create_dataframe_studies_by_type(studies,lambda s:is_white_literature(s))
    print(df)
    create_piechart(df, 'number of studies')
    
    df=create_dataframe_studies_by_type(studies,lambda s:is_grey_literature(s))
    print(df)
    create_piechart(df, 'number of studies')
    
     
    dict_pub_year = count_studies_by_year(studies)
    print(dict_pub_year)
  
    dict_pub_year_wl = count_studies_by_year(studies,lambda s:is_white_literature(s))
    print(dict_pub_year_wl)
  
    dict_pub_year_gl = count_studies_by_year(studies,lambda s:is_grey_literature(s))
    print(dict_pub_year_gl)
    
    df = create_dataframe_studies_by_year(studies)
    col_names=['white literature','grey literature']
    colours =['orange','grey']
    markers =[MARKER_SQUARE,MARKER_CIRCLE]
    create_line_plot_multiple_colums(df,'year', col_names, colours ,markers)