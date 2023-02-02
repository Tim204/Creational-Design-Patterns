from abc import ABC, abstractmethod


class ConfigManager(ABC):
    @abstractmethod
    def __init__(self):
        self._setting = {}
        self.config = ConfigManager()

    def set(self, key, value):
        self._setting[key] = value

    def get(self, key):
        return self._setting.get(key)

    def get_instance(self):
        return self.config


def client():
    manage = ConfigManager.get_instance()
    manage.set("name", "timas")
    print(manage.get("name"))


client()



