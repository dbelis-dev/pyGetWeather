#! /usr/bin/python3

import pyowm
owm = pyowm.OWM('b3362437408e57646f5c22fe4e576f8e',version='2.5')
raised_exc = 0

#try:
obs = owm.weather_at_place("Sheffield,uk")
w = obs.get_weather()

fc = owm.daily_forecast("Sheffield,uk", limit=1)
f = fc.get_forecast()

fc3 = owm.three_hours_forecast("Sheffield,uk")
f3 = fc3.get_forecast()
#except:
#    raised_exc = -1
#else:
print(w.get_detailed_status())
print(w.get_temperature(unit='celsius'))

print ("Daily forecast")
for weather in f:
    #print(weather.get_reference_time('iso'),weather.get_detailed_status())
    print(weather.get_reference_time('iso'),weather.get_status(),weather.get_temperature(unit='celsius'))

#print ("3hr forecast")
#for weather3 in f3:
#    print(weather3.get_reference_time('iso'),weather3.get_status())

print ("Only first 4 values")
pos = 0
for weather3 in f3:
    print(weather3.get_reference_time('iso'),weather3.get_status())
    if pos == 3: break
    pos += 1
