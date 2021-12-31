#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:59:07 2020

@author: boek0007
"""
#%%
import pandas as pd

# set up dataframe
df = pd.DataFrame({'colA':['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd'], 
                   'colB':['cat', 'cat', 'dog', 'cat', 'dog', 'cat', 'cat', 'dog'],
                   'colC':[1,2,3,4,4,5,6,7], })
print(df)

# group on vals in column A
# get min (within groups) for column B 
df_agg = ( df.groupby(by=['colA'])
          .agg({'colB':'min', 'colC':'mean'})
          .rename(columns={'colB':'min_colB', 'colC':'avg_colC'})
          )
print(df_agg)


# if you want multiple aggregations on the same column, pass a list
#   this will return a multiindex
# group on vals in column A
# get min (within groups) for column B 
# get avg and max (within groups) for column C
df_agg2 = ( df.groupby(by=['colA'])
          .agg({'colB':'min', 'colC':['mean', 'max']})
          .rename(columns={'colB':'colB_grp_min', 'colC':'colC_grp_multi_index'})
          )
print(df_agg2)
