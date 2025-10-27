from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

class DBConnection:
    def __init__(self):
        string_conexao = config["ATLAS_URI"]
        nome_db = config["DB_NAME"]
        self.client = MongoClient(string_conexao)
        self.db = self.client[nome_db]

    def getCollection(self, name):
        return self.db[name]