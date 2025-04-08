import pandas as pd
import plotly.express as px

# Read the data
data = pd.read_excel(r"Dataset\Visakhapatnam_data.xlsx")

# Filter the dataset for Visakhapatnam
target_city = 'Visakhapatnam'
visakhapatnam_data = data[data['city'] == target_city]

# Line chart for AQI trends over time for Visakhapatnam
fig = px.line(visakhapatnam_data, x='date', y='aqi', title=f'AQI Trend for {target_city}')
fig.show()
fig.write_html("Visakhapatnam_1.jsp", auto_open=True)

# Scatter plot for AQI and PM10 with color-coded cities 
fig = px.scatter(visakhapatnam_data, x='pm10', y='aqi', title='AQI vs PM10 for Visakhapatnam')
fig.show()
fig.write_html("Visakhapatnam_2.jsp", auto_open=True)

# Box plot for AQI distribution in Visakhapatnam
fig = px.box(visakhapatnam_data, y='aqi', title='AQI Distribution in Visakhapatnam')
fig.show()
fig.write_html("Visakhapatnam_3.jsp", auto_open=True)

# Bubble chart for AQI, NO2, and SO2 with bubble size indicating PM2.5 levels in Visakhapatnam
fig = px.scatter(visakhapatnam_data, x='no2', y='so2', size='pm2_5', color='aqi', hover_name='city',
                 title='AQI, NO2, SO2, and PM2.5 Bubble Chart for Visakhapatnam')
fig.show()
fig.write_html("Visakhapatnam_4.jsp", auto_open=True)

# Sunburst chart for AQI distribution by pollutant in Visakhapatnam
fig = px.sunburst(visakhapatnam_data, path=['city', 'aqi'], values='pm10', title='AQI Distribution by Pollutant in Visakhapatnam')
fig.show()
fig.write_html("Visakhapatnam_5.jsp", auto_open=True)

# Heatmap for correlation between pollutants in Visakhapatnam
pollutants_corr = visakhapatnam_data[['aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].corr()
fig = px.imshow(pollutants_corr, labels=dict(x='Pollutants', y='Pollutants'), x=pollutants_corr.columns, y=pollutants_corr.columns, title='Correlation Heatmap in Visakhapatnam')
fig.show()
fig.write_html("Visakhapatnam_6.jsp", auto_open=True)

# Line chart for trends of various pollutants over time in Visakhapatnam
fig = px.line(visakhapatnam_data, x='date', y=['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3'], title='Pollutant Trends over Time in Visakhapatnam')
fig.show()
fig.write_html("Visakhapatnam_7.jsp", auto_open=True)

# Radar chart for the distribution of pollutants in Visakhapatnam
pollutants_avg = visakhapatnam_data[['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].mean().reset_index().rename(columns={0: 'Average'})
fig = px.line_polar(pollutants_avg, r='Average', theta='index', line_close=True, title='Average Pollutant Distribution in Visakhapatnam')
fig.show()
fig.write_html("Visakhapatnam_8.jsp", auto_open=True)
