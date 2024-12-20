from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel
from uuid import UUID


class OrderStatus(Enum):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class OrderItemRequest(BaseModel):
    product_id: UUID
    quantity: int
    total_price: Decimal | None = None
    side_dish: list[UUID] | None = None


class OrderRequest(BaseModel):
    user_id: UUID
    customer_id: UUID
    delivery_date: str
    delivery_address: str | None = None
    is_paid: bool | None = None
    total_price: float | None = None
    order_item: list[OrderItemRequest]


class OrderItem(BaseModel):
    order_item_id: UUID
    order_id: UUID
    product_id: UUID
    quantity: int
    total_price: Decimal


class Order(BaseModel):
    order_id: UUID
    user_id: UUID
    customer_id: UUID
    delivery_date: datetime
    delivery_address: str
    is_paid: bool
    total_price: float
    status: OrderStatus


class SideDishDetail(BaseModel):
    side_dish_id: UUID
    side_dish_name: str


class OrderItemDetail(BaseModel):
    order_item_id: UUID
    product_id: UUID
    product_name: str
    quantity: int
    total_price: Decimal
    side_dish: list[SideDishDetail] | None = None


class OrderDetail(BaseModel):
    order_id: UUID
    user_id: UUID
    user_name: str
    customer_id: UUID
    customer_name: str
    delivery_date: datetime
    delivery_address: str
    is_paid: bool
    total_price: float
    status: OrderStatus
    order_item: list[OrderItemDetail] | None = None
