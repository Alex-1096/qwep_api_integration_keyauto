from database.repository import QWEPRepository

if __name__ == '__main__':
    QWEPRepository().create_tables()
    QWEPRepository().merge_prices()

