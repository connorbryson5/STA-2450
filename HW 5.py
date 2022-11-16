# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:39:43 2022

@author: nerdf
"""

import random as rand
import scipy.stats as stats


def bootstrap_sample(data):
    bootstrap_list = rand.choices(data, k=len(data))
    return bootstrap_list

def trimmed_mean(data, area):
    bootstrap = bootstrap_sample(data)
    bootstrap.sort()
    sorted_bootstrap = bootstrap
    trimmed_mean = stats.trim_mean(sorted_bootstrap, area)
    
    return trimmed_mean
    
    
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 50, 59, 1009, 38381, 909]
trimmed_mean(data, .53)


    