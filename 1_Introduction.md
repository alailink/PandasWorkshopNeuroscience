# Introduction

Today we are going over the basics of pandas, a python package. It allows you to manipulate datasets, and with a few other tools you can do statistics and graphing with it fairly easily. 

## Wtf is a "package"? 

If you've ever looked at code, you may have seen some garbage at the top that looks like this:

```python
import pandas as pd
import numpy as np
from os import chdir
from scipy.stats import ttest_ind, f_oneway
import seaborn as sns
import matplotlib.pyplot as plt
```  

Understandably, it's nonsense to you. Why are we "importing" things into python?  The thing is, python is really dumb, and it's just an empty shell for everything else we want to do. 

For example, imagine a future pizza restaurant, but right now it's just an empty building. We have everything we need for a good restaurant (building, heating, water, etc.), but we don't have any equipment yet. Let's do that now:  

```python
import mccormickandschidt_pizzaheater
import cuttingboard
import freezer
```  

Cool. But imagine that you want to give a nickname to that really long oven. Python lets you do that:

```python
import mccormickandschidt_pizzaheater as oven
```  

## What's this BS about "object-oriented" programming?

I don't know why programmers make such a big deal about this, or make it so complicated. The concept is simple, though. Say you imported your oven package, and you wanted to do things with it. Perhaps some commands would look like this:

```python
oven.heat_on()
oven.start_rolling()
oven.set_temp(500)
```  

oven is the object, and those things we called came from the object. But that's not the only thing we can do with it. Maybe we want to get information about that object. Often there are commands to just find information:

```python
print(oven.temp())
375
``` 

It hasn't warmed up yet, but it gave us the current temperature. Also, we learned how to use the print command for something useful.

## How does this apply to Pandas?

Pandas is a python package, and it works just like the ridiculous pizza example. To create a dataset, you can explicitly create one in python, or you can load in an excel/csv file:

```python
import pandas as pd

df1 = pd.Dataframe([[4,5,4,5][a,b,c,d]])
df2 = pd.read_excel("data.xls")
df3 = pd.read_csv("data.csv")
``` 
The cool part is that you have created a dataframe object. Yes, an object. And it has properties and methods that you can check and use.  

```python
df3.size()
df3.columns
df3.groupby()
```  

These will be used extensively throughout the workshop.
