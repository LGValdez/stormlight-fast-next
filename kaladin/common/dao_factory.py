from typing import Any

from kaladin.common.database import DatabaseConnection
from kaladin.data_access.customer_dao import CustomerReadDAO, CustomerWriteDAO
from kaladin.data_access.order_dao import OrderReadDAO, OrderWriteDAO
from kaladin.data_access.product_dao import ProductReadDAO, ProductWriteDAO
from kaladin.data_access.side_dish_dao import SideDishReadDAO, SideDishWriteDAO


class DaoFactory:

    def __init__(self,
                 db_connection: DatabaseConnection,
                 secrets: Any):
        self._db_connection = db_connection
        self._secrets = secrets

    @property
    def customer_read_dao(self) -> CustomerReadDAO:
        return CustomerReadDAO(self._db_connection, self._secrets)

    @property
    def customer_write_dao(self) -> CustomerWriteDAO:
        return CustomerWriteDAO(self._db_connection, self._secrets)

    @property
    def product_read_dao(self) -> ProductReadDAO:
        return ProductReadDAO(self._db_connection, self._secrets)

    @property
    def product_write_dao(self) -> ProductWriteDAO:
        return ProductWriteDAO(self._db_connection, self._secrets)

    @property
    def side_dish_read_dao(self) -> SideDishReadDAO:
        return SideDishReadDAO(self._db_connection, self._secrets)

    @property
    def side_dish_write_dao(self) -> SideDishWriteDAO:
        return SideDishWriteDAO(self._db_connection, self._secrets)

    @property
    def order_read_dao(self) -> OrderReadDAO:
        return OrderReadDAO(self._db_connection, self._secrets)

    @property
    def order_write_dao(self) -> OrderWriteDAO:
        return OrderWriteDAO(self._db_connection, self._secrets)
