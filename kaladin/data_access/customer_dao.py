from uuid import uuid4, UUID

from kaladin.data_access.base_dao import BaseDAO
from kaladin.data_classes.customer import Customer


class CustomerWriteDAO(BaseDAO):

    def insert_customer(self, customer: Customer):
        sql = "INSERT INTO customer (customer_id, name, address, note) VALUES (%s, %s, %s, %s)"
        self._db_connection.insert_record(sql, [
            str(customer.customer_id),
            customer.name,
            customer.address,
            customer.note
        ])


class CustomerReadDAO(BaseDAO):

    _CUSTOMER = ', '.join(f for f in Customer.__fields__)

    def fetch_customer_by_id(self, customer_id: UUID) -> Customer:
        sql = f"SELECT {self._CUSTOMER} FROM customer WHERE customer_id = %s"
        r = self._db_connection.fetch_one(sql, [str(customer_id)])
        return Customer(**r)

    def fetch_all_customers(self) -> list[Customer]:
        sql = f"SELECT {self._CUSTOMER} FROM customer c"
        r = self._db_connection.fetch_all(sql)
        return [Customer(**customer) for customer in r]
