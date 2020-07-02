# -*- coding: utf-8 -*-
'''
Created on 27 jun. 2020

@author: reinaqu_2
'''
from matplotlib import pyplot as plt
import pandas as pd
import geopandas as gpd
import shapefile
import pycrs
from dataframes import create_dataframe_studies_per_country
from json.decoder import NaN
import numpy as np

MARKER_SQUARE='s'
MARKER_CIRCLE='o'
COUNTRY_MAP = 'ADMIN' # for countries.geojson
#COUNTRY_MAP = 'name' ==> for world_countries.json


def create_piechart(dataframe, y_name,legend=False):
    '''
    INPUT:
        -dataframe: A panda dataframe with the data to be plotted.
        -x_name: Name of the column that has to be represented in the x axis.
        -lines: Sequence or list of names of the columns that have to be represented in y axis.
        -colours: Sequence or list of colours of the different lines
    '''
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

def create_bar(dataframe, x_name):
    '''
    INPUT:
        -dataframe: A panda dataframe with the data to be plotted.
        -x_name: Name of the column that has to be represented in the x axis.
        -lines: Sequence or list of names of the columns that have to be represented in y axis.
        -colours: Sequence or list of colours of the different lines
    '''
    # gca stands for 'get current axis'
    plot = dataframe.plot(kind='bar')
    plt.show()

def create_stacked_bar(dataframe,column_name, values_name):
    '''
    INPUT:
        -dataframe: A panda dataframe with the data to be plotted.
        -x_name: Name of the column that has to be represented in the x axis.
        -lines: Sequence or list of names of the columns that have to be represented in y axis.
        -colours: Sequence or list of colours of the different lines
    '''
    pivot_df = dataframe.pivot(columns=column_name, values=values_name)
    pivot_df.plot.bar(stacked=True)
    
    plt.show()
    
def dataframe_search_country(dataframe,country):
    #res = dataframe['number of studies'].where(dataframe['countries'] == country,0)
    print(dataframe)
    res_df= dataframe.loc[dataframe['countries'] == country]
    if res_df.empty:
        res=0
    else:
        res= res_df['number of studies']
        res.index=[range(0,len(res))] 
        print(res.index,'-->', res)
    return res

def create_choropleth_map (dataframe, column_name, geojson_mapfile):

    #read the map as a geodataframe
    world_df = gpd.read_file(geojson_mapfile)
   
    #To draw all the countries, a left -join is needed.
    #Note that when the country does not exist in dataframe, the column 'number of studies' has a NaN value
    merged = world_df.merge(dataframe, how='left',left_on = COUNTRY_MAP, right_on = 'countries')
    #The NaN values are replaced by 0
    merged = merged.replace(np.nan, 0)    
    
    # set the range for the choropleth (min and max values)
    vmin, vmax=0, max(dataframe[column_name])
    
    # create figure and axes for Matplotlib
    fig, ax = plt.subplots(1, figsize=(30, 10))
    #remove axes
    ax.set_axis_off()
    
    # Create colorbar as a legend
    sm = plt.cm.ScalarMappable(cmap='Blues', 
                               norm=plt.Normalize(vmin=vmin, vmax=vmax))
    # empty array for the data range
    sm._A = []
    # add the colorbar to the figure
    cbar = fig.colorbar(sm)
 
 
    # create map
    ax = merged.plot(column=column_name, 
                           cmap ='Blues',
                           linewidth=0.8, 
                           ax=ax, 
                           edgecolor='0.8')
   
    # Add Labels
    #merged['coords'] = merged['geometry'].apply(lambda x: x.representative_point().coords[:])
    #merged['coords'] = [coords[0] for coords in merged['coords']]
    #for idx, row in merged.iterrows():
    #    if (row[column_name]>0):
    #        plt.annotate(s=str(int(row[column_name])), xy=row['coords'],horizontalalignment='center')
    plt.show()