from pathlib import Path
import csv

import plotly.express as px

# Read data as a string and  convert to a list.
path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header = next(reader)
print(header)

# Extract data.
lons, lats, brts = [], [], []
for row in reader:
    lats.append(float(row[0]))
    lons.append(float(row[1]))
    brts.append(float(row[2]))
    date = row[5]

# Configure plot.
title = f"Fires in the last day: {date}"
min_val = min(brts)
max_val = max(brts)
sizes = [1 + (b - min_val) * (4 - 1) / (max_val - min_val)
        for b in brts]
fig = px.scatter_geo(lat=lats, lon=lons, size=sizes, title=title,
        color=brts,
        color_continuous_scale='inferno',
        labels={'color':'Brightness'},
        projection='natural earth',
    )
fig.show()
