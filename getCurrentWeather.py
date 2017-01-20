#! /usr/bin/python3

import pyowm
#import stringcase

raised_exc = 0
x = 0

owm = pyowm.OWM('b3362437408e57646f5c22fe4e576f8e')

try:
    observation = owm.weather_at_place("Sheffield,uk")
    current_weather = observation.get_weather()
except:
    raised_exc = -1
else:
    detailed = current_weather.get_detailed_status()
    temp = current_weather.get_temperature('celsius')
    cur_temp = temp['temp']

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
        str_out_1_pre = "#[bg=%s]#[fg=black]" % (temp_col)
        str_out_1 = "%s | %s" % (detailed.title(),round(cur_temp,1))
        str_out_1_post = "#[fg=default]#[bg=default]"

    file = open("/Users/dbelis/openweathermap.1", "w")
    file.write( str_out_1_pre + str_out_1.center(35) + str_out_1_post )
    file.close()

