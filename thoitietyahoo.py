from yahoo_weather.weather import YahooWeather
from yahoo_weather.api_handler import request_api, get_city_url, get_location_url
from yahoo_weather.classes.API_param import yahoo_API_parameters
from yahoo_weather.classes.atmosphere import Atmosphere
from yahoo_weather.classes.astronomy import Astronomy
from yahoo_weather.classes.condition import Condition
from yahoo_weather.classes.current_observation import Current_Observation
from yahoo_weather.classes.current_weather import Current_Weather
from yahoo_weather.classes.forecasts import Forecasts
from yahoo_weather.classes.location import Location
from yahoo_weather.classes.wind import Wind
from yahoo_weather.config.units import Unit

data = YahooWeather(APP_ID="7QMMCcOS",api_key="dj0yJmk9MlFpQTFrQnNYamx4JmQ9WVdrOU4xRk5UVU5qVDFNbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTU5",api_secret="28ba0fc7c529f17ae61f9b6cd83985ec200a4db2")

data.get_yahoo_weather_by_city("vinh", Unit.celsius)
# data.get_yahoo_weather_by_location(35.67194, 51.424438)
#location
print(data.location.city)
print(data.location.region)
print(data.location.country)
print(data.location.lat)
print(data.location.long)
print(data.location.timezone_id)
print("------------------------")
print(data.wind.chill)
print(data.wind.direction)
print(data.wind.speed)
print("------------------------")
print(data.atmosphere.humidity)
print(data.atmosphere.visibility)
print(data.atmosphere.pressure)
print("------------------------")
print(data.astronomy.sunrise)
print(data.astronomy.sunset)
print("------------------------")
print(data.condition.text)
print(data.condition.code)
print(data.condition.temperature)
print("------------------------")
print(data.current_observation.pubDate)

for forecasts in data.forecasts:
    print(forecasts.date)
    print(forecasts.text)
    print(forecasts.high)
    print(forecasts.low)
    print(forecasts.code)
    
    print("-----------")