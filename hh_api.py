import requests
from get_api import GetApi
from pprint import pprint


class HhApi(GetApi):
    """ Класс для подключения к API hh.ru"""
    def __init__(self):
        self.api_url = "https://api.hh.ru/vacancies/"

    def get_api(self):
        """Метод для получения вакансий """
        response = requests.get(self.api_url)
        if response.status_code != 200:
            return f"Ошибка подключения к api с кодом {response.status_code}"
        return response.json()['items']


hh = HhApi()
pprint(hh.get_api())
