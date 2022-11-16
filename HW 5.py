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
    trimmed_mean = stats.trim_mean(bootstrap, area)
    return trimmed_mean

def bootstrap_trimmed_mean(data, area, simulations):
    bootstrapMeanList = []
    for i in range (1, simulations):
        bootstrapMean = trimmed_mean(data, area)
        bootstrapMeanList.append(bootstrapMean)
    bootstrapMeanList.sort()
    trimmedbootstrapMean = stats.trim_mean(bootstrapMeanList, area)
    return trimmedbootstrapMean
    
    
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 50, 59, 1009, 38381, 909]
trimmed_mean(data, 0.1)
bootstrap_trimmed_mean(data, 0.1, 10)


    