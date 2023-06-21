from vacancy import Vacancy
import json

if __name__ == "__main__":

    with open("jobs.json", "r", encoding='utf-8') as file:
        vacancies = json.load(file)
        try:
            for el in vacancies[0]['items']:
                title = el['name']
                salary_min = el['salary']['from']
                salary_max = el['salary']['to']
                url = el['area']['url']
                requirement = el['snippet']['requirement']
            for el in vacancies[1]['objects']:
                title = el['profession']
                salary_min = el["payment_from"]
                salary_max = el["payment_to"]
                url = el["client"]["link"]
                requirement = el["candidat"]
        except KeyError:
            print("no key")

    list_job = []
    v = Vacancy(title, salary_min, salary_max, url, requirement)
    list_job.append(v)


    def user_interaction():
        platforms = ["HeadHunter", "SuperJob"]
        user_input = input("Введите поисковый запрос: ")
        if user_input == v.title:
            return v
        else:
            return f"Нет вакансий, соответствующих заданным критериям."


    user_interaction()
