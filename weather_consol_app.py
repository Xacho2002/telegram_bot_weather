import pyowm

city = "Vanadzor, ARM"

owm = pyowm.OWM("9b6cbef84565796f8f8e2c2d0f05f5e2")
# mgr = owm.weather_manager()

# observation = mgr.weather_at_place(city)
# w = observation.weather

# temp = w.temperature('celsius')['temp']

temp_cels = owm.weather_manager().weather_at_place(city).weather.temperature('celsius')['temp']
temp_far = owm.weather_manager().weather_at_place(city).weather.temperature('farengate')['temp']

print("tempriture in celsius = " + temp_cels + "\ntempriture in farengate = " + temp_far)