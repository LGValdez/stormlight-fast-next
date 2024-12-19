from decimal import Decimal
from pydantic import BaseModel
from uuid import UUID


class SideDishRequest(BaseModel):
    name: str
    extra_price: Decimal = Decimal('0')
    description: str | None = None
    product_id: UUID | None = None


class SideDish(BaseModel):
    side_dish_id: UUID
    name: str
    extra_price: Decimal = Decimal('0')
    description: str | None = None
    product_id: UUID | None = None
