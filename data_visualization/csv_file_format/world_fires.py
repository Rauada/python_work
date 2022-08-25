import csv
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Get latitude, longitude and brightness from this file.
	lats,lons,brights = [],[],[]
	for row in reader:
		lats.append(float(row[0]))
		lons.append(float(row[1]))
		brights.append(float(row[2]))

# Map the fires.
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    # 'text':hover_texts,
    'marker':{
    'size':[5*bright for bright in brights],
    'color':brights,
    'colorscale':'Reds',
    # 'reversescale':True,
    'colorbar':{'title':'Brightness'}
    },
}]

my_layout = Layout(title='World Fires Past Day')

fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='world_fires.html')