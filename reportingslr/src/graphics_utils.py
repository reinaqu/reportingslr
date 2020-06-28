# -*- coding: utf-8 -*-
'''
Created on 27 jun. 2020

@author: reinaqu_2
'''
from matplotlib import pyplot as plt

def create_piechart(data_dict):
    ''' Create a piechart from a dictionary with data   
    INPUT: 
       - data_dict: dict with values-> {str:int}
    OUTPUT: 
       - A piechart is shown
    '''
    labs,values = zip(*data_dict.items()) 
   
    plt.pie(values, labels=labs, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.show()    
