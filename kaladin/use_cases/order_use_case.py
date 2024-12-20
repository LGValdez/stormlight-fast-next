from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

from kaladin.data_access.customer_dao import CustomerReadDAO
from kaladin.data_access.order_dao import OrderReadDAO, OrderWriteDAO
from kaladin.data_access.product_dao import ProductReadDAO
from kaladin.data_classes.order import Order, OrderRequest, OrderItemRequest, OrderItem, OrderDetail, OrderStatus


class OrderUseCase:

    def __init__(self,
                 customer_read_dao: CustomerReadDAO,
                 order_read_dao: OrderReadDAO,
                 order_write_dao: OrderWriteDAO,
                 product_read_dao: ProductReadDAO):
        self._customer_read_dao = customer_read_dao
        self._order_read_dao = order_read_dao
        self._order_write_dao = order_write_dao
        self._product_read_dao = product_read_dao

    def create_order(self, order_request: OrderRequest) -> UUID | None:
        new_order_id = uuid4()
        delivery_address = self._get_delivery_address(order_request)
        total_price = self._get_order_total_price(order_request)
        delivery_date = datetime.strptime(order_request.delivery_date, "%Y-%m-%d %H:%M:%S")

        new_order = Order(
            order_id=new_order_id,
            user_id=order_request.user_id,
            customer_id=order_request.customer_id,
            delivery_date=delivery_date,
            delivery_address=delivery_address,
            is_paid=bool(order_request.is_paid),
            total_price=total_price,
            status=OrderStatus.PENDING,
        )
        self._order_write_dao.insert_order(new_order)

        for order_item_request in order_request.order_item:
            self.create_order_item(order_item_request, new_order_id)

        return new_order_id

    def _get_delivery_address(self, order_request: OrderRequest) -> str:
        if order_request.delivery_address:
            return order_request.delivery_address

        customer = self._customer_read_dao.fetch_customer_by_id(order_request.customer_id)
        return customer.address if customer.address else 'TBD'

    def _get_order_total_price(self, order_request: OrderRequest) -> Decimal:
        order_total_price = Decimal('0')
        for order_item in order_request.order_item:
            order_total_price += self._get_order_item_total_price(order_item)
        return order_total_price

    def _get_order_item_total_price(self, order_item_request: OrderItemRequest) -> Decimal:
        if order_item_request.total_price:
            return order_item_request.total_price

        product = self._product_read_dao.fetch_product_by_id(order_item_request.product_id)
        return product.price * order_item_request.quantity

    def create_order_item(self, order_item_request: OrderItemRequest, order_id: UUID) -> bool:
        order_item_id = uuid4()
        new_order_item = OrderItem(
            order_item_id=order_item_id,
            order_id=order_id,
            product_id=order_item_request.product_id,
            quantity=order_item_request.quantity,
            total_price=self._get_order_item_total_price(order_item_request),
        )
        self._order_write_dao.insert_order_item(new_order_item)

        if order_item_request.side_dish:
            for side_dish_uuid in order_item_request.side_dish:
                self._order_write_dao.insert_order_item_side_dish(order_item_id, side_dish_uuid)

        return True

    def get_order_details(self, order_id: UUID) -> OrderDetail:
        order_detail = self._order_read_dao.fetch_order_detail_by_order_id(order_id)
        all_order_items = self._order_read_dao.fetch_order_item_detail_by_order_id(order_id)
        for order_item in all_order_items:
            order_item.side_dish = self._order_read_dao.fetch_order_item_side_dish_detail_by_order_item_id(
                order_item.order_item_id)
        order_detail.order_item = all_order_items
        return order_detail
