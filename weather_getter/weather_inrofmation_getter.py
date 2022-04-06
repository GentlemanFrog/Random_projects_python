# We will be using open weather map api:
# https://home.openweathermap.org

import requests  # import needed for using api
from pprint import pprint
from collections import defaultdict
import pandas as pd
# proper way to import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# After sending request api from open weather is sending response in jason format
# we have to handle that .jason file to get proper output form city we want to lokate and get info
# about weather. In handling json format files pprint library will help to read this and get output

API_KEY = 'generated_api_key_From_openweather'
# city = input('Write city name: ')


# importing cities names from list to working on it
with open('weather_getter/list_of_cities.txt') as f:
    cities = f.read().splitlines()

#print(cities)

# it is url where we wanna send response: to make propoer url we adding key by concatenation
# and give city name to querry for search
# base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city

# weather_data = requests.get(base_url).json()

# pprint(weather_data)

# need defauldict: created dict will know that base value is list and now we don't use = but append cos
# we add somthing to list
cities_data_dict = defaultdict(list)
# we gonna take few cities ang get the comparasion:
for city in cities:
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q=" + city
    weather_data = requests.get(base_url).json()
    # if base is empty then it means no data:
    if not weather_data['base']:
        print('No data found ')
        pass
    else:
        cities_data_dict['city_name'].append(weather_data["name"])
        cities_data_dict['country_shortcut'].append(weather_data["sys"]["country"])
        cities_data_dict['temp_feels_like'].append(weather_data["main"]["feels_like"])
        cities_data_dict['temp'].append(weather_data["main"]["temp"])
        cities_data_dict['pressure'].append(weather_data["main"]["pressure"])
        cities_data_dict['wind'].append(weather_data['wind']['speed']) # in m/s


# print(cities_data_dict)
df = pd.DataFrame.from_dict(cities_data_dict)
#print(df)

# making plot of data:
# fig = px.bar(df, x='city_name', y='temp_feels_like', color='city_name')

# fig = make_subplots(rows=2, cols=2, subplot_titles=('Temp feels like', "Temp mesured", "Pressure", "Wind"))
# fig.add_trace(go.Bar(x=df[['city_name']], y=df[['temp_feels_like']]), row=1, col=1)
# fig.add_trace(go.Bar(x=df[['city_name']], y=df[['temp']]), row=1, col=2)
# fig.add_trace(go.Bar(x=df[['city_name']], y=df[['pressure']]), row=2, col=1)
# fig.add_trace(go.Bar(x=df[['city_name']], y=df[['wind']]), row=2, col=2)

# Plot of prameters in comparison to cities
fig = go.Figure()
fig.add_trace(go.Bar(x=df['city_name'], y=df['temp_feels_like'], name='Temp feels like (K)'))
fig.add_trace(go.Bar(x=df['city_name'], y=df['temp'], name='Temp mesured (K)'))
fig.add_trace(go.Bar(x=df['city_name'], y=df['pressure'], name='Pressure (hPa)'))
fig.add_trace(go.Bar(x=df['city_name'], y=df['wind'], name='Wind (m/s)'))

fig.update_layout(barmode='group')
fig.show()


