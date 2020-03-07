# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:12:09 2020

@author: clayk
"""

from os import chdir
import pandas as pd

#############################################
### User defined variables ##################
#############################################

wdir = r"C:\Users\clayk\Desktop\SpringBreakPythonWorkshop"
data = "Data\Day 1_Raw Data.xlsx"

###################################

#change working directory
chdir(wdir)

#read in the data file
df = pd.read_excel(data, skiprows = 2, header = [0,1], index_col=None)
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




######################################
## Just for fun......

#eventcount = dfs.groupby(by=["Subject","Event"]).count().unstack()
#eventcountm = pd.melt(eventcount, id_vars = index)
#eventcount.columns = eventcount.columns.droplevel(level=0)
#
#df = eventcount
#df = df/df.std(axis=0).T
#
#import seaborn as sns
#sns.scatterplot(data=df)

#########################################
