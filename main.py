import pandas as pd
import plotly.express as px

# Load and process your data
data = pd.read_csv("Dataset/stations.csv")
data.dropna(inplace=True)

# Create the bar chart
count_data = data['State'].value_counts().reset_index()
count_data.columns = ['State', 'Count']
bar_fig = px.bar(count_data, x='State', y='Count', title='Count of Data Points by State', text='Count')
bar_fig.update_xaxes(categoryorder='total ascending')
bar_fig.update_layout(xaxis_title='State', yaxis_title='Count')
bar_fig.write_html('bar_chart.html')

# Create the pie chart
state_counts = data['State'].value_counts().reset_index()
state_counts.columns = ['State', 'Count']
pie_fig = px.pie(state_counts, names='State', values='Count', title='Distribution of Data Points by State', hole=0.3)
pie_fig.update_layout(width=800, height=800)
pie_fig.write_html('pie_chart.html')

print("HTML files generated: bar_chart.html and pie_chart.html")
