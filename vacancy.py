from hh_api import HhApi
from superjob_api import SuperJobApi
from pprint import pprint


class Vacancy(HhApi, SuperJobApi):
    def __init__(self):
        super().__init__()


 def get_vacancy(self):
        vacancy = []
        for el in self.get_api['items']:
            title = el['name']
            id_v = el['id']
            salary = el['salary']
            requirement = el['snippet']['requirement']
            job = {"title": title,
                   "id": id_v,
                   "salary": salary,
                   "requirement": requirement}
        vacancy.append(job)
        return vacancy

v = Vacancy()
pprint(v.name)
