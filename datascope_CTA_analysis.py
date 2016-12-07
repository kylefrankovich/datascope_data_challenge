# script to explore Chicago L stop data for Datascope data challenge:

# data origin: https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Daily-Totals/5neh-572f

# station information origin:
# https://data.cityofchicago.org/Transportation/CTA-System-Information-List-of-L-Stops/8pix-ypme

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

station_data.iloc[0]

station_data[station_data['STATION_NAME'] == 'Wilson']['Location']

station_data[station_data['MAP_ID'] == 41450]['Location'].iloc[0] # gives string of coordinates

string_coords = ''.join(c for c in station_data[station_data['MAP_ID'] == 41450]['Location'].iloc[0] if c not in '(){}<>')

coordinates = map(float, string_coords.split(','))

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

lolla_dates = ['07/28/2016', '07/29/2016', '07/30/2016', '07/31/2016',
               '07/31/2015', '08/01/2015', '08/02/2015',
               '08/01/2014', '08/02/2014', '08/03/2014',
               '08/02/2013', '08/03/2013', '08/04/2013',
               '08/03/2012', '08/04/2012', '08/05/2012']

data_filtered_data = data[data['date'].isin(lolla_dates)]

df[df['A'].isin([3, 6])]

len(data_filtered_data)/
len(data)


for e in station_data:
    print station_data['STATION_NAME']




inp = [{'c1':10, 'c2':100}, {'c1':11,'c2':110}, {'c1':12,'c2':120}]
df = pd.DataFrame(inp)

for index, row in df.iterrows():
    print row['c1'], row['c2']

for index, row in station_data.iterrows():
    #print row['Location']
    string_coords = ''.join(
        c for c in row['Location'] if c not in '(){}<>')

    # coordinates = map(float, string_coords.split(','))
    # coordinates = float(string_coords.split(','))
    coordinates = [float(i) for i in string_coords.split(',')]
    current_ID = row['MAP_ID']
    current_name = row['STOP_NAME']
    print coordinates, current_ID, current_name, index
