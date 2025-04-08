import pandas as pd
import plotly.express as px

# Read the data for Bengaluru
data = pd.read_excel(r"Dataset\Bengaluru_data.xlsx")

# Filter the dataset for Bengaluru
target_city = 'Bengaluru'
bengaluru_data = data[data['city'] == target_city]

# Line chart for AQI trends over time for Bengaluru
fig = px.line(bengaluru_data, x='date', y='aqi', title=f'AQI Trend for {target_city}')
fig.show()
fig.write_html("Bengaluru_1.jsp", auto_open=True)

# Scatter plot for AQI and PM10 with color-coded cities 
fig = px.scatter(bengaluru_data, x='pm10', y='aqi', title='AQI vs PM10 for Bengaluru')
fig.show()
fig.write_html("Bengaluru_2.jsp", auto_open=True)

# Box plot for AQI distribution in Bengaluru
fig = px.box(bengaluru_data, y='aqi', title='AQI Distribution in Bengaluru')
fig.show()
fig.write_html("Bengaluru_3.jsp", auto_open=True)

# Bubble chart for AQI, NO2, and SO2 with bubble size indicating PM2.5 levels in Bengaluru
fig = px.scatter(bengaluru_data, x='no2', y='so2', size='pm2_5', color='aqi', hover_name='city',
                 title='AQI, NO2, SO2, and PM2.5 Bubble Chart for Bengaluru')
fig.show()
fig.write_html("Bengaluru_4.jsp", auto_open=True)

# Sunburst chart for AQI distribution by pollutant in Bengaluru
fig = px.sunburst(bengaluru_data, path=['city', 'aqi'], values='pm10', title='AQI Distribution by Pollutant in Bengaluru')
fig.show()
fig.write_html("Bengaluru_5.jsp", auto_open=True)

# Heatmap for correlation between pollutants in Bengaluru
pollutants_corr = bengaluru_data[['aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].corr()
fig = px.imshow(pollutants_corr, labels=dict(x='Pollutants', y='Pollutants'), x=pollutants_corr.columns, y=pollutants_corr.columns, title='Correlation Heatmap in Bengaluru')
fig.show()
fig.write_html("Bengaluru_6.jsp", auto_open=True)

# Line chart for trends of various pollutants over time in Bengaluru
fig = px.line(bengaluru_data, x='date', y=['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3'], title='Pollutant Trends over Time in Bengaluru')
fig.show()
fig.write_html("Bengaluru_7.jsp", auto_open=True)

# Radar chart for the distribution of pollutants in Bengaluru
pollutants_avg = bengaluru_data[['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].mean().reset_index().rename(columns={0: 'Average'})
fig = px.line_polar(pollutants_avg, r='Average', theta='index', line_close=True, title='Average Pollutant Distribution in Bengaluru')
fig.show()
fig.write_html("Bengaluru_8.jsp", auto_open=True)
