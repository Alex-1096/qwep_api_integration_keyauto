from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session


class DBConnector:
    def __init__(self, db_url: str | None) -> None:
        self.engine = create_engine(db_url)
        self.session = self.create_connect_db()

    def create_connect_db(self) -> Session:
        """
        Функция создания коннекта к БД
        """
        session = sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)
        return session()

    def get_session(self) -> Session:
        return self.session

    def close(self) -> None:
        """
        Функция для закрытия соедиенения
        """
        self.session.close()

    def flush(self) -> None:
        """
        Функция для отправки изменений на БД
        """
        self.session.flush()

    def commit(self) -> None:
        """
        Функция для фиксации изменений на БД
        """
        self.session.commit()

    def rollback(self) -> None:
        """
        Функция для отмены изменений на БД
        """
        self.session.rollback()
