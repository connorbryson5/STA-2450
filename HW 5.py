# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:39:43 2022

@author: nerdf
"""

# imports the module "random" as "rand"
import random as rand

# imports the module "scipy.stats" as "stats"
import scipy.stats as stats

# imports the module plotnine
import plotnine

# imports the module pandas as pd
import pandas as pd

def bootstrap_sample(L):
    """
    Creates a bootstrap sample (list made with replacement from an initial list 
    of numbers

    Parameters
    ----------
    L : list
        user-inputted list of numbers

    Returns
    -------
    bootstrap_list : list
        bootstrap list of numbers generated from the original list "data"

    """
    
    # creates the list "bootstrap_list" with uses the module "random" to 
    # take values from the list "data" with replacement. Takes number of values
    # equal to the length of the list "data" to keep the list lengths the same
    bootstrapList = rand.choices(L, k=len(L))
    
    # returns bootstrap_list
    return bootstrapList

def trimmed_mean(L, area):
    """
    Calculates the trimmed_mean of the bootsrap list, which is the mean of the
    list without a user-determined percentage of its lowest and highest values

    Parameters
    ----------
    L : list
        user-inputted list of numbers
    area : float
        percentage of data to be trimmed

    Returns
    -------
    trimmed_mean : float
        trimmed mean of "bootstrap list"

    """
    
    # creates the list "bootstrap" which is the bootstrap list obtained
    # from running the function "bootstrap_sample"
    bootstrap = bootstrap_sample(L)
    
    # creates the variable trimmedMean which trims the mean of bootstrap by 
    # a user determined percentage "area"
    trimmedMean = stats.trim_mean(bootstrap, area)
    
    # returns "trimmedMean"
    return trimmedMean


def bootstrap_trimmed_mean(L, area, simulations):
    """
    Creates a bootstrap list for a list of trimmed means of the original 
    bootstrap list

    Parameters
    ----------
    L : list
        user-inputted list of numbers
    area : float
        percentage of data to be trimmed
    simulations : integer
        Determines how many trimmed means will be calculated and appended to an
        empty list

    Returns
    -------
    finalbootstrap : list
        Bootstrap list for the list of trimmed means of the original bootstrap
        list

    """
    
    # Creates an empty list called "bootstrapMeanList"
    bootstrapmeanList = []
    
    # For loop tht goes from 1 to the amount of simulations+1 
    for i in range (1, simulations+1):
        
        # Calls the "trimmed_mean" function with input parameters "L" and 
        # "area" and saves the result to a variable called "bootstrapMean"
        bootstrapMean = trimmed_mean(L, area)
        
        # Appends that "bootstrapMean" to the bootstrapMeanList
        bootstrapmeanList.append(bootstrapMean)
     
    # Calls the "bootstrap_sample" function with the "bootstrapMeanList"
    # and stores the result in "finalbootstrapMean"    
    finalBootstrap = bootstrap_sample(bootstrapmeanList)
    
    # Returns finalbootstrapMean
    return finalBootstrap


def bootstrap_histogram(L, area, simulations):
    """
    

    Parameters
    ----------
    L : list
        user-inputted list of numbers
    area : float
        percentage of data to be trimmed
    simulations : integer
        Determines how many trimmed means will be calculated and appended to an
        empty list

    Returns
    -------
    p : histogram
        Histogram of the the list of bootstrap means obtained from the function
        "bootstrap_trimmed_mean"

    """
    
    # creates the list "finalbootstrapList" which is created by calling the 
    # function "bootstrap_trimmed_mean"
    finalbootstrapList = bootstrap_trimmed_mean(L, area, simulations)
    
    # creates the variable "widths_df" which creates a data frame with 
    # "finalbootstrapList" as the data and columns
    widths_df = pd.DataFrame(finalbootstrapList, columns = ["finalbootstrapList"])
    
    # creates the histogram "p" which is a histogram of the data in the list
    # "finalbootstrapList"
    p = (plotnine.ggplot(data = widths_df) +
    plotnine.aes(x = finalbootstrapList) +
    plotnine.geom_histogram()
    )
    
    # returns the histogram "p"
    return p



mydata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 50, 59]
bootstrap_sample(mydata)
trimmed_mean(mydata, 0.1)
bootstrap_trimmed_mean(mydata, 0.1, 10)
bootstrap_histogram(mydata, 0.1, 100)


    