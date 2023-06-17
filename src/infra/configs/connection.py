from pymongo import MongoClient
from ...infra.interfaces.db_connection_interface import DBConnectionInterface
from .mongo_db_configs import mongo_db_infos
from ..interfaces.db_connection_interface import DBConnectionInterface

# classe que gerencia todas as conexoes
class DBConnectionHandler(DBConnectionInterface):
    def __init__(self) -> None:
        self.__connection_string = 'mongodb://{}:{}@{}:{}/?authSource=admin'.format(
            mongo_db_infos["USERNAME"],
            mongo_db_infos["PASSWORD"],
            mongo_db_infos["HOST"],
            mongo_db_infos["PORT"],
        )
        self.__datababase_name = mongo_db_infos["DB_NAME"]
        self.__client = None
        self.__db_connection = None

    # Ao iniciar o objeto da minha classe ele ja vai criar essa conexão
    def connect_to_db(self):
        # fazer metedo para conectar o banco de dados
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__datababase_name]

    def get_db_connection(self):
        return self.__db_connection

    def get_db_client(self):
        return self.__client

    def get_collection(self, collection_name: str):
        # Aqui, self.__db_connection é uma conexão com o banco de dados
        return self.__db_connection[collection_name]