# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 01:20:35 2020

@author: clayk
"""

import pandas as pd

####################################
data_file = "behavior_df_adjusted.csv"
time_threshold = 5
###################################

df = pd.read_csv(data_file, index_col=0)
df["time_diff"] = df["Time(s)"].diff()
df.time_diff[df.time_diff.isna()]=100
df.time_diff[df.time_diff<0]=100

df["follow3"] = df['Event'].shift(1)==3

df_pared = df[df.follow3 & (df.time_diff<time_threshold)]
df_pared.Event = df_pared.Event.astype('category')



#########################################
## Some fun counting and visualizations
import seaborn as sns
import matplotlib.pyplot as plt

#table
by_day_summary = df_pared.groupby(['Subject', 'Event', 'Day']).size().unstack(fill_value=0)

#one subject countplot
sns.countplot(data=df_pared[df_pared.Subject=="AOIL1"], x="Event", hue="Day")

#all subject individual plots
g = sns.FacetGrid(data=df_pared[(df_pared.Subject!="AIOL2") & (df_pared.Subject!="AOIL6")], col="Subject", hue="Day")
g = g.map(sns.countplot, "Event")
############################################

