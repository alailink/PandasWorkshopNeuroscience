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
* behav_df.reset_index(drop=True) will make your life a little easier.

## Reformatting it for YOU
Currently our data looks something like this

| AOIL1   | AOIL1 | AOIL2   | AOIL2 |
|---------|-------|---------|-------|
| Time(s) | Event | Time(s) | Event |   ........
| 3       | 8     | 7.9     |  10   |
| 4       | 12    | 9       |  12   |

And we have a loooong way to go to make it look like this:

| Event | Time(s) | Subject | Day |
|-------|---------|---------|-----|
| 3     |  0.3    | AOIL2   | 1   |
| 6     | 8.1     | AOIL2   | 1   |
| 2     | 12      | AOIL2   | 1   |

What we have to do is called reshaping the data, and in pandas there are a few ways to do that. Here are two tutorials on how to reshape your data the way you want to:  
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html
https://nikgrozev.com/2015/07/01/reshaping-in-pandas-pivot-pivot-table-stack-and-unstack-explained-with-pictures/

hint:
* you'll want to use stack for this one.
* dfs.index = dfs.index.droplevel(level=0), this command will simplify your dataframe to what you need (after stacking.)


## Cleaning Up
If you notice, your data has a lot of zeros in it... Importantly, zeros that aren't real measurements. You need to get rid of them somehow. I have chosen to just remove all zero events, because I know that zero doesn't represent a real event.

```python
behav_df = behav_df[behav_df.Event!=0]
```  
if you just type in behav_df.Event!=0, you get an array returned that is True/False. And so, another way to think about this confusing dataframe inside a dataframe is:

```python
rows_i_care_about = behav_df.Event!=0 #rows where event doesn't equal zero
behav_df = behav_df[rows_i_care_about] #resetting dataframe to only include rows i care about
```



