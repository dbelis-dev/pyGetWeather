#! /usr/local/bin/python

import pyowm
from datetime import date

raised_exc = 0
str_out_2 = ''

owm = pyowm.OWM('b3362437408e57646f5c22fe4e576f8e')

try:
    forecast = owm.three_hours_forecast("Sheffield,uk")
    f3 = forecast.get_forecast()
except:
    raised_exc = -1
    print ('Failed to update!')
else:
    if raised_exc == -1:
        str_out_2 = "#[bg=%s] #[fg=white][%s]#[fg=default]#[bg=default]" % ('black', 'N/A'.center(35))
    else:
        str_out_2_pre = "#[bg=cyan]#[fg=black]"
        pos = 0
        for weather3 in f3:
            if pos == 0:
                dt = weather3.get_reference_time(timeformat='date')
                str_out_2 += "%sh " % (dt.strftime("%H"))
            str_out_2 += "%s" % (weather3.get_status())
            if pos == 3: break
            pos += 1
            str_out_2 += ", "
        str_out_2_post = "#[fg=default]#[bg=default]"
        print ('Updated successfully!')

    file = open("/Users/dbelis/openweathermap.2", "w")
    file.write( str_out_2_pre + str_out_2.center(35) + str_out_2_post )
    file.close()


