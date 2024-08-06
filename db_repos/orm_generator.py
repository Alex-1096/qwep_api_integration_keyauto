from sqlalchemy import MetaData, Table
from sqlalchemy.orm import declarative_base

from base_config import DATABASE_URL, DB_SCHEMA
from database.db_connector import DBConnector


class ORMGenerator:
    """
    Класс генерации ORM-объектов таблиц
    """
    db = DBConnector(DATABASE_URL)
    metadata = MetaData()
    Base = declarative_base()

    def __init__(self, table_name):
        """
        :param table_name: название таблицы, объект которой требуется получить
        """
        self.table_name = table_name

    def get_table(self):
        """
        :return: объект таблицы как класс
        """
        res = Table(self.table_name, self.metadata, autoload_with=self.db.engine, schema=DB_SCHEMA)
        self.db.close()
        return res

    def get_table_class(self):
        """
        :return: ORM-модель таблицы
        """
        class_dict = {'__table__': self.get_table()}
        return type(self.table_name, (self.Base,), class_dict)

