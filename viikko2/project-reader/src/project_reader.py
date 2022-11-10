from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        with open("pyproject.toml", "rb") as f:
            content = tomli.load(f)

        name = content['tool']['poetry']['name']
        description = content['tool']['poetry']['description']
        dependencies = content['tool']['poetry']['dependencies']
        dev_dependencies = content['tool']['poetry']['dev-dependencies']

        # # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
