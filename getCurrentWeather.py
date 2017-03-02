#! /usr/local/bin/python

import pyowm
#import stringcase

raised_exc = 0
x = 0

owm = pyowm.OWM('b3362437408e57646f5c22fe4e576f8e')

try:
    observation = owm.weather_at_place("Sheffield,uk")
    current_weather = observation.get_weather()
    location = observation.get_location().get_name().title()
except:
    raised_exc = -1
    print ('Failed to update!')
else:
    detailed = current_weather.get_detailed_status()
    temp = current_weather.get_temperature('celsius')
    cur_temp = temp['temp']

    ## change color depending on the temp
    if cur_temp > 22:
        temp_col = 'red'
    else:
        if cur_temp > 13:
            temp_col = 'green'
        else:
            temp_col = 'cyan'

    ## switch on Location
    locs = {
        'Sheffield': 'SHF',
    }

    if raised_exc == -1:
        str_out_1 = "#[bg=%s] #[fg=white][%s]#[fg=default]#[bg=default]" % ('black', 'N/A'.center(35))
    else:
        str_out_1_pre = "#[bg=%s]#[fg=black]" % (temp_col)
        str_out_1 = "%s: %s %sC" % (locs.get(location, 'N/A'), detailed.title(),int(round(cur_temp)))
        str_out_1_post = "#[fg=default]#[bg=default]"
        print ('Updated successfully!')

    file = open("/Users/dbelis/openweathermap.1", "w")
    file.write( str_out_1_pre + str_out_1.center(35) + str_out_1_post )
    file.close()


