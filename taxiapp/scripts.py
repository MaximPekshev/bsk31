import requests
import json
from .models import Driver, Car

def import_car():

	cars_url = 'https://fleet-api.taxi.yandex.net/v1/parks/cars/list'
	dr_headers = {'Accept-Language': 'ru',
	           'X-Client-ID': 'taxi/park/d720a2f94349461ab80d9c613b8e801c',
	           'X-API-Key': 'rrAqtFLKUQzNQTNPkh+WyCGzWfPbIvCxCUt+Iy'}

	cars_data = {
				"fields": {
				},
				"limit": 100,
				"query": {
				      "park": {
				        "id": 'd720a2f94349461ab80d9c613b8e801c'
				      },
			    },

	}

	answer = requests.post(cars_url, headers=dr_headers, data=json.dumps(cars_data),)
	response = answer.json()
	cars = response.get('cars')

	for car in cars:
		brand = car.get('brand')
		model = car.get('model')
		number = car.get('number')
		vin = car.get('vin')
		year = car.get('year')
		color = car.get('color')

		print(brand, number)

		new_car = Car(

			car_number = number,
			car_brand = brand,
			car_model = model,

			)

		new_car.save()

		print(new_car)
		print('--------------------------------------')


def link_cars():
	driver = Driver.objects.all()
	for dr in driver:
		num = dr.car_number.upper()

		try:
			car = Car.objects.get(car_number=num)
			dr.car = car
			dr.save()

			print(car, ' загружена успешно! для водителя ', dr)
			print('-------------------------------------------------')

		except car.DoesNotExist:

			print(num, ' номер в базе автомобилей не найден!')
			print('-------------------------------------------------')