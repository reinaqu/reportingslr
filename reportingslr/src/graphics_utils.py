# -*- coding: utf-8 -*-
'''
Created on 27 jun. 2020

@author: reinaqu_2
'''
from matplotlib import pyplot as plt
import geopandas as gpd
from dataframes import create_dataframe_studies_by_country
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import venn

MARKER_SQUARE='s'
MARKER_CIRCLE='o'
COUNTRY_MAP = 'ADMIN' # for countries.geojson
#COUNTRY_MAP = 'name' ==> for world_countries.json


def create_piechart(dataframe, y_name,legend=False, y_axis_label=True):
    '''
    INPUT:
        -dataframe: A panda dataframe with the data to be plotted.
        -x_name: Name of the column that has to be represented in the x axis.
        -lines: Sequence or list of names of the columns that have to be represented in y axis.
        -colours: Sequence or list of colours of the different lines
    '''
    plt.axis('equal')
    ax = plt.gca()
        
    plot = dataframe.plot.pie(y=y_name, figsize=(5, 5),ax=ax,  pctdistance=0.8, labeldistance=1.1, autopct='%1.1f%%', legend=legend)
    if y_axis_label==False:
        ax.set_ylabel('')
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
        
          
    plt.grid()    
    plt.show()


def create_bar(dataframe, x_labels_rotation=90, legend=True):
    '''
    INPUT:
        -dataframe: A panda dataframe with the data to be plotted.
        -x_name: Name of the column that has to be represented in the x axis.
        -lines: Sequence or list of names of the columns that have to be represented in y axis.
        -colours: Sequence or list of colours of the different lines
    '''
    # gca stands for 'get current axis'
    #plot = dataframe.plot(kind='bar',x=x_name)
    plot = dataframe.plot(kind='bar')
    plt.xticks(rotation=x_labels_rotation)
    ax1 = plt.gca()
    ax1.xaxis.label.set_visible(False)
    ax1.legend().set_visible(legend)
    plt.show()

    

def create_stacked_bar(dataframe,column_name, values_name,x_labels_rotation=0):
    '''
    INPUT:
        -dataframe: A panda dataframe with the data to be plotted.
        -x_name: Name of the column that has to be represented in the x axis.
        -lines: Sequence or list of names of the columns that have to be represented in y axis.
        -colours: Sequence or list of colours of the different lines
    '''
    pivot_df = dataframe.pivot(columns=column_name, values=values_name)
 

    ax=pivot_df.plot.bar(stacked=True)
    #to draw the labels we have to iterate over the bar rectangles.
    for rec in ax.patches:
        x= rec.get_x() + rec.get_width() / 2
        y =  rec.get_y()+ rec.get_height()/2
        label= str(int(rec.get_height()))
        ax.text(x, y,label, ha = 'center', va='center') 
    plt.xticks(rotation=x_labels_rotation)      
    plt.show()


def dataframe_search_country(dataframe,country):
    #res = dataframe['number of studies'].where(dataframe['countries'] == country,0)
    res_df= dataframe.loc[dataframe['countries'] == country]
    if res_df.empty:
        res=0
    else:
        res= res_df['number of studies']
        res.index=[range(0,len(res))] 
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
    fig, ax = plt.subplots(1, figsize=(20, 50))
    #remove axes
    ax.set_axis_off()
    
    # Create colorbar as a legend
    sm = plt.cm.ScalarMappable(cmap='Blues', 
                               norm=plt.Normalize(vmin=vmin, vmax=vmax))
    # empty array for the data range
    sm._A = []
    
    
    axins1 = inset_axes(ax,
                    width="2%",  # width = 50% of parent_bbox width
                    height="50%",  # height : 5%
                    loc='lower right'
                    )
    
    # add the colorbar to the figure
    cbar = fig.colorbar(sm, cax=axins1)
 
 
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
    
def create_bubble(dataframe, rows, columns, count_name, x_name, y_name):
    #create padding column from values for circles that are neither too small nor too large
    df_aux= dataframe[count_name]
    dataframe["padd"] = 2.5 * (df_aux - df_aux.min()) / (df_aux.max() - df_aux.min()) + 0.5
    fig = plt.figure()
    #prepare the axes for the plot - you can also order your categories at this step
    s = plt.scatter(rows, columns, s = 0)
    #s.remove
    ax = plt.gca()
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.set_xmargin(0.5)
    ax.set_ymargin(0.5)
   
    
    #plot data row-wise as text with circle radius according to Count
    for row in dataframe.itertuples():
        bbox_props = dict(boxstyle = "circle, pad = {}".format(row.padd), fc = "w", ec = "r", lw = 2)
        plt.annotate(str(row[3]), xy = (row[1], row[2]), bbox = bbox_props, ha="center", va="center", zorder = 2, clip_on = False)
    #plot grid behind markers
    plt.grid(ls = "--", zorder = 1)
    #take care of long labels
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.show()


    
def create_venn4(labels, names):
    fig, ax = venn.venn4(labels, names=names)

    #fig.savefig('venn4.png', bbox_inches='tight')
    plt.show()
    
def create_venn3(labels, names):
    fig, ax = venn.venn3(labels, names=names)

    #fig.savefig('venn4.png', bbox_inches='tight')
    plt.show()