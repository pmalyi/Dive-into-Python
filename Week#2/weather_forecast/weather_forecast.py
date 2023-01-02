class CityInfo:

    def __init__(self, city):
        self.city = city

    def weather_forecast(self):
        pass



def _main(city):
    city_info = CityInfo(city)
    forecast = city_info.weather_rorecast()
    print(forecast)


if __name__ == "__main__":
    city = input()
    _main(city)