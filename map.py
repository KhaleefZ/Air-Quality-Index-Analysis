import pandas as pd
import plotly.express as px

# Read the air pollution data
data = pd.read_csv(r"Dataset\air_pollution_data.csv")

# Read the India data
dt = pd.read_csv(r"Dataset\India.csv")

# Assuming dt is your DataFrame
fig = px.scatter_geo(dt,
                     lat='lat',
                     lon='lng',
                     color='city',
                     scope='asia',
                     title='Cities in India',
                     width= None,  # Set width to None for full screen
                     height= 600,  # Set height to None for full screen
                     hover_data=['city', 'population', 'capital'])

# Use the 'text' parameter to customize hover text
fig.update_traces(
    text='<b>' + dt['city'] + '</b><br>Population: ' + dt['population'].astype(str) + '<br>Capital: ' + dt['capital']
)

fig.update_layout(
    geo=dict(showcountries=True, countrycolor="Black")
)

fig.update_geos(projection_type="natural earth")

fig.update_traces(
    hoverinfo="text+lat+lon"  # Corrected hoverinfo combination
)

fig.write_html("scatter_map_plot_hover_details.jsp")
