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

from dataframes_sc import *
import locale
from csvbib_utils import ID_PAPER
if __name__ == "__main__":
    studies=load_report_csv("../data/report.0.0.97.csv",ID_PAPER, enc='cp1252')
    MAP_FILE='../data/countries.geojson'
    CITATION_FILE='../data/citations_per_paper.xlsx'
    REPORT_FILE="../data/report.0.0.97.xlsx"
     
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
#      
#      
    languages = studies_by_language(studies)

#     print(count_languages_by_blockchain(languages))
#     generate_languages_by_blockchain(languages,lambda b:not is_blockchain_null(b))
  
    df = create_dataframe_languages_by_blokchain_platform(languages)
    print(df)
    create_bar(df)
    print(languages)
     
#     df=create_dataframe_languages_by_context_and_kind(languages)
#     create_stacked_bar(df,'kind of language','number of languages')
#     print(df)
#     
#     df=create_dataframe_languages_by_context_and_type(languages)
#     create_stacked_bar(df,'type of language','number of languages')
#     print(df)
#     
#     df=create_dataframe_languages_by_kind_and_type(languages)
#     create_stacked_bar(df,'type of language','number of languages')
#     print(df)
#    
#     df= create_dataframe_studies_by_country(studies)
#     print(df) 
# #     create_choropleth_map(df,'number of studies', MAP_FILE)
#          
#    generate_venues_ordered_by_num_studies(studies) 
#          

    
    df_pp= create_dataframe_from_excel(CITATION_FILE, 'From publish or perish - Rebuta', ID_PAPER)
    df_am= create_dataframe_from_excel(CITATION_FILE, 'Altimetrics from PlumX',ID_PAPER)
    df_rp= create_dataframe_from_excel(REPORT_FILE,'report.0.0.97', ID_PAPER)
    df_qa= create_dataframe_from_excel(REPORT_FILE,'Quality', ID_PAPER)
    df_uc= create_dataframe_from_excel(REPORT_FILE,'Use cases', ID_PAPER)
    
    #print(df_pp)
    #print(df_am)
    #print(df_rp)
    print(df_uc)
    
     
#     df_intrinsicIQ_count = create_dataframe_intrinsicIQ_count(df_qa)
#     create_bar(df_intrinsicIQ_count, 'IntrinsicIQ',x_labels_rotation=0)

    df_contextualIQ=create_dataframe_studies_contextualIQ(studies)
#     df_ciq_count = create_dataframe_contextualIQ_count(df_contextualIQ)
#     print(df_ciq_count)
#     create_bar(df_ciq_count, 'ContextualIQ',x_labels_rotation=0)
 
  
#     df_facets=create_dataframe_quality_facets(df_contextualIQ, df_qa)
#     print(df_facets)
#     df_fa=create_dataframe_facets_count(df_facets)  
#     print(df_fa)
#     rows=['Low', 'Medium','High']
#     create_bubble(df_fa, rows, rows,'number of studies', 'IntrinsicIQ' , 'ContextualIQ')
    
    df = create_dataframe_use_cases_count(languages, df_uc)
    print(df)
    create_bar(df)
    
    #generate_citations_per_paper(studies, df_pp, df_am, df_rp)
    #generate_white_literature(studies, df_rp)
    
    #generate_grey_literature(studies, df_rp)

        