from uuid import UUID, uuid4

from kaladin.data_access.product_dao import ProductReadDAO, ProductWriteDAO
from kaladin.data_access.side_dish_dao import SideDishWriteDAO, SideDishReadDAO
from kaladin.data_classes.product import Product, ProductRequest, ProductWithSideDishes
from kaladin.data_classes.side_dish import SideDishRequest, SideDish


class ProductConfigurationUseCase:

    def __init__(self,
                 product_read_dao: ProductReadDAO,
                 product_write_dao: ProductWriteDAO,
                 side_dish_read_dao: SideDishReadDAO,
                 side_dish_write_dao: SideDishWriteDAO,
                 ):
        self._product_read_dao = product_read_dao
        self._product_write_dao = product_write_dao
        self._side_dish_write_dao = side_dish_write_dao
        self._side_dish_read_dao = side_dish_read_dao

    def get_all_side_dishes(self) -> list[SideDish]:
        return self._side_dish_read_dao.fetch_all_side_dishes()

    def create_side_dish(self, side_dish_request: SideDishRequest):
        side_dish = SideDish(
            side_dish_id=uuid4(),
            name=side_dish_request.name,
            extra_price=side_dish_request.extra_price,
            description=side_dish_request.description,
            product_id=side_dish_request.product_id,
        )
        self._side_dish_write_dao.insert_side_dish(side_dish)

    def get_all_products(self) -> list[Product]:
        return self._product_read_dao.fetch_all_products()

    def get_product(self, product_id: UUID) -> Product:
        return self._product_read_dao.fetch_product_by_id(product_id)

    def create_product(self, product_request: ProductRequest):
        product = Product(
            product_id=uuid4(),
            name=product_request.name,
            price=product_request.price,
            description=product_request.description,
        )
        self._product_write_dao.insert_product(product)

        if product_request.side_dish:
            self._create_side_dishes_for_product(product_request.side_dish, product.product_id)

    def _create_side_dishes_for_product(self, side_dishes: list[SideDishRequest], product_id: UUID):
        for side_dish_request in side_dishes:
            side_dish = SideDish(
                side_dish_id=uuid4(),
                product_id=product_id,
                name=side_dish_request.name,
                extra_price=side_dish_request.extra_price,
                description=side_dish_request.description,
            )
            self._side_dish_write_dao.insert_side_dish(side_dish)

    def get_product_with_side_dishes(self, product_id: UUID) -> ProductWithSideDishes:
        product = self._product_read_dao.fetch_product_by_id(product_id)
        side_dishes = self._side_dish_read_dao.fetch_side_dish_for_product(product_id)
        return ProductWithSideDishes(
            product_id=product_id,
            name=product.name,
            price=product.price,
            description=product.description,
            side_dish=side_dishes
        )
