import pandas as pd
SHOOTINGS_DATASET = '../datasets/fatal-police-shootings-data.csv'

if __name__ == '__main__':
    shootings_dataset = pd.read_csv(SHOOTINGS_DATASET)
    print(shootings_dataset)
