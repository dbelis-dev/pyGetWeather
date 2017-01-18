#! /usr/bin/python3

import pyowm
#import stringcase

raised_exc = 0

owm = pyowm.OWM('b3362437408e57646f5c22fe4e576f8e')

try:
    observation = owm.weather_at_place("Sheffield,uk")
    current_weather = observation.get_weather()
    today_forecasts = owm.daily_forecast("Sheffield,uk", limit=1)
    today_forecast = today_forecasts.get_forecast()
except:
    raised_exc = -1
else:
    #short = current_weather.get_status()
    detailed = current_weather.get_detailed_status()
    temp = current_weather.get_temperature('celsius')
    cur_temp = temp['temp']
    for weather in today_forecast:
        temp_fc = weather.get_temperature('celsius')
        max_temp = temp_fc['max']
        min_temp = temp_fc['min']

    if cur_temp > 22:
        temp_col = 'red'
    else:
        if cur_temp > 13:
            temp_col = 'green'
        else:
            temp_col = 'cyan'

    if raised_exc == -1:
        str_out_1 = "#[bg=%s] #[fg=white][%s] #[fg=default]#[bg=default]" % ('black', 'N/A')
    else:
        str_out_1 = "#[bg=%s] #[fg=black]%s | %s #[fg=default]#[bg=default]" % (temp_col,detailed.title(),round(cur_temp,1))

    file = open("/home/vagrant/openweathermap.1", "w")
    file.write( str_out_1 )
    file.close()

