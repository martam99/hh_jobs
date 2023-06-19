import requests
from get_api import GetApi
from pprint import pprint


class SuperJobApi(GetApi):
    """ Класс для подключения к API superjob.ru"""
    def __init__(self):
        self.api_url = "https://api.superjob.ru/2.0/vacancies/"
        self.headers = {"Host": "api.superjob.ru",
                        "X-Api-App-Id": "v3.r.137614145.cb26bfdfa58f9da553a2e2914a14330a40f30d5e.c39d10f2ffd5e1eae7f5da48af569f7b7a09b985",
                        "Authorization": "Bearer r.000000010000001.example.access_token",
                        "Content-Type": "application/x-www-form-urlencoded"}
        self.params = {}

    def get_api(self):
        """Метод для получения вакансий """
        return requests.get(self.api_url, headers=self.headers).json()


s = SuperJobApi()
pprint(s.get_api())
