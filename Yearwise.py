import pandas as pd
import plotly.express as px
import plotly.offline as pyo
import os

# Load data from Excel file
data = pd.read_excel(r"Dataset\Visakhapatnam_data.xlsx")

# Filter the dataset for Visakhapatnam
target_city = 'Visakhapatnam'
visakhapatnam_data = data[data['city'] == target_city]

# Convert 'date' column to datetime format with multiple possible formats
formats = ['%m/%d/%Y', '%d-%m-%Y']

for fmt in formats:
    try:
        data['date'] = pd.to_datetime(data['date'], format=fmt, errors='coerce', dayfirst=True)
        break  # Break out of the loop if successful
    except ValueError:
        pass  # Continue to the next format if the current one fails

# Extract year from the 'date' column
data['year'] = data['date'].dt.year

# List of unique years in the dataset
unique_years = data['year'].unique()

# Create a directory to store the HTML files
output_directory = "output_html_files"
os.makedirs(output_directory, exist_ok=True)

# Define a list of AQI chart types
aqi_chart_types = ['line', 'scatter', 'box', 'scatter', 'sunburst', 'bar', 'imshow', 'line']

# Perform analysis for each year
for year in unique_years:
    # Filter data for the current year
    year_data = data[data['year'] == year]

    # Generate and save HTML files for each AQI chart type
    for chart_type in aqi_chart_types:
        # Generate chart using Plotly Express
        if chart_type == 'imshow':
            pollutants_corr_year = year_data[['aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].corr()
            fig = px.imshow(pollutants_corr_year, labels=dict(x='Pollutants', y='Pollutants'), 
                            x=pollutants_corr_year.columns, y=pollutants_corr_year.columns,
                            title=f'AQI {chart_type.capitalize()} for {year}')
        elif chart_type == 'sunburst':
            fig = px.sunburst(year_data, path=['city', 'aqi'], values='pm10', title=f'AQI {chart_type.capitalize()} for {year}')
        elif chart_type == 'line':
            fig = px.line_polar(year_data, r=year_data[['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']].mean(),
                                theta=['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3'],
                                title=f'AQI {chart_type.capitalize()} for {year}')
        else:
            chart_function = getattr(px, chart_type)
            fig = chart_function(year_data, x='date', y='aqi', title=f'AQI {chart_type.capitalize()} for {year}')

        # Save the AQI chart content to an HTML file
        file_path = os.path.join(output_directory, f'{year}_aqi_{chart_type}_chart.html')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(pyo.plot(fig, output_type='div', include_plotlyjs=True))

# Print a message indicating the completion of the process
print(f"AQI Charts saved to {output_directory}")
