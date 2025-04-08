import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot

def generate_chart(data, parameter, chart_title):
    S = data.groupby('city')[parameter].max().sort_values(ascending=False).reset_index().round(2)

    trace_table = go.Table(
        domain=dict(x=[0, 0.4],
                    y=[0, 1.0]),
        header=dict(values=["city", parameter],
                    fill=dict(color='#119DFF'),
                    font=dict(color='white', size=12),
                    align=['center'],
                    height=30),
        cells=dict(values=[S['city'].head(10), S[parameter].head(10)],
                   fill=dict(color=['moccasin', 'white']),
                   align=['center']))

    trace_bar = go.Bar(x=S['city'].head(10),
                      y=S[parameter].head(10),
                      xaxis='x1',
                      yaxis='y1',
                      marker=dict(color='lime'), opacity=0.60)

    layout = dict(
        width=630,
        height=None,
        autosize=False,
        title=f'TOP 10 Cities with {chart_title}',
        showlegend=False,
        xaxis1=dict(**dict(domain=[0.5, 1], anchor='y1', showticklabels=True)),
        yaxis1=dict(**dict(domain=[0, 1.0], anchor='x1', hoverformat='.2f')),
    )

    fig = dict(data=[trace_table, trace_bar], layout=layout)

    # Save the chart as an HTML file
    plotly_file = f"{parameter}_chart.html"
    plot(fig, filename=plotly_file, auto_open=False)

# Example usage:
data = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Documents\\NetBeansProjects\\WebApplication1\\web\\HTML\\Dataset\\air_pollution_data.csv")

# Generate charts for different parameters
generate_chart(data, 'no', 'NO')
generate_chart(data, 'no2', 'NO2')
generate_chart(data, 'o3', 'O3')
generate_chart(data, 'so2', 'SO2')
generate_chart(data, 'pm2_5', 'PM2.5')
generate_chart(data, 'pm10', 'PM10')
generate_chart(data, 'nh3', 'NH3')
generate_chart(data, 'Parti_matt', 'Particulate Matter')
