from uuid import UUID

from kaladin.data_access.base_dao import BaseDAO
from kaladin.data_classes.side_dish import SideDish


class SideDishWriteDAO(BaseDAO):

    def insert_side_dish(self, side_dish: SideDish):
        sql = """INSERT INTO side_dish (side_dish_id, name, extra_price, description, product_id) 
                 VALUES (%s, %s, %s, %s, %s)"""
        self._db_connection.insert_record(sql, [
            str(side_dish.side_dish_id),
            side_dish.name,
            side_dish.extra_price,
            side_dish.description,
            str(side_dish.product_id) if side_dish.product_id else None,
        ])


class SideDishReadDAO(BaseDAO):

    _SIDE_DISH = ', '.join(f for f in SideDish.__fields__)

    def fetch_side_dish_for_product(self, product_id: UUID) -> list[SideDish]:
        sql = f"""SELECT {self._SIDE_DISH} 
                  FROM side_dish 
                  WHERE product_id = %s OR product_id IS NULL"""
        r = self._db_connection.fetch_all(sql, [str(product_id)])
        return [SideDish(**side_dish) for side_dish in r]

    def fetch_side_dish_by_id(self, side_dish_id: UUID) -> SideDish:
        sql = f"SELECT {self._SIDE_DISH} FROM side_dish WHERE side_dish_id = %s"
        r = self._db_connection.fetch_one(sql, [str(side_dish_id)])
        return SideDish(**r)

    def fetch_all_side_dishes(self) -> list[SideDish]:
        sql = f"SELECT {self._SIDE_DISH} FROM side_dish"
        r = self._db_connection.fetch_all(sql)
        return [SideDish(**side_dish) for side_dish in r]
