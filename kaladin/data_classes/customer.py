from pydantic import BaseModel
from uuid import UUID


class CustomerRequest(BaseModel):
    name: str
    address: str | None = None
    note: str | None = None


class Customer(BaseModel):
    customer_id: UUID
    name: str
    address: str | None = None
    note: str | None = None
