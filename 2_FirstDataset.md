# Loading in your First Dataset

Before all the fun begins, we must first load in one or several datasets. You can't do anything until you've gotten past this boring step. Since we're using excel:

```python
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
behav_df = pd.read_excel()
``` 
A few important notes. It's good practice to change your working directory at the beginning of the program. That way your program runs as expected every time. Hence chdir and wdir. Second, I haven't loaded in the excel file. You'll have to look up documentation on how to do that here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html. 

hints:  
* you already defined the data file (or you should have)
* set index_col = False
* the headers of the file are in the wrong spot, so you'll have to skip rows and explicity declare where the 2 headers are.  

## Reformatting it for YOU



