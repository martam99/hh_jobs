from hh_api import HhApi
from superjob_api import SuperJobApi
from json_saver import JSONSaver
from vacancy import Vacancy


def main():
    hh = HhApi()
    sj = SuperJobApi()
    j = JSONSaver("data.json")
    platforms = ["Head Hunter", "Super Job"]
    user_platform = input(f"Выберите платформу для поиска вакансий ]\n1){platforms[0]}\n2){platforms[1]}")
    user_input = input("Введите название вакансии:")
    try:
        if user_platform == "1":
            for el in hh.get_api():
                vac_hh = Vacancy(el['name'], el['salary']['from'], el['salary']['to'], el['area']['url'],
                                 el['snippet']['requirement'])
                if user_input == vac_hh.title:
                    j.save_vacancies([vac_hh])
                    print(j.load_vacancies())
            else:
                print("Нет вакансий, соответствующих заданным критериям.")
        elif user_platform == "2":
            for el in sj.get_api():
                vac_sj = Vacancy(el['profession'], el["payment_from"], el["payment_to"], el["client"]["link"],
                                 el["candidat"])
                if user_input == vac_sj.title:
                    j.save_vacancies([vac_sj])
                    print(j.load_vacancies())
            else:
                print("Нет вакансий, соответствующих заданным критериям.")
        elif user_platform != "1" or "2":
            print("Такой платформы не существует")

    except TypeError:
        print(" ")
    except KeyError:
        print(" ")


if __name__ == "__main__":
    main()
