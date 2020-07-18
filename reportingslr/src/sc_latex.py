# -*- coding: utf-8 -*-
'''
Created on 8 jul. 2020

@author: reinaqu_2
'''
from sc_utils import *
from csvbib_utils import *
import pandas as pd

def generate_languages_by_blockchain(languages_list, filter=None):
    
    dict=group_languages_names_by_blockchain(languages_list, filter)
    txt='''\\textsf{{{0}}} & {1} \\\\ 
            \\tabucline{{1-2}}'''
    for blockchain, languages in dict:
        str_langs= str(languages).replace("[","").replace("]","").replace("'","")
        print(txt.format(blockchain, str_langs))
        
def generate_venues_ordered_by_num_studies(studies, limit=None):
    
    dict=group_studies_by_venue(studies)
    #      1 &\textsf{Computing Research Repository (CoRR)}  & Other & 5 \\ 
    lista=sorted(dict.items(), key=lambda item:(len(item[1]),item[0]), reverse=True)
    if limit!=None:
        lista=lista[:limit]
    txt='''{} & \\textsf{{{}}} & {} & {}\\\\'''
    i=1
    for venue, list_studies in lista:
        type=list_studies[0][TYPE].lower().replace("paper","").strip()
        print(txt.format(i,venue, type, len(list_studies)))
        i=i+1
        
def generate_citations_per_paper(studies, df_ppmetrics, df_altimetrics, df_studies):
    
    
    #Rank id title gs sc wos alti
    #1 & S06 & Hawk: The blockchain model of cryptography and privacy-preserving smart \hl{contracts} & 1250 & 601 & 314 & 3312\\ 
    txt='''{} & {} & {}& {} & {}& {} & {}\\\\'''
    citations=get_citations_data(studies, df_ppmetrics, df_altimetrics, df_studies)
    
    citations = sorted(citations,key=lambda t:t[2], reverse=True)
    i=1
    for id, language, gs_cit, sc_cit, wos_cit, alti_cit in citations:
        print(txt.format(i, id, language, hyphenize(gs_cit), hyphenize(sc_cit), hyphenize(wos_cit), hyphenize(alti_cit)))
        i=i+1

def generate_white_literature(studies, df_studies):
# %S50 id -start: 361084 -------------------------------------------  
# \textsf{S50}  & \cite{conf/atva/AlbertGLRS18} & Peer-to-peer Affine Commitment Using Bitcoin & K. Crary, M. J. Sullivan  & PLDI'15:479-488, 2015\\
    dict= select_literature(studies,lambda s:is_white_literature(s)) 
    sorted_ids= sorted(int(key) for key in dict.keys())

    txt='''%{} id -start: {} -------------------------------------------  
             \\textsf{{{}}}  & \\cite{{ }} & {} & {} & {}\\\\'''
    res=[]
    for study_id in sorted_ids:
        id_slr, title, authors, venue = get_id_slr_title_authors_venue(df_studies, study_id)
        venue = venue.strip().split("#")[1]
        res.append((study_id, id_slr, title, authors, venue))
        
    res = sorted(res,key=lambda t:t[1])
    for study_id, id_slr, title, authors, venue in res:
       #print(study_id, id_slr, title, authors, venue)
       print(txt.format(id_slr,study_id,id_slr,title, authors, venue))
       
def generate_grey_literature(studies, df_studies):
#%G34 id -start: 730958 -------------------------------------------     
#\textsf{G34}  & \cite{github/ewasm19} & Ethereum flavored WebAssembly (ewasm) & A. Beregszaszi, N. Wang, G. Ballet, Hugo, J. Lang, jwasinger, L. Rettig, wanderer & GitHub page & 2019 \\
    dict= select_literature(studies,lambda s:is_grey_literature(s)) 
    sorted_ids= sorted(int(key) for key in dict.keys())

    txt='''%{} id -start: {} -------------------------------------------  
             \\textsf{{{}}}  & \\cite{{ }} & {} & {} & {} & {}\\\\'''
    res=[]
    for study_id in sorted_ids:
        id_slr, title, authors, type, year = get_id_slr_title_authors_type_year(df_studies, study_id)
        res.append((study_id, id_slr, title, authors, type, year))
        
    res = sorted(res,key=lambda t:t[1])
    for study_id, id_slr, title, authors, type, year in res:
       #print(study_id, id_slr, title, authors, venue)
       print(txt.format(id_slr,study_id,id_slr,title, authors, type, year))
       
def hyphenize(num):
    return '-' if int(num)<0 else num

def hyphenize_if_nan(data):
    return '-' if pd.isna(data) else data

def get_id_slr_title_authors_venue (dataframe, id):
    row = dataframe[dataframe[ID_PAPER] == id]

    tuple= (row.iloc[0][ID_SLR], row.iloc[0]['Title'], row.iloc[0]['Authors'],row.iloc[0]['Venue'])
    return tuple

def get_id_slr_title_authors_type_year (dataframe, id):
    row = dataframe[dataframe[ID_PAPER] == id]
    
    tuple= (row.iloc[0][ID_SLR], row.iloc[0]['Title'], row.iloc[0]['Authors'],row.iloc[0]['Type'],row.iloc[0]['Year']) 
    return tuple

def get_citations_data(studies, df_ppmetrics, df_altimetrics, df_studies): 
    dict= select_literature(studies,lambda s:is_white_literature(s)) 
    sorted_ids= sorted(int(key) for key in dict.keys())
     
    df_gs = df_ppmetrics.loc[df_ppmetrics['Source']== 'Google Scholar']
    df_sc = df_ppmetrics.loc[df_ppmetrics['Source']== 'Scopus']
    df_ws = df_ppmetrics.loc[df_ppmetrics['Source']== 'Web of Science']
    res=[] 
    for study_id in sorted_ids:

        id, language = get_id_slr_language(df_studies, study_id)
        gs_cit=get_citation(df_gs, study_id)
        sc_cit=get_citation(df_sc, study_id)
        wos_cit=get_citation(df_ws,study_id)
        alti_cit = get_captures(df_altimetrics,study_id)
        res.append((id, language,gs_cit, sc_cit, wos_cit, alti_cit))
    return res

def get_id_slr_language (dataframe, id):
    row = dataframe[dataframe[ID_PAPER] == id]
    
    return (row.iloc[0][ID_SLR], row.iloc[0]['Title'])


def get_citation (dataframe, id ):
    row = dataframe[dataframe[ID_PAPER] == id]
    papers = row.iloc[0]['Papers']
    if papers != 0:
        res= row.iloc[0]['Citations']
    else:
        res=-1
    return res    

def get_captures(dataframe, id):
    row = dataframe[dataframe[ID_PAPER] == id]
    res= row.iloc[0]['PlubmX-Captures']
    if pd.isna(res):
        res=-1
    return res

def generate_studies_by_language(languages):
    ordenado = sorted(languages.items())
    for language, list_studies in ordenado:
        ids = get_property(list_studies, lambda s:id(s))
        ids_slr = get_property(list_studies, lambda s:id_slr(s))
        kinds=get_property(list_studies, lambda s:language_kind(s))
        types=get_property(list_studies, lambda s:language_type(s))
        contexts=get_property(list_studies, lambda s:language_institution_origin(s))
        paradigms=get_property(list_studies, lambda s:language_paradigms(s)) 
        bclks=blockchains(list_studies) 
        print(language , "\t", ids, "\t",ids_slr, "\t", kinds, "\t", types,"\t", contexts, "\t", paradigms, "\t", bclks)
        
def get_property(list_studies, feature):
    return [feature(study) for study in list_studies]

def generate_implementation_languages(dataframe):
    txt='''\\textsf{{{}}} & {} & {} & {}\\\\'''
    for index, row in dataframe.iterrows():
        print(txt.format(index.strip(), row.loc['slrs ids'], 
                        hyphenize_if_nan(row.loc['Level']),
                        hyphenize_if_nan(row.loc['Paradigm'])))

def generate_specification_languages(dataframe):
    txt='''\\textsf{{{}}} & {} & {}\\\\'''
    for index, row in dataframe.iterrows():
        print(txt.format(index.strip(), row.loc['slrs ids'], 
                        hyphenize_if_nan(row.loc['Paradigm'])))
        
def generate_implementation_languages_5(dataframe):
    txt='''\\textsf{{{}}} & {} & {} & {} & {}\\\\'''
    for index, row in dataframe.iterrows():
        print(txt.format(index.strip(), row.loc['slrs ids'], 
                        hyphenize_if_nan(row.loc['Focus']),
                        hyphenize_if_nan(row.loc['Level']),
                        hyphenize_if_nan(row.loc['Paradigm'])))
        