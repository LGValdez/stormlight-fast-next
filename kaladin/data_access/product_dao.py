from uuid import UUID

from kaladin.data_access.base_dao import BaseDAO
from kaladin.data_classes.product import Product


class ProductWriteDAO(BaseDAO):

    def insert_product(self, product: Product):
        sql = "INSERT INTO product (product_id, name, price, description) VALUES (%s, %s, %s, %s)"
        self._db_connection.insert_record(sql, [
            str(product.product_id),
            product.name,
            product.price,
            product.description
        ])


class ProductReadDAO(BaseDAO):

    _PRODUCT = ', '.join(f for f in Product.__fields__)

    def fetch_product_by_id(self, product_id: UUID) -> Product:
        sql = f"SELECT {self._PRODUCT} FROM product WHERE product_id = %s"
        r = self._db_connection.fetch_one(sql, [str(product_id)])
        return Product(**r)

    def fetch_all_products(self) -> list[Product]:
        sql = f"SELECT {self._PRODUCT} FROM product"
        r = self._db_connection.fetch_all(sql)
        return [Product(**product) for product in r]
