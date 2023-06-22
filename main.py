from vacancy import Vacancy
import json


def user_interaction():
    try:
        with open("jobs.json", "r", encoding='utf-8') as file:
            vacancies = json.load(file)
            list_job = []
            # Достали значения из файла json
            for el in vacancies[0]['items']:
                title_hh = el['name']
                salary_min_hh = el['salary']['from']
                salary_max_hh = el['salary']['to']
                url_hh = el['area']['url']
                requirement_hh = el['snippet']['requirement']
                # Создали экземпляр класса Vacancy со значениями из платформы hh.ru
                v_hh = Vacancy(title_hh, salary_min_hh, salary_max_hh, url_hh, requirement_hh)
                # Добавили экземпляры в список list_job
                list_job.append(v_hh)
            # Достали значения из файла json
            for el in vacancies[1]['objects']:
                title_sj = el['profession']
                salary_min_sj = el["payment_from"]
                salary_max_sj = el["payment_to"]
                url_sj = el["client"]["link"]
                requirement_sj = el["candidat"]
                # Создали экземпляр класса Vacancy со значениями из платформы superjob.ru
                v_sj = Vacancy(title_sj, salary_min_sj, salary_max_sj, url_sj, requirement_sj)
                # Добавили экземпляры в список list_job
                list_job.append(v_sj)
    except FileNotFoundError:
        print("File not found")
    except KeyError:
        print("No key")

    for hh in list_job:
        user_input = input("Введите поисковый запрос: ")
        if user_input == hh.title:
            print(hh)
        else:
            print(f"Нет вакансий, соответствующих заданным критериям.")

        input_max_salary = int(input("Максимальная сумма зарплаты до։ "))
        if input_max_salary <= v_hh.salary_max or v_sj.salary_max:
            print(hh)
        elif input_max_salary > v_hh.salary_max or v_sj.salary_max:
            print(f"Нет вакансий, соответствующих заданным критериям.")


if __name__ == "__main__":
    user_interaction()
