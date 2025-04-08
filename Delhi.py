import pandas as pd
import plotly.express as px
# Read the data for Delhi
delhi_data = pd.read_excel(r"Dataset\Delhi_data.xlsx")
# Filter the dataset for Delhi
target_city_delhi = 'Delhi'
delhi_data = delhi_data[delhi_data['city'] == target_city_delhi]
# Line chart for AQI trends over time for Delhi
fig = px.line(delhi_data, x='date', y='aqi', title=f'AQI Trend for {target_city_delhi}')
fig.show()
fig.write_html("Delhi_1.jsp", auto_open=True)

# Scatter plot for AQI and PM10 with color-coded cities for Delhi
fig = px.scatter(delhi_data, x='pm10', y='aqi', title='AQI vs PM10 for Delhi')
fig.show()
fig.write_html("Delhi_2.jsp", auto_open=True)

# Box plot for AQI distribution in Delhi
fig = px.box(delhi_data, y='aqi', title='AQI Distribution in Delhi')
fig.show()
fig.write_html("Delhi_3.jsp", auto_open=True)

# Bubble chart for AQI, NO2, and SO2 with bubble size indicating PM2.5 levels in Delhi
fig = px.scatter(delhi_data, x='no2', y='so2', size='pm2_5', color='aqi', hover_name='city',
                 title='AQI, NO2, SO2, and PM2.5 Bubble Chart for Delhi')
fig.show()
fig.write_html("Delhi_4.jsp", auto_open=True)

# Sunburst chart for AQI distribution by pollutant in Delhi
fig = px.sunburst(delhi_data, path=['city', 'aqi'], values='pm10', title='AQI Distribution by Pollutant in Delhi')
fig.show()
fig.write_html("Delhi_5.jsp", auto_open=True)

# Heatmap for correlation between pollutants in Delhi
pollutants_corr_delhi = delhi_data[['aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].corr()
fig = px.imshow(pollutants_corr_delhi, labels=dict(x='Pollutants', y='Pollutants'), x=pollutants_corr_delhi.columns, y=pollutants_corr_delhi.columns, title='Correlation Heatmap in Delhi')
fig.show()
fig.write_html("Delhi_6.jsp", auto_open=True)

# Line chart for trends of various pollutants over time in Delhi
fig = px.line(delhi_data, x='date', y=['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3'], title='Pollutant Trends over Time in Delhi')
fig.show()
fig.write_html("Delhi_7.jsp", auto_open=True)

# Radar chart for the distribution of pollutants in Delhi
pollutants_avg_delhi = delhi_data[['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].mean().reset_index().rename(columns={0: 'Average'})
fig = px.line_polar(pollutants_avg_delhi, r='Average', theta='index', line_close=True, title='Average Pollutant Distribution in Delhi')
fig.show()
fig.write_html("Delhi_8.jsp", auto_open=True)
