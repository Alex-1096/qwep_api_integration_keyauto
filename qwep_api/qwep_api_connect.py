from urllib.parse import urljoin

import requests

from base_config import TOKEN, ROOT_API_URL


class QwApi:

    @classmethod
    def post_query(cls, relative_path, data):
        """
        Запрос данных через APT
        :param relative_path: адрес подключения
        :param data: отправляемые данные
        :return: json с выгруженными данными
        """
        abs_url = urljoin(ROOT_API_URL, relative_path)
        headers = {"Authorization": TOKEN, "Content-Type": "application/json"}
        response = requests.post(abs_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(response.json())
