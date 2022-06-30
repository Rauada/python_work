def make_car(manufacturer,model,**kyargs):
	kyargs['Manufacturer'] = manufacturer.title()
	kyargs['Model'] = model.title()
	return kyargs

car_info = make_car('subaru','impreza',Year=2010,Mileage='10.000km')
print(car_info)