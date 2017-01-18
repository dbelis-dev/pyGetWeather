#! /usr/bin/python3

import pyowm
owm = pyowm.OWM('b3362437408e57646f5c22fe4e576f8e')
raised_exc = 0

try:
    forecast = owm.daily_forecast("Sheffield,GB",3)
    #forecast = owm.get_forecast()
    day1_morning = pyowm.timeutils.tomorrow(6,0)
    tomorrow_minTemp_forecast = forecast.will_have_clouds()
    print (tomorrow_minTemp_forecast)
    tomorrow_rainy_forecast = forecast.will_have_rain()
except:
    raised_exc = -1
else:
    if raised_exc == -1:
        str_out_3 = "#[bg=red] #[fg=white][FC:%s] #[fg=default]#[bg=default]" % ('black', 'N/A')
    else:
        str_out_3 = "#[bg=yellow] #[fg=white]%s#[fg=black]/#[fg=white]%s #[fg=default]#[bg=default]" % (tomorrow_minTemp_forecast, tomorrow_rainy_forecast)

    file = open("/home/vagrant/openweathermap.3", "w")
    file.write( str_out_3 )
    file.close()
