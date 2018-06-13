import sys
import pandas as pd

from lib.preprocessing import *

SHOOTINGS_DATASET = 'datasets/fatal-police-shootings-data.csv'
SHOOTINGS_LATS_LONGS_DATASET = '../datasets/fatal-police-shootings-with-coords.csv'

if __name__ == '__main__':

    # Get dataset
    shootings_dataset = get_data()
    
    '''
    NOTE:
        The method works for a slice of 3 'city name state' strings, but won't work for a list 
        of every 'city name state' in dataset
    '''
    #get_geo_coords(shootings_dataset)
    #merge_coordinates()
    
     

   