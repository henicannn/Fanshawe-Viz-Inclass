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
    stops[[ 'stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'stop_code']], on='stop_id')
stops_merge.head()
# stop_merge.shape

# %% Merge trips into stops_merge by trip_id
trips_merge = stops_merge.merge(
    trips[['trip_id', 'route_id']], on='trip_id')
trips_merge.head()

# %%
