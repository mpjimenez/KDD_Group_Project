import time
import pandas as pd
from geopy.geocoders import GoogleV3

SHOOTINGS_DATASET = '../datasets/fatal-police-shootings-data.csv'
SHOOTINGS_LATS_LONGS_DATASET = '../datasets/fatal-police-shootings-with-coords.csv'

if __name__ == '__main__':
    # Import dataset
    shootings_dataset = pd.read_csv(SHOOTINGS_DATASET)

     # Add 2 new columns for lat and long coords
    shootings_dataset['latitude'] = 0
    shootings_dataset['longitude'] = 0

    # { city_name : (lat, long)}
    city_coords = {}

    # Append lat and long coords for each row
    for index, row in shootings_dataset.iterrows():
        location = row['city'] + ' ' + row['state']

        # Sleep
        time.sleep(5) # 3 Seconds

        # IF location in hashmap, append lat and long coords
        if location in city_coords:
            row['latitude'] = city_coords[location][0]
            row['longitude'] = city_coords[location][1]
        else:
            geolocator = GoogleV3(format_string="%s, {}".format(location))
            address, (latitude, longitude) = geolocator.geocode("")
            city_coords[location] = (latitude, longitude)

            row['latitude'] = latitude
            row['longitude'] = longitude

            print('New Coord:', location, str(latitude), str(longitude))

    # Save new dataframe
    shootings_dataset.to_csv(SHOOTINGS_LATS_LONGS_DATASET)
