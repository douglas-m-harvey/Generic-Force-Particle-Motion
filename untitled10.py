# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 12:48:25 2018

@author: My Surface Pro
"""

for k in range(1, 30):
    for i in range(0, 4):
        for j in range(0, 4):
            if i != j:
                print("No match")
            else:
                print("Match")