import requests
import sys
from pprint import pprint

# Для работы программы надо получить ключ для доступа к API в
# личном кабинете разработчика яндекс
# https://developer.tech.yandex.ru/,
# тестовой версий вполне хватит для целей тестирования и написания программы.
# Ключ необходимо сохранить в константе API_KEY_YANDEX_WEATHER, в реальной
# разработке хранить таким образом секретные данные не стоит

Api_Key_Tomorrow = 'N99O1lgeGj2nOyUib0wogqaVlNxly9ph'
FIELDS = ["temp_max", "temp_min"]


class YandexWeatherForecast:
    """
    класс для работы с API ЯндексПогоды, страница документации API -
    https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test.html/
    """

    URL = 'https://api.weather.yandex.ru/v1/forecast?'

    def __init__(self, key):
        self.key = key
        self.headers = {'X-Yandex-API-Key': key}

    def get_weather_week_forecasts(self, city, fields):
        """возвращает список с недельным прогнозом погоды для населенного пункта city,
        необходимые характеристики погоды передаются в списке fields"""

        data = requests.get(f'{self.URL}{city}', headers=self.headers).json()

        week_forecast = []

        for forecast in data['forecasts']:
            data = {'date': forecast["date"]}
            for field in fields:
                value = forecast["parts"]["day"].get(field, None)
                if value is not None:
                    data[field] = value
            week_forecast.append(data)

        return week_forecast


class CityInfo:

    def __init__(self, city, forecast_provider):
        self.city = city.lower()
        self._forecast_provider = forecast_provider

    def weather_forecast(self, fields):
        return self._forecast_provider.get_weather_week_forecasts(self.city, fields)


def _main():
    weather_api = YandexWeatherForecast(Api_Key_Tomorrow)
    city_name = sys.argv[1]
    city = CityInfo(city_name, weather_api)
    pprint(city.weather_forecast(FIELDS))


if __name__ == "__main__":
    _main()
