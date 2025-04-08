import pandas as pd
import plotly.express as px

# Read the data for Patna
data = pd.read_excel(r"Dataset\Patna_data.xlsx")

# Filter the dataset for Patna
target_city = 'Patna'
patna_data = data[data['city'] == target_city]

# Line chart for AQI trends over time for Patna
fig = px.line(patna_data, x='date', y='aqi', title=f'AQI Trend for {target_city}')
fig.show()
fig.write_html("Patna_1.jsp", auto_open=True)

# Scatter plot for AQI and PM10 with color-coded cities 
fig = px.scatter(patna_data, x='pm10', y='aqi', title='AQI vs PM10 for Patna')
fig.show()
fig.write_html("Patna_2.jsp", auto_open=True)

# Box plot for AQI distribution in Patna
fig = px.box(patna_data, y='aqi', title='AQI Distribution in Patna')
fig.show()
fig.write_html("Patna_3.jsp", auto_open=True)

# Bubble chart for AQI, NO2, and SO2 with bubble size indicating PM2.5 levels in Patna
fig = px.scatter(patna_data, x='no2', y='so2', size='pm2_5', color='aqi', hover_name='city',
                 title='AQI, NO2, SO2, and PM2.5 Bubble Chart for Patna')
fig.show()
fig.write_html("Patna_4.jsp", auto_open=True)

# Sunburst chart for AQI distribution by pollutant in Patna
fig = px.sunburst(patna_data, path=['city', 'aqi'], values='pm10', title='AQI Distribution by Pollutant in Patna')
fig.show()
fig.write_html("Patna_5.jsp", auto_open=True)

# Heatmap for correlation between pollutants in Patna
pollutants_corr = patna_data[['aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].corr()
fig = px.imshow(pollutants_corr, labels=dict(x='Pollutants', y='Pollutants'), x=pollutants_corr.columns, y=pollutants_corr.columns, title='Correlation Heatmap in Patna')
fig.show()
fig.write_html("Patna_6.jsp", auto_open=True)

# Line chart for trends of various pollutants over time in Patna
fig = px.line(patna_data, x='date', y=['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3'], title='Pollutant Trends over Time in Patna')
fig.show()
fig.write_html("Patna_7.jsp", auto_open=True)

# Radar chart for the distribution of pollutants in Patna
pollutants_avg = patna_data[['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].mean().reset_index().rename(columns={0: 'Average'})
fig = px.line_polar(pollutants_avg, r='Average', theta='index', line_close=True, title='Average Pollutant Distribution in Patna')
fig.show()
fig.write_html("Patna_8.jsp", auto_open=True)
