from decimal import Decimal
from pydantic import BaseModel
from uuid import UUID

from kaladin.data_classes.side_dish import SideDish, SideDishRequest


class ProductRequest(BaseModel):
    name: str
    price: Decimal
    description: str | None = None
    side_dish: list[SideDishRequest] | None = None


class Product(BaseModel):
    product_id: UUID
    name: str
    price: Decimal
    description: str | None = None


class ProductWithSideDishes(Product):
    side_dish: list[SideDish]
