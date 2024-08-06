from math import ceil

from database.db_connector import DBConnector
from base_config import DATABASE_URL, URL_PRICES_FOR_DATE
from db_repos.db_models import Model, PricesORM
from db_repos.orm_generator import ORMGenerator
from qwep_api.api_models import gen_post_json_nomenclature, PriceModel
from qwep_api.qwep_api_connect import QwApi

db = DBConnector(DATABASE_URL)


class QWEPRepository:
    db = db
    _limit: int = 100000

    @classmethod
    def create_tables(cls):
        """
        Создание таблиц в БД, если не существует
        """
        with cls.db.engine.begin() as conn:
            Model.metadata.create_all(bind=conn)

    @classmethod
    def drop_tables(cls):
        """
        Удаление таблиц БД, если существуют
        """
        with cls.db.engine.begin() as conn:
            Model.metadata.drop_all(bind=conn)

    @classmethod
    def get_table(cls, table: str):
        """
        Генерация ORM-объекта таблицы по названию
        :param table: имя таблицы
        :return: класс таблицы
        """
        return ORMGenerator(table).get_table_class()

    @classmethod
    def get_nomnklature(cls):
        """
        Получение списка номенклатуры из таблицы БД
        """
        Nomenclature = cls.get_table('Qwep_post_nom')
        res = cls.db.session.query(Nomenclature).all()
        return res

    @classmethod
    def get_prices(cls, post_date: str = None):
        """
        :param post_date: дата действия цен (например, '2024-05-25'). Если не задана, то берётся вчерашняя
        :return: tuple(list[dict], date) полученные цены и дата
        """
        items = [{'brand': row.brand, 'article': row.article, 'group': row.id_nom} for row in cls.get_nomnklature()]
        num_pack = ceil(len(items) / cls._limit)
        res = []
        date_upd = None
        for s in range(num_pack):
            post_data = gen_post_json_nomenclature(items[s*cls._limit:(s + 1) * cls._limit])
            if post_date:
                post_data.parameters.date = post_date
            date_upd = post_data.parameters.date
            prices = QwApi().post_query(URL_PRICES_FOR_DATE, post_data.dict())  # import resp from test_responce
            res.extend(prices)
        print("Получен ответ")
        return res, date_upd

    @classmethod
    def merge_prices(cls):
        """
        Запись полученных данных в таблицу БД
        """
        resp_qwep, date_upd = cls.get_prices()
        resp_model = PriceModel(rows=resp_qwep)
        with cls.db.session as session:
            session.query(PricesORM).filter(PricesORM.date_actual == date_upd).delete()
            for row in resp_model.rows:
                db_obj = PricesORM(**row.model_dump(by_alias=True), date_actual=date_upd)
                session.merge(db_obj)
            else:
                session.commit()


