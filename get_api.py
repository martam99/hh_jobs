from abc import ABC, abstractmethod


class GetApi(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def get_api(self):
        print("Get api")
