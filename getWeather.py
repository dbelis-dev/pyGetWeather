#! /usr/bin/env python

import pyowm

owm = pyowm.OWM('b3362437408e57646f5c22fe4e576f8e')

try:
    observation = owm.weather_at_place("Sheffield,GB")
    current_weather = observation.get_weather()

    detailed = current_weather.get_detailed_status()
    short = current_weather.get_status()
    humidity = current_weather.get_humidity()
    temp = current_weather.get_temperature('celsius')
    max_temp = temp['temp_max']
    min_temp = temp['temp_min']
    cur_temp = temp['temp']

    #print(detailed)
    #print(short)
    #print(humidity)
    #print(round(max_temp))
    #print(min_temp)
    #print(round(cur_temp,1))

    if cur_temp > 22:
        temp_col = 'red'
    else:
        if cur_temp > 13:
            temp_col = 'green'
        else:
            temp_col = 'cyan'

    file = open("./openweathermap.out", "w")
    file.write("#[bg=%s] #[fg=white][%s] %s#[fg=black] | %s/%s #[fg=default]#[bg=default]" % (temp_col,short,round(cur_temp,1),round(min_temp),round(max_temp)))
    file.close()
except:
    file = open("./openweathermap.out", "w")
    file.write("#[bg=%s] #[fg=white][%s] #[fg=default]#[bg=default]" % ('black', 'N/A'))
    file.close()
 
