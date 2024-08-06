import os
from os import getenv
from typing import Final
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Использование переменных окружения
DB_DIALECT = str(getenv('DB_DIALECT'))
DB_DRIVER = str(getenv('DB_DRIVER'))
DB_LOGIN = str(getenv('DB_LOGIN'))
DB_PASSWORD = str(getenv('DB_PASSWORD'))
DB_SERVER = str(getenv('DB_SERVER'))
DB_NAME = str(getenv('DB_NAME'))
DB_ODBC_CONNECT_DRIVER = str(getenv('DB_ODBC_CONNECT_DRIVER'))
DB_SCHEMA = str(getenv('DB_SCHEMA'))
DATABASE_URL = f'{DB_DIALECT}+{DB_DRIVER}://{DB_LOGIN}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver={DB_ODBC_CONNECT_DRIVER}'

TOKEN = f'Bearer {str(os.getenv('TOKEN'))}'
ROOT_API_URL = r'https://dataapi.kube.qwep.ru/'

# url для апи
URL_PRICES_FOR_DATE = r'v2/report/avg-price/date/buys-requests'
