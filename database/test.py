from datetime import date as date_type

from datetime import timedelta

print(str(date_type.today()))

yesterday = date_type.today() - timedelta(days=1)

print(str(yesterday))
