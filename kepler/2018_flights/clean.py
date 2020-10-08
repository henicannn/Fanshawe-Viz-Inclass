# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'kepler/2018_flights'))
    print(os.getcwd())
except:
    pass

# %%
import pandas as pd

# %% Import Data
flights = pd.read_csv('./data/Cleaned_2018_Flights.csv')
flights.head()

# %% Check the airport data
airports = pd.read_csv('./data/GlobalAirportDatabase.csv', names=[
    'Airport ID',
    'Name', 'City',
    'Country', 'IATA',
    'ICAO', 'Latitude',
    'Longitude', 'Altitude',
    'Timezpne', 'DST',
    'Tz database time zone',
    'Type', 'Source'
])

airports.head()

# %%
airports.to_csv('./data/formatted_airports.csv', index=False)

# %% Look up the origin lat/lng
flights_full = flights.merge(
    airports[['IATA', 'Longitude', 'Latitude']], left_on='Origin', right_on='IATA')
flights_full.head()

# %% Clean up the origin
flights_full['origin_lat'] = flights_full['Latitude']
flights_full['origin_long'] = flights_full['Longitude']
flights_full = flights_full.drop(['Latitude', 'Longitude', 'IATA'], axis=1)
flights_full.head()

# %%
flights_dest = flights_full.merge(
    airports[['IATA', 'Longitude', 'Latitude']], left_on='Dest', right_on='IATA')
flights_dest.head()
# %%

flights_dest['dest_lat'] = flights_dest['Latitude']
flights_dest['dest_long'] = flights_dest['Longitude']
flights_dest = flights_dest.drop(['Latitude', 'Longitude', 'IATA'], axis=1)
flights_dest.head()
# flights_dest.shape
# %%
flights_part_clean = flights_dest
flights_part_clean.head()

# %%

s1 = flights_part_clean[flights_part_clean['Quarter'] == 1].sample(5000).index
s2 = flights_part_clean[flights_part_clean['Quarter'] == 2].sample(5000).index
s3 = flights_part_clean[flights_part_clean['Quarter'] == 3].sample(5000).index
s4 = flights_part_clean[flights_part_clean['Quarter'] == 4].sample(5000).index

flights_clean = flights_part_clean.loc[s1.union(s2).union(s3).union(s4)]
flights_clean.head()
# %%

flights_clean.shape

# %%
flights_clean.to_csv('./data/simplified_flights.csv')

# %%
