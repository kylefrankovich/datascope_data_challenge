# script to explore Chicago L stop data for Datascope data challenge:

# data origin: https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Daily-Totals/5neh-572f

# station information origin: https://data.cityofchicago.org/Transportation/CTA-System-Information-List-of-L-Stops/8pix-ypme

# interactive map resource: https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/

# load CSV data:

import pandas as pd

# data location (keep raw data off of github):

path_to_data = '/Users/kylefrankovich/Desktop/datascope_CTA_data/' \
               'CTA_-_Ridership_-__L__Station_Entries_-_Daily_Totals.csv'

path_to_station_info = '/Users/kylefrankovich/Desktop/datascope_CTA_data/' \
                       'CTA_-_System_Information_-_List_of__L__Stops.csv'


data = pd.read_csv(path_to_data)

station_data = pd.read_csv(path_to_station_info)

print(len(data)) # 809326 rows, matches data from CTA data site

print(len(station_data)) # 300 rows, matches data from CTA data site

# let's see what we got:

data.head()

station_data.head()

data.columns # list of column names

station_data.columns

data.describe()

data.iloc[0]

data.isnull().values.any()
# looks like we have no missing data. dope.

station_names = data.stationname.unique()

len(station_names) # 147 station names

station_IDs = data.station_id.unique()

len(station_IDs) # 146 station IDs

map_IDs = station_data.MAP_ID.unique()

len(map_IDs) # 144 map IDs; NB: it appears that map IDs from this dataset
# matches with station IDs in the main dataset, although there is a mismatch in
# number (146 vs. 144)






