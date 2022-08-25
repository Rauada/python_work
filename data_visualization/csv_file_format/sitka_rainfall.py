import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = "data/sitka_weather_2018_simple.csv"

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get rainfall data and dates from this file.
	dates,rainfall_data = [],[]
	for row in reader:
		current_date = datetime.strptime(row[2],'%Y-%m-%d')
		rainfall = float(row[3])
		dates.append(current_date)
		rainfall_data.append(rainfall)

# Plot the rainfall data.
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,rainfall_data,c='blue')

# Format plot.
title = "Daily rainfall - 2018\nSitka, Alaska"
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (in)",fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()