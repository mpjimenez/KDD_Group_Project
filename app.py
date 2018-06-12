import sys
import pandas as pd

from lib.preprocessing import *

SHOOTINGS_DATASET = 'datasets/fatal-police-shootings-data.csv'
SHOOTINGS_LATS_LONGS_DATASET = '../datasets/fatal-police-shootings-with-coords.csv'

if __name__ == '__main__':

    # Get dataset
    shootings_dataset = get_data()
    
    # Get lat, lon of each (city, state) in dataset
    get_geo_coords(shootings_dataset)
    sys.exit()
     

   