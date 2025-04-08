import pandas as pd
import plotly.express as px

# Read the data for Lucknow
data = pd.read_excel(r"Dataset\Lucknow_data.xlsx")  # Update the file path for Lucknow data

# Filter the dataset for Lucknow
target_city = 'Lucknow'
lucknow_data = data[data['city'] == target_city]

# Line chart for AQI trends over time for Lucknow
fig = px.line(lucknow_data, x='date', y='aqi', title=f'AQI Trend for {target_city}')
fig.show()
fig.write_html("Lucknow_1.jsp", auto_open=True)

# Scatter plot for AQI and PM10 with color-coded cities 
fig = px.scatter(lucknow_data, x='pm10', y='aqi', title='AQI vs PM10 for Lucknow')
fig.show()
fig.write_html("Lucknow_2.jsp", auto_open=True)

# Box plot for AQI distribution in Lucknow
fig = px.box(lucknow_data, y='aqi', title='AQI Distribution in Lucknow')
fig.show()
fig.write_html("Lucknow_3.jsp", auto_open=True)

# Bubble chart for AQI, NO2, and SO2 with bubble size indicating PM2.5 levels in Lucknow
fig = px.scatter(lucknow_data, x='no2', y='so2', size='pm2_5', color='aqi', hover_name='city',
                 title='AQI, NO2, SO2, and PM2.5 Bubble Chart for Lucknow')
fig.show()
fig.write_html("Lucknow_4.jsp", auto_open=True)

# Sunburst chart for AQI distribution by pollutant in Lucknow
fig = px.sunburst(lucknow_data, path=['city', 'aqi'], values='pm10', title='AQI Distribution by Pollutant in Lucknow')
fig.show()
fig.write_html("Lucknow_5.jsp", auto_open=True)

# Heatmap for correlation between pollutants in Lucknow
pollutants_corr = lucknow_data[['aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].corr()
fig = px.imshow(pollutants_corr, labels=dict(x='Pollutants', y='Pollutants'), x=pollutants_corr.columns, y=pollutants_corr.columns, title='Correlation Heatmap in Lucknow')
fig.show()
fig.write_html("Lucknow_6.jsp", auto_open=True)

# Line chart for trends of various pollutants over time in Lucknow
fig = px.line(lucknow_data, x='date', y=['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3'], title='Pollutant Trends over Time in Lucknow')
fig.show()
fig.write_html("Lucknow_7.jsp", auto_open=True)

# Radar chart for the distribution of pollutants in Lucknow
pollutants_avg = lucknow_data[['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].mean().reset_index().rename(columns={0: 'Average'})
fig = px.line_polar(pollutants_avg, r='Average', theta='index', line_close=True, title='Average Pollutant Distribution in Lucknow')
fig.show()
fig.write_html("Lucknow_8.jsp", auto_open=True)
