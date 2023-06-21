import json
from json_saver import JSONSaver
from pprint import pprint


class Vacancy(JSONSaver):

    def __init__(self, title, url, salary_min, salary_max, requirement):
        super().__init__()
        self.title = title
        self.url = url
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.requirement = requirement
