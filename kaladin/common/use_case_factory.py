from kaladin.common.dao_factory import DaoFactory
from kaladin.use_cases.customer_use_case import CustomerUseCase
from kaladin.use_cases.order_use_case import OrderUseCase
from kaladin.use_cases.product_configuration_use_case import ProductConfigurationUseCase


class UseCaseFactory:

    def __init__(self,
                 dao_factory: DaoFactory):
        self._dao_factory = dao_factory

    @property
    def customer_use_case(self) -> CustomerUseCase:
        return CustomerUseCase(
            customer_read_dao=self._dao_factory.customer_read_dao,
            customer_write_dao=self._dao_factory.customer_write_dao,
        )

    @property
    def product_configuration_use_case(self) -> ProductConfigurationUseCase:
        return ProductConfigurationUseCase(
            product_read_dao=self._dao_factory.product_read_dao,
            product_write_dao=self._dao_factory.product_write_dao,
            side_dish_read_dao=self._dao_factory.side_dish_read_dao,
            side_dish_write_dao=self._dao_factory.side_dish_write_dao,
        )

    @property
    def order_use_case(self) -> OrderUseCase:
        return OrderUseCase(
            customer_read_dao=self._dao_factory.customer_read_dao,
            order_read_dao=self._dao_factory.order_read_dao,
            order_write_dao=self._dao_factory.order_write_dao,
            product_read_dao=self._dao_factory.product_read_dao,
        )
