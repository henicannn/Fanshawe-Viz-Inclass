# %%
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'kepler/london_transit'))
    print(os.getcwd())
except:
    pass

# %% Import all packages
import pandas as pd


# %% Import Data
stops = pd.read_csv('./data/stops.csv')
trips = pd.read_csv('./data/trips.csv')
stop_times = pd.read_csv('./data/stop_times.csv')

print(stops, trips, stop_times)

# %% Merge stops into stop_times by stop_id
stops_merge = stop_times.merge(
    stops[['stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'stop_code']], on='stop_id')
stops_merge.head()


# %% Merge trips into stops_merge by trip_id
trips_merge = stops_merge.merge(
    trips[['trip_id', 'route_id']], on='trip_id')
trips_merge.head()

# %%Customize function
def validate_time(date_str):
    x = int(date_str, split(':', 1)[0])
    if x >= 24:
        return str(x%24) + date_str[2:]
    else:
        return date_str

# %% Clean the time format
trips_merge['arrival_time'] = trips_merge['arrival_time'].apply(
    lambda x: x.replace(' ', '0')
)

trips_merge['departure_time'] = trips_merge['departure_time'].apply(
    lambda x: x.replace(' ', '0')
)



# %% Convert arrival_time and departure_time to be time
trips_merge['arrival_time'] = pd.to_datetime(
    trips_merge['arrival_time'], format='%H:%M:%S').dt.time
trips_merge['departure_time'] = pd.to_datetime(
    trips_merge['departure_time'], format='%H:%M:%S').dt.time


# %% Export to new csv
trips_merge.to_csv('./data/full_trips.csv')

# %%
