import sys
import os
import pandas as pd 
import numpy as np
import csv
import time
import geocoder

SHOOTINGS_DATASET = 'datasets/fatal-police-shootings-data.csv'
COORDINATES_PATH = 'datasets/city_coordinates.csv'
SHOOTINGS_LATS_LONGS_DATASET = '../datasets/fatal-police-shootings-with-coords.csv'

def get_data():
    '''
    parameters:
    -----------
        None

    return:
    ------
        shooting_dataset : Pandas Dataframe
    '''
    shootings_dataset = pd.read_csv(SHOOTINGS_DATASET)
    return shootings_dataset

def get_geo_coords(shootings_dataset):
    '''
    parameters:
    -----------
        shootings_dataset : Pandas Dataframe

    return:
        Not Sure
    -------
    '''
    start = time.time()
    city_states = []
    city_coordinates = {}
    # get lists of cities and states 3,399 cities and states in dataset
    cities = shootings_dataset['city'].tolist()
    states = shootings_dataset['state'].tolist()
    
    # append all (city, state) tuples to city_state_tuples
    for city, state in zip(cities, states):
        city_states.append(city + ' ' + state)

    
    test = city_states[:3]
    # Testing only 3 city_states
    coords = geocoder.mapquest(test, method = 'batch', key = 'put_key_here')
    #coords = geocoder.mapquest(city_states, method = 'batch', key = 'put_key_here')

    ndx = 0
    for location in coords:
        #print(location.address, location.latlng)
        city_coordinates.update({city_states[ndx] : location.latlng})
        ndx += 1

    results_file = csv.writer(open(COORDINATES_PATH, 'w'))
    results_file.writerow(['Location ', 'Lat', 'Lon'])

    for loc in city_coordinates:
        results_file.writerow([loc, city_coordinates[loc][0], city_coordinates[loc][1]])
        print(loc, city_coordinates[loc][0], city_coordinates[loc][1])

    end = time.time()
    print('It took {} seconds to get 3,399 city coordinates!'.format(end - start))
    sys.exit()
    