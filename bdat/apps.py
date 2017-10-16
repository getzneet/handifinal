from django.apps import AppConfig
from watson import search as watson


class BdatConfig(AppConfig):
    name = 'bdat'

    def ready(self):
        Technology = self.get_model("Technology")
        watson.register(Technology)
    

