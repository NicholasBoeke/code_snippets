#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:43:51 2020

@author: boek0007
"""

#% import the library
import pandas as pd
import time

# path
data_dir = '/Users/boek0007/Desktop/'
file_name = 'dataset.csv'

# read csv into dataframe
df = pd.read_csv(data_dir + file_name)


# first five lines of df
print(df.head())

#% add some columns
# check if the string is in THIS set
df['string_manipulation'] = df['string_data'].isin(['a', 'b', 'c', 'd'])

# mulitply the integers in THIS column
df['integer_manipulation'] = df['integer_data'] * 4

# parse the string represention of the date into a date TUPLE
# see time.strptime(); string parse time
df['date_tuple'] = df['date_data'].apply(lambda x: time.strptime(x, '%m/%d/%y') )

# parse the tuple & format it into something readable
# see time.strftime(); string format time
df['date_readable'] = df['date_tuple'].apply(lambda x: time.strftime('%A %b %d, %Y', x))

# first five lines of the new dataframe 
print(df.head())


# write dataframe to new file in same dir
new_file_name = 'dataset2.csv'
df.to_csv(data_dir + new_file_name)