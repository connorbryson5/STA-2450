# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:39:43 2022

@author: nerdf
"""

# imports the module "random" as "rand"
import random as rand

# imports the module "scipy.stats" as "stats"
import scipy.stats as stats


def bootstrap_sample(data):
    """
    Creates a bootstrap sample (list made with replacement from an initial list 
    of numbers

    Parameters
    ----------
    data : list
        user-inputted list of numbers

    Returns
    -------
    bootstrap_list : list
        bootstrap list of numbers generated from the original list "data"

    """
    
    # creates the list "bootstrap_list" with uses the module "random" to 
    # take values from the list "data" with replacement. Takes number of values
    # equal to the length of the list "data" to keep the list lengths the same
    bootstrap_list = rand.choices(data, k=len(data))
    
    # returns bootstrap_list
    return bootstrap_list

def trimmed_mean(data, area):
    """
    Calculates the trimmed_mean of the bootsrap list, which is the mean of the
    list without a user-determined percentage of its lowest and highest values

    Parameters
    ----------
    data : list
        user-inputted list of numbers
    area : float
        percentage of data to be trimmed

    Returns
    -------
    trimmed_mean : float
        trimmed mean of "bootstrap list"

    """
    
    # creates the variable "bootstrap" which is the bootstrap list obtained
    # from running the function "bootstrap_sample"
    bootstrap = bootstrap_sample(data)
    
    trimmed_mean = stats.trim_mean(bootstrap, area)
    return trimmed_mean

def bootstrap_trimmed_mean(data, area, simulations):
    bootstrapMeanList = []
    for i in range (1, simulations+1):
        bootstrapMean = trimmed_mean(data, area)
        bootstrapMeanList.append(bootstrapMean)
    finalbootstrapMean = bootstrap_sample(bootstrapMeanList)
    return finalbootstrapMean
    
    
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 50, 59, 1009, 38381, 909]
trimmed_mean(data, 0.1)
bootstrap_trimmed_mean(data, 0.1, 10)


    