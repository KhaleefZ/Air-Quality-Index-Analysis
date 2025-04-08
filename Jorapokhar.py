import pandas as pd
import plotly.express as px

# Read the data for Jorapokhar
data = pd.read_excel(r"Dataset\Jorapokhar_data.xlsx")

# Filter the dataset for Jorapokhar
target_city = 'Jorapokhar'
jorapokhar_data = data[data['city'] == target_city]

# Line chart for AQI trends over time for Jorapokhar
fig = px.line(jorapokhar_data, x='date', y='aqi', title=f'AQI Trend for {target_city}')
fig.show()
fig.write_html("Jorapokhar_1.jsp", auto_open=True)

# Scatter plot for AQI and PM10 with color-coded cities 
fig = px.scatter(jorapokhar_data, x='pm10', y='aqi', title='AQI vs PM10 for Jorapokhar')
fig.show()
fig.write_html("Jorapokhar_2.jsp", auto_open=True)

# Box plot for AQI distribution in Jorapokhar
fig = px.box(jorapokhar_data, y='aqi', title='AQI Distribution in Jorapokhar')
fig.show()
fig.write_html("Jorapokhar_3.jsp", auto_open=True)

# Bubble chart for AQI, NO2, and SO2 with bubble size indicating PM2.5 levels in Jorapokhar
fig = px.scatter(jorapokhar_data, x='no2', y='so2', size='pm2_5', color='aqi', hover_name='city',
                 title='AQI, NO2, SO2, and PM2.5 Bubble Chart for Jorapokhar')
fig.show()
fig.write_html("Jorapokhar_4.jsp", auto_open=True)

# Sunburst chart for AQI distribution by pollutant in Jorapokhar
fig = px.sunburst(jorapokhar_data, path=['city', 'aqi'], values='pm10', title='AQI Distribution by Pollutant in Jorapokhar')
fig.show()
fig.write_html("Jorapokhar_5.jsp", auto_open=True)

# Heatmap for correlation between pollutants in Jorapokhar
pollutants_corr = jorapokhar_data[['aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].corr()
fig = px.imshow(pollutants_corr, labels=dict(x='Pollutants', y='Pollutants'), x=pollutants_corr.columns, y=pollutants_corr.columns, title='Correlation Heatmap in Jorapokhar')
fig.show()
fig.write_html("Jorapokhar_6.jsp", auto_open=True)

# Line chart for trends of various pollutants over time in Jorapokhar
fig = px.line(jorapokhar_data, x='date', y=['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3'], title='Pollutant Trends over Time in Jorapokhar')
fig.show()
fig.write_html("Jorapokhar_7.jsp", auto_open=True)

# Radar chart for the distribution of pollutants in Jorapokhar
pollutants_avg = jorapokhar_data[['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].mean().reset_index().rename(columns={0: 'Average'})
fig = px.line_polar(pollutants_avg, r='Average', theta='index', line_close=True, title='Average Pollutant Distribution in Jorapokhar')
fig.show()
fig.write_html("Jorapokhar_8.jsp", auto_open=True)
