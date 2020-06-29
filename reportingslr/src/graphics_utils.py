# -*- coding: utf-8 -*-
'''
Created on 27 jun. 2020

@author: reinaqu_2
'''
from matplotlib import pyplot as plt
import pandas as pd



MARKER_SQUARE='s'
MARKER_CIRCLE='o'


def create_piechart(dataframe, y_name,legend=False):
    plt.axis('equal')
    ax = plt.gca()
    plot = dataframe.plot.pie(y=y_name, figsize=(5, 5),ax=ax, autopct='%1.1f%%', legend=legend)
    plt.show()     

def create_piechart_subplots(dataframe,legend=False):
    plt.axis('equal')
    ax = plt.gca()
    plot = dataframe.plot.pie(subplots=True, ax=ax, autopct='%1.1f%%',legend=legend) 
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
