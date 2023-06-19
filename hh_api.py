import requests
from get_api import GetApi
from pprint import pprint


class HhApi(GetApi):
    """ Класс для подключения к API hh.ru"""
    def __init__(self):
        self.api_url = "https://api.hh.ru/vacancies/"

    def get_api(self):
        """Метод для получения вакансий """
        return requests.get(self.api_url).json()


hh = HhApi()
pprint(hh.get_api())
