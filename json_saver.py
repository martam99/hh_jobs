import json
from hh_api import HhApi
from superjob_api import SuperJobApi


class JSONSaver(HhApi, SuperJobApi):
    """Класс, который сохраняет все вакансии в json файл."""
    def save_as_json(self):
        api_h = HhApi()
        api_s = SuperJobApi()
        api = [api_h.get_api(), api_s.get_api()]

        with open("jobs.json", "w", encoding="utf-8") as f:
            json.dump(api, f, sort_keys=False, indent=2, ensure_ascii=False)

