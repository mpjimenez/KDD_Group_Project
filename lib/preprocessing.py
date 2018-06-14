import sys
import os
import pandas as pd 
import numpy as np
import csv
import time
import geocoder

SHOOTINGS_DATASET = 'datasets/fatal-police-shootings-data.csv'
FATAL_DATASET = 'datasets/fatal.csv'
COORDINATES_PATH = 'datasets/city_coordinates.csv'
COORDINATES_PATH1 = 'datasets/city_coordinates1.csv'
COORDINATES_PATH2 = 'datasets/city_coordinates2.csv'
COORDINATES_PATH3 = 'datasets/city_coordinates3.csv'
COORDINATES_PATH4 = 'datasets/city_coordinates4.csv'
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
    fatal = pd.read_csv(FATAL_DATASET)
    print(fatal)
    sys.exit()
    return shootings_dataset, fatal

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

    coords = city_states[1000:2000] 
    print(len(coords))
    ndx = 1000
    for city in coords:
        loc = geocoder.google(city, key = 'AIzaSyDTWezUHP0dMFyHBlHRlgP1Np35MJvlzEk')
        city_coordinates.update({city_states[ndx] : loc.latlng})
        print('{}: {}'.format(ndx, loc.latlng))
        ndx += 1
        

    results_file = csv.writer(open(COORDINATES_PATH2, 'w'))
    results_file.writerow(['Location ', 'Lat', 'Lon'])

    for val in city_coordinates:
        results_file.writerow([val, city_coordinates[val][0], city_coordinates[val][1]])
        print(val, city_coordinates[val][0], city_coordinates[val][1])

    end = time.time()
    print('It took {} seconds to get 1000 city coordinates!'.format(end - start))
    sys.exit()

def merge_coordinates():
    df = pd.read_csv(SHOOTINGS_DATASET)
    coords1 = pd.read_csv(COORDINATES_PATH1)
    coords2 = pd.read_csv(COORDINATES_PATH2)
    coords3 = pd.read_csv(COORDINATES_PATH3)
    coords4 = pd.read_csv(COORDINATES_PATH4)
   
    frames = [coords1, coords2, coords3, coords4]
    dataset_geo_coordinates = pd.concat(frames)
    dataset_geo_coordinates.reset_index(drop = True, inplace = True)
    dataset_geo_coordinates.to_csv(COORDINATES_PATH)
    sys.exit()


    