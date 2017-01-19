#! /usr/bin/python3

import pyowm

raised_exc = 0

owm = pyowm.OWM('b3362437408e57646f5c22fe4e576f8e')

try:
    forecast = owm.three_hours_forecast("Sheffield,uk")
    f3 = forecast.get_forecast()
except:
    raised_exc = -1
else:
    if raised_exc == -1:
        str_out_2 = "#[bg=%s] #[fg=white][%s] #[fg=default]#[bg=default]" % ('black', 'N/A')
    else:
        str_out_2 = "#[bg=cyan] "
        pos = 0
        for weather3 in f3:
            str_out_2 += "#[fg=black]%s#[fg=white]" % (weather3.get_status())
            if pos == 3: break
            pos += 1
            str_out_2 += "/"
        str_out_2 += " #[fg=default]#[bg=default]"

    file = open("/Users/dbelis/openweathermap.2", "w")
    file.write( str_out_2 )
    file.close()

