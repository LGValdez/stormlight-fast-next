from uuid import UUID

from kaladin.data_access.base_dao import BaseDAO
from kaladin.data_classes.order import Order, OrderItem, OrderDetail, OrderItemDetail, SideDishDetail


class OrderWriteDAO(BaseDAO):

    def insert_order(self, order: Order):
        sql = """INSERT INTO sale_order (order_id, user_id, customer_id, delivery_date, 
                                    delivery_address, is_paid, total_price, status) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        self._db_connection.insert_record(sql, [
            str(order.order_id),
            str(order.user_id),
            str(order.customer_id),
            order.delivery_date,
            order.delivery_address,
            order.is_paid,
            order.total_price,
            order.status.value
        ])

    def insert_order_item(self, order_item: OrderItem):
        sql = """INSERT INTO order_item (order_item_id, order_id, product_id, quantity, total_price) 
                 VALUES (%s, %s, %s, %s, %s)"""
        self._db_connection.insert_record(sql, [
            str(order_item.order_item_id),
            str(order_item.order_id),
            str(order_item.product_id),
            order_item.quantity,
            order_item.total_price
        ])

    def insert_order_item_side_dish(self, order_item_id: UUID, side_dish_id: UUID):
        sql = "INSERT INTO order_item_side_dish (order_item_id, side_dish_id) VALUES (%s, %s)"
        self._db_connection.insert_record(sql, [
            str(order_item_id),
            str(side_dish_id)
        ])


class OrderReadDAO(BaseDAO):

    _PRODUCT = ', '.join(f for f in Order.__fields__)

    def fetch_order_detail_by_order_id(self, order_id: UUID) -> OrderDetail:
        sql = """
            SELECT
                so.order_id, so.user_id, u.name AS "user_name", so.customer_id, c.name AS "customer_name", 
                so.delivery_date, so.delivery_address, so.is_paid, so.total_price, so.status
            FROM sale_order so
            INNER JOIN customer u ON u.customer_id = so.user_id
            INNER JOIN customer c ON c.customer_id = so.customer_id
            WHERE order_id = %s;
        """
        r = self._db_connection.fetch_one(sql, [str(order_id)])
        return OrderDetail(**r)

    def fetch_order_item_detail_by_order_id(self, order_id: UUID) -> list[OrderItemDetail]:
        sql = """
            SELECT
                oi.order_item_id, oi.product_id, p.name AS "product_name", oi.quantity, oi.total_price
            FROM order_item oi
            INNER JOIN product p ON p.product_id = oi.product_id
            WHERE oi.order_id = %s;
        """
        r = self._db_connection.fetch_all(sql, [str(order_id)])
        return [OrderItemDetail(**i) for i in r]

    def fetch_order_item_side_dish_detail_by_order_item_id(self, order_item_id: UUID) -> list[SideDishDetail]:
        sql = """
            SELECT
                os.side_dish_id,
                sd.name AS "side_dish_name"
            FROM order_item_side_dish os
            INNER JOIN side_dish sd ON sd.side_dish_id = os.side_dish_id
            WHERE os.order_item_id = %s
        """
        r = self._db_connection.fetch_all(sql, [str(order_item_id)])
        return [SideDishDetail(**i) for i in r]
