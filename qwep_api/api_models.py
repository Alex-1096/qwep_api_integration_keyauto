from __future__ import annotations

from datetime import date as date_type, timedelta

from typing import List, Optional, TypedDict

from pydantic import BaseModel, Field

# Модели отправляемых и получаемых данных

### post_data
class Parameters(BaseModel):
    date: str = str(date_type.today() - timedelta(days=1))
    currency: str = 'RUB'
    status: str = 'All'


class Item(BaseModel):
    brand: str
    article: str
    group: Optional[int]

class PostNomenclature(BaseModel):
    parameters: Parameters
    items: List[Item]

class DictNomenclature(TypedDict):
    brand: str
    article: str
    group: Optional[int]


def gen_post_json_nomenclature(items: List[DictNomenclature], parameters=Parameters()):
    return PostNomenclature(parameters=parameters, items=[Item(**item_dict) for item_dict in items])


### get_data
class ModelItem(BaseModel):
    article: str
    brand: str
    currency: str
    group: int = Field(validation_alias='group', serialization_alias='id_nom')
    avgprice: Optional[float] = None
    cnt: Optional[int] = None
    maxprice: Optional[float] = None
    minprice: Optional[float] = None
    status: Optional[str] = None
    vendor: Optional[str] = None


class PriceModel(BaseModel):
    rows: List[ModelItem]

