# -*- coding: utf-8 -*-
'''
Created on 28 jun. 2020

@author: reinaqu_2
'''
from graphics_utils import *
from dataframes import *
from commons import *
from sc_utils import *
from sc_latex import *

from dataframes_sc import create_dataframe_languages_by_blokchain_platform,\
    create_dataframe_languages_by_context_and_kind,\
    create_dataframe_languages_by_context_and_type,\
    create_dataframe_languages_by_kind_and_type
import locale
if __name__ == "__main__":
    studies=load_report_csv("../data/report.0.0.97.csv",ID_PAPER, enc='cp1252')
 #   languages_clas=load_report_csv("../data/languages_classification.csv",'ID Language')
    studies_country = load_report_csv("../data/publicationsPerCountry.csv",'Paper ID')
    MAP_FILE='../data/countries.geojson'
     
    #print_report_items(studies)
#     df= create_dataframe_studies_by_literature_type(studies)
#     print(df)
#     create_piechart(df,'number of studies')
#      
#     df=create_dataframe_studies_by_type(studies)
#     print(df)
#     create_piechart(df, 'number of studies', y_axis_label=False)
#        
#     df=create_dataframe_studies_by_type(studies,lambda s:is_white_literature(s))
#     print(df)
#     create_piechart(df, 'number of studies', y_axis_label=False)
#        
#     df=create_dataframe_studies_by_type(studies,lambda s:is_grey_literature(s))
#     print(df)
#     create_piechart(df, 'number of studies', y_axis_label=False)
#        
#         
#     dict_pub_year = count_studies_by_year(studies)
#     print(dict_pub_year)
#      
#     dict_pub_year_wl = count_studies_by_year(studies,lambda s:is_white_literature(s))
#     print(dict_pub_year_wl)
#      
#     dict_pub_year_gl = count_studies_by_year(studies,lambda s:is_grey_literature(s))
#     print(dict_pub_year_gl)
#        
#     df = create_dataframe_studies_by_year(studies)
#     col_names=['white literature','grey literature']
#     colours =['orange','grey']
#     markers =[MARKER_SQUARE,MARKER_CIRCLE]
#     print(df)
#     create_line_plot_multiple_colums(df,'year', col_names, colours ,markers)
#       
    
     
    languages = studies_by_language(studies)
#     print(count_languages_by_blockchain(languages))
#     generate_languages_by_blockchain(languages,lambda b:not is_blockchain_null(b))
  
#     df = create_dataframe_languages_by_blokchain_platform(languages)
#     print(df)
#     create_bar(df, BLOCKCHAIN)
#     print(languages)
     
#     df=create_dataframe_languages_by_context_and_kind(languages)
#     create_stacked_bar(df,'kind of language','number of languages')
#     print(df)
    
#     df=create_dataframe_languages_by_context_and_type(languages_clas)
#     create_stacked_bar(df,'type of language','number of languages')
#     print(df)
#    
#     df=create_dataframe_languages_by_kind_and_type(languages_clas)
#     create_stacked_bar(df,'type of language','number of languages')
#     print(df)
   
#     df= create_dataframe_studies_by_country(studies)
#     print(df) 
#     create_choropleth_map(df,'number of studies', MAP_FILE)
     
 
    dict=count_studies_by_venue(studies)
    lista=sorted(dict.items(), key=lambda item:item[1], reverse=True)
    for elem in lista:
        print(elem)
      