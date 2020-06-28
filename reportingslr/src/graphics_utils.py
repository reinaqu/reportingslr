# -*- coding: utf-8 -*-
'''
Created on 27 jun. 2020

@author: reinaqu_2
'''
from matplotlib import pyplot as plt
import pandas as pd



MARKER_SQUARE='s'
MARKER_CIRCLE='o'

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
    
def create_line_plot_multiple_colums(dataframe, x_name, lines, colours,markers):
    '''
    INPUT:
        -dataframe: A panda dataframe with the data to be plotted.
        -x_name: Name of the column that has to be represented in the x axis.
        -lines: Sequence or list of names of the columns that have to be represented in y axis.
        -colours: Sequence or list of colours of the different lines
    '''
    # gca stands for 'get current axis'
    ax = plt.gca()
    for i in range(0,len(lines)):
        dataframe.plot(kind='line',x=x_name, y=lines[i], color=colours[i],marker=markers[i], ax=ax)
        
    plt.show()
    
