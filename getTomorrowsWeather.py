#! /usr/bin/python3

import pyowm
#import stringcase

raised_exc = 0
x = 0

owm = pyowm.OWM('b3362437408e57646f5c22fe4e576f8e')

try:
    multiday_forecasts = owm.daily_forecast("Sheffield,uk", limit=2)
    multiday_forecast = multiday_forecasts.get_forecast()
except:
    raised_exc = -1
else:
    for weather in multiday_forecast:
        ## skip today's forecast
        if x > 0:
            temp_fc = weather.get_temperature('celsius')
            max_temp = temp_fc['max']
            min_temp = temp_fc['min']
            detail_fc = weather.get_detailed_status()
        else:
            x += 1
            pass

    if raised_exc == -1:
        str_out_3 = "#[bg=%s] #[fg=white][%s] #[fg=default]#[bg=default]" % ('black', 'N/A')
    else:
        str_out_3_pre = "#[bg=yellow]#[fg=black]"
        str_out_3 = "%s [%s / %s]" % (detail_fc.title(), round(min_temp,1), round(max_temp,1))
        str_out_3_post = "#[fg=default]#[bg=default]"

    file = open("/Users/dbelis/openweathermap.3", "w")
    file.write( str_out_3_pre + str_out_3.center(35) + str_out_3_post )
    file.close()

