from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

def extract_data(filepath):
    """Retrieves the rainfall data from the .csv file."""

    path = Path(filepath)
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    # Extract dates and precipitation data.
    data = {}
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rainfall = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            data[current_date] = rainfall

    return data

path = 'weather_data/sitka_weather_2021_full.csv'
sitka_data = extract_data(path)
path = 'weather_data/death_valley_2021_full.csv'
valley_data = extract_data(path)

# Remove keys that don't appear in both datasets.
for key in list(sitka_data):
    if key not in valley_data:
        del sitka_data[key]
for key in list(valley_data):
    if key not in sitka_data:
        del valley_data[key]

# Plot the precipitation.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(sitka_data.keys(), sitka_data.values(), color='blue', alpha=0.5)
ax.plot(valley_data.keys(), valley_data.values(), color='red', alpha=0.5)
ax.fill_between(sitka_data.keys(), sitka_data.values(), valley_data.values(),
                facecolor='yellow', alpha=0.1)

# Format plot.
title = "Daily Rainfall Comparison Between\nSitka, AK, and Death Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (mm?)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
