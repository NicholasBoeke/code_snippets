#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 07:49:19 2020

@author: boek0007
"""
#%%

import calendar as c
c.setfirstweekday(6)

import os
os.chdir('/Users/boek0007/Desktop/')


sep = '\n'*3
rng = range(1977, 2078)

cal_list = [c.calendar(y) for y in rng]
cals_str = sep.join(cal_list)

with open('century_calendar1977.txt', 'w', encoding='utf8') as txt_file:
    txt_file.write(cals_str)
    