# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:12:09 2020

@author: clayk
"""

from os import chdir, listdir
import pandas as pd
import re

#############################################
### User defined variables ##################
#############################################

wdir = r"C:\Users\clayk\Desktop\SpringBreakPythonWorkshop\Data"
save=False


###################################

def file_loader_dataset_maker(file):
    #read in the data file
    df = pd.read_excel(file, skiprows = 2, header = [0,1], index_col=None)
    df = df.reset_index(drop=True)

    #Reformat the data
    dfs = df.stack(level=0)
    dfs.index = dfs.index.droplevel(level=0) #drop the other level because you don't care about it
    dfs = dfs[dfs.Event!=0] #Choose events DO NOT equal zero because it indicates it's not a measurement

    #Make a third column that defines the subject
    dfs["Subject"] = dfs.index
    dfs.reset_index(inplace=True, drop=True)

    #And to make life easier sort the dataframe by subect, and then by time(s)
    dfs.sort_values(by=["Subject","Time(s)"], inplace=True)
    return dfs


chdir(wdir)             #change directory
files = listdir(wdir)   #get all files in directory

i = 1
for each_file in files:
    temp_data = file_loader_dataset_maker(each_file)
    temp_data["Day"] = int(re.split(r"[\s,_]",each_file)[1])
    #this could be done in a few lines as well:
    #broken = re.split(r"[\s,_]",file)
    #number_str = strings[1]
    #value = int(number_str)
    if i == 1:
        data = temp_data
    else:
        data = pd.concat([data, temp_data], axis=0)
    i+=1

if save==True:
    data.reset_index(drop=True).to_csv("behavior_df_adjusted.csv")

########################
## visualization for fun

#import seaborn as sns
#import matplotlib.pyplot as plt
#sns.countplot(x="Event", hue="Day", data=data)
#plt.title("Lesson 3")
###########################
