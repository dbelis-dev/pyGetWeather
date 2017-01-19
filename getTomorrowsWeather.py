#! /usr/bin/python3

import pyowm

raised_exc = 0

owm = pyowm.OWM('b3362437408e57646f5c22fe4e576f8e')

try:
    forecast = owm.three_hours_forecast("Sheffield,uk")
    tomorrow_morning = pyowm.timeutils.tomorrow(6,0)
    tomorrow_morning_forecast = forecast.get_weather_at(tomorrow_morning).get_status()
    tomorrow_noon = pyowm.timeutils.tomorrow(12,0)
    tomorrow_noon_forecast = forecast.get_weather_at(tomorrow_noon).get_status()
    tomorrow_evening = pyowm.timeutils.tomorrow(18,0)
    tomorrow_evening_forecast = forecast.get_weather_at(tomorrow_evening).get_status()
    tomorrow_night = pyowm.timeutils.tomorrow(23,59)
    tomorrow_night_forecast = forecast.get_weather_at(tomorrow_night).get_status()
except:
    raised_exc = -1
else:
    if raised_exc == -1:
        str_out_3 = "#[bg=%s] #[fg=white][%s] #[fg=default]#[bg=default]" % ('black', 'N/A')
    else:
        str_out_3 = "#[bg=yellow] #[fg=white]%s#[fg=black]/#[fg=white]%s#[fg=black]/#[fg=white]%s#[fg=black]/#[fg=white]%s #[fg=default]#[bg=default]" % (tomorrow_morning_forecast, tomorrow_noon_forecast, tomorrow_evening_forecast, tomorrow_night_forecast)

    file = open("/Users/dbelis/openweathermap.3", "w")
    file.write( str_out_3 )
    file.close()

