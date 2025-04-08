import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px

data = pd.read_csv(r"Dataset\air_pollution_data.csv")
# Assuming your dataset has a column named 'City' containing the city names
city_column_name = 'city'

# Get unique city names from the dataset
unique_cities = data[city_column_name].unique()

# Scatter plot for AQI and PM10 with color-coded cities
fig1 = px.scatter(data, x='pm10', y='aqi', color='city', title='AQI vs PM10 by City')
fig1.write_html("scatter_aqi_pm10.jsp")

# Box plot for AQI distribution by city
fig2 = px.box(data, x='city', y='aqi', title='AQI Distribution Across Cities')
fig2.update_xaxes(tickangle=45)
fig2.write_html("box_aqi_distribution.jsp")

# Bubble chart for AQI, NO2, and SO2 with bubble size indicating PM2.5 levels
fig3 = px.scatter(data, x='no2', y='so2', size='pm2_5', color='aqi', hover_name='city',
                  title='AQI, NO2, SO2, and PM2.5 Bubble Chart')
fig3.write_html("bubble_chart_aqi_no2_so2_pm25.jsp")

# Sunburst chart for AQI distribution by city and pollutant
fig4 = px.sunburst(data, path=['city', 'aqi'], values='pm10', title='AQI Distribution by City and Pollutant')
fig4.write_html("sunburst_aqi_distribution.jsp")
