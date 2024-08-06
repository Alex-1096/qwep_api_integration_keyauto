from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker
from base_config import DATABASE_URL

# Создаем объект engine для подключения к базе данных
engine = create_engine(DATABASE_URL)  # замените на ваш URL

# Определяем объект MetaData
metadata = MetaData()

# Отражаем существующую таблицу в объект Table
existing_table = Table('TipyDiagnostikiASP', metadata, autoload_with=engine)

# Создаем базовый класс для ORM
Base = declarative_base()

# Определяем класс, используя рефлексию
class ExistingTable(Base):
    __table__ = existing_table

session = sessionmaker(bind=engine)()

# Выполняем запрос SELECT
result = session.query(ExistingTable).all()

# Выводим результаты
for row in result:
    print(row.__dict__)

print(existing_table)