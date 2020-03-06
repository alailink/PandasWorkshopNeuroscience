# Introduction

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
