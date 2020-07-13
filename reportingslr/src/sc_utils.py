# -*- coding: utf-8 -*-
'''
Created on 29 jun. 2020

@author: reinaqu_2
'''
from commons import *
import numpy as np
import pandas as pd

BLOCKCHAIN ="Blockchain name"
ID_LANG ="Language (ids studies)"
IMPLEMENTATION_KIND= "Kind : Implementation"
SPECIFICATION_KIND= "Kind : Specification"
ACADEMIA_CONTEXT="Insitution origin : Academia"
INDUSTRY_CONTEXT="Insitution origin : Industry}"
STANDALONE_TYPE ="DSL Type : Standalone"
EXTENSION_TYPE="DSL Type : Extension}"
IMPLEMENTATION_LABEL="Implementation"
SPECIFICATION_LABEL="Specification"
ACADEMIA_LABEL="Academia"
INDUSTRY_LABEL="Industry" 
STANDALONE_LABEL="Standalone"
EXTENSION_LABEL="Extension"
UNKNOWN_LABEL="Unknown"

ID_PAPER ="ID Paper"
LANGUAGE_NAME= "Name"
ID_SLR="ID SLR"
def count_languages_by_blockchain(languages_list, filter=None):
    '''
    INPUT:
        - languages_list: Dict(language: [Dict{id_paper:DictReaderEntry(reference)}])
    OUTPUT:
        - dataframe: panda.Dataframe with the following structure:
           * index: blockain platform
           * number of languages_list: number of languages_list per blockchain platform
    '''
    dict = group_languages_by_blockchain(languages_list)
    if filter==None:
        res= {blockchain:len(lang_list) for blockchain, lang_list in dict.items()}
    else:
        res= {blockchain:len(lang_list) for blockchain, lang_list in dict.items() if filter(blockchain)}
    return res

def group_languages_names_by_blockchain(languages_list, filter=None):
    dict = group_languages_by_blockchain(languages_list)
    if filter==None:
        res= {blockchain:languages_names(lang_list) for blockchain, lang_list in dict.items()}
    else:
        res= {blockchain:languages_names(lang_list) for blockchain, lang_list in dict.items() if filter(blockchain)}
        
    return sorted(res.items(), key=lambda it:len(it[1]), reverse=True)

def languages_names(studies_list):
    return sorted(set(studies_list))
    
def is_blockchain_null(blockchain):
    return blockchain == 'null'

def is_blockchain_na(blockchain):
    return blockchain == 'n/a' 

def group_languages_by_blockchain(languages):
    '''
    INPUT:
        - languages: Dict(language: [Dict{id_paper:DictReaderEntry(reference)}])
    OUTPUT:
        - Dict(language: {Blockchain}}
    '''
    dicc=defaultdict(list)
    for language, list_studies in languages.items():
        conj = blockchains(list_studies)
        for blockchain in conj:
            dicc[blockchain].append(language)
    return dicc
    
def blockchains(list_studies):
    con=set()
    for study in list_studies:
        lst= study[BLOCKCHAIN].split(',')
        for it in lst:
            con.add(it.strip())
    return con

def count_languages_by_context_and_kind(languages, filter=None):
    '''
    INPUT: Dict(language:[OrderedDict(...)]
    '''
    dict ={language: studies[0] for language, studies in languages.items()}
    return count_by_property_pairs(dict, lambda s:language_context(s), lambda s:language_kind(s),  filter)

def count_languages_by_kind_and_type(languages, filter=None):
    dict ={language: studies[0] for language, studies in languages.items()}
    return count_by_property_pairs(dict, lambda l:language_kind(l), lambda l:language_type(l),  filter)

def count_languages_by_context_and_type(languages, filter=None):
    dict ={language: studies[0] for language, studies in languages.items()}
    return count_by_property_pairs(dict, lambda l:language_context(l), lambda l:language_type(l),  filter)

def language_kind (study):
    res=UNKNOWN_LABEL
    if study[IMPLEMENTATION_KIND]=='Y' and  study[SPECIFICATION_KIND]=='N':
        res=IMPLEMENTATION_LABEL
    elif study[IMPLEMENTATION_KIND]=='N' and  study[SPECIFICATION_KIND]=='Y':
        res=SPECIFICATION_LABEL
    return res

def language_context (study):
    res=UNKNOWN_LABEL
    if study[ACADEMIA_CONTEXT]=='Y' and  study[INDUSTRY_CONTEXT]=='N':
        res=ACADEMIA_LABEL
    elif study[ACADEMIA_CONTEXT]=='N' and  study[INDUSTRY_CONTEXT]=='Y':
        res=INDUSTRY_LABEL
    return res

def language_type(language):
    res=UNKNOWN_LABEL
    if language[EXTENSION_TYPE]=='Y' and  language[STANDALONE_TYPE]=='N':
        res=EXTENSION_LABEL
    elif language[EXTENSION_TYPE]=='N' and  language[STANDALONE_TYPE]=='Y':
        res=STANDALONE_LABEL
    return res


def studies_by_language(studies):
    return group_by_property(studies, lambda s:language(s))
    
def language(study_dict):
    
    lang_name=study_dict[LANGUAGE_NAME].strip()
    if lang_name=='null':
        lang_name=study_dict[ID_SLR].strip()
    return lang_name    


def completeness(study):
    qa1 = has_language_name(study)
    qa2 = has_paradigm(study)
    qa3 = has_blockchain(study)
    qa4 = has_dsl_type(study)
    qa5 = has_focus(study)
    qa6 = has_institution(study)
    qa7 = has_institution_origin(study)
    qa8 = has_challenges(study)
    qa9= has_use_cases(study)
    qa10 = has_language_kind(study)
    return (qa1+qa2+qa3+qa4+qa5+qa6+qa7+qa8+qa9+qa10)/10

def contextual_IQ(study):
    c = completeness(study)
    if c>0.5:
        res='High'
    elif c>0.2:
        res='Medium'
    else:
        res='Low'
    return (c, res)
    
def has_language_name(study):
    LANGUAGE_NAME='Name'
    return 0 if study[LANGUAGE_NAME]=='null' else 1

def has_paradigm(study):
    UNDETERMINED_PARADIGM="Paradigm : Undetermined}"
    return 0 if study[UNDETERMINED_PARADIGM]=='Y' else 1

def has_blockchain(study):
    SUPPORTED_BY_BLOCKCHAIN='Supported by blockchain platform : Yes'
    BLOCKCHAIN_NAME="Blockchain name"
    return 0 if study[SUPPORTED_BY_BLOCKCHAIN]=='Y' and study[BLOCKCHAIN_NAME]=='null' else 1

def has_dsl_type(study):
    STANDALONE='DSL Type : Standalone'
    EXTENSION='DSL Type : Extension}'
    return 0 if study[STANDALONE]=='N' and study[EXTENSION]== 'N' else 1

def has_focus(study):
    FOCUS='Focus'
    return 0 if study[FOCUS]=='null' else 1

def has_institution(study):
    INSTITUTION='Institution name'
    return 0 if study[INSTITUTION]=='null' else 1

def has_institution_origin(study):
    INSTITUTION='Institution name'
    ACADEMIA = 'Insitution origin : Academia'
    INDUSTRY = 'Insitution origin : Industry}'
    return 0 if study[INSTITUTION]=='null' and (study[ACADEMIA]=='Y' or study[INDUSTRY]== 'Y') else 1


def has_challenges(study):
    CHALLENGES='Challenges'
    return 0 if study[CHALLENGES]=='null' else 1
 
def has_use_cases(study):
    USE_CASES='Use cases'
    return 0 if study[USE_CASES]=='null' else 1

def has_language_kind(study):
    IMPLEMENTATION='Kind : Implementation'
    SPECIFICATION='Kind : Specification'
    UNKNOWN='Kind : Unknown}'

    return 0 if study[IMPLEMENTATION]=='N' and study[SPECIFICATION]=='N' and study[UNKNOWN]=='N' or study[UNKNOWN]=='Y' else 1

def count_use_cases (languages, df_usecases):
    '''
    INPUT: 
        -studies : list o studies [OrderedDict(('Paper ID':id), ('Zone', Country_name)]
        -df_usecases: dataframe with the following requirements:
            * It should have as index the ID_PAPER
            * It should have a column (named Clasificación) with the use cases
            * The use cases of the study should have the format uc1/uc2/...
              For example, Financial/Game/Notary/Others

    OUTPUT: 
        - {language:set(use cases)} dictionary whose keys are the languages names and whose
          values are sets of the use cases found for that language
    ''' 
    dict= group_use_cases_by_languages(languages, df_usecases)
    lista=[]
    for conj in dict.values():
        print(conj)
        lista= lista +list(conj)
    return Counter(lista)
    
    

def group_use_cases_by_languages (languages, df_usecases):
    '''
    INPUT: 
        -studies : list o studies [OrderedDict(('Paper ID':id), ('Zone', Country_name)]
        -df_usecases: dataframe with the following requirements:
            * It should have as index the ID_PAPER
            * It should have a column (named Clasificación) with the use cases
            * The use cases of the study should have the format uc1/uc2/...
              For example, Financial/Game/Notary/Others

    OUTPUT: 
        - {language:set(use cases)} dictionary whose keys are the languages names and whose
          values are sets of the use cases found for that language
    ''' 
    return {language: extract_use_cases(studies,df_usecases) for language, studies in languages.items()}

def extract_use_cases(studies, df_usecases):
    '''
    INPUT: 
        -studies : list o studies [OrderedDict(('Paper ID':id), ('Zone', Country_name)]
        -df_usecases: dataframe with the following requirements:
            * It should have as index the ID_PAPER
            * It should have a column (named Clasificación) with the use cases
            * The use cases of the study should have the format uc1/uc2/...
              For example, Financial/Game/Notary/Others

    OUTPUT: 
        - A set with all the use cases of all the studies in the list
    '''
    conj=set()
    for study in studies:
        conj=conj.union(get_use_cases(study, df_usecases))
    return conj

def get_use_cases(study,df_usecases):
    '''
    INPUT: 
        -study : OrderedDict(('Paper ID':id), ('Zone', Country_name)
        -df_usecases: dataframe with the following requirements:
            * It should have as index the ID_PAPER
            * It should have a column (named Clasificación) with the use cases
            * The use cases of the study should have the format uc1/uc2/...
              For example, Financial/Game/Notary/Others

    OUTPUT: 
        - A set with all the use cases of the study
    '''
    conj=set()
    #Get the id of the study
    id_slr=study[ID_PAPER].strip()
    #Query de dataframe to get all the use cases
    uc=df_usecases.loc[int(id_slr)].loc['Clasificación']
    #As there can be nan data, we only can split if the data is not nan
    if not pd.isna(uc):
        c=set(uc.split("/"))
        c={pal.strip() for pal in c}
        conj=conj.union(c)
    return conj


  
   