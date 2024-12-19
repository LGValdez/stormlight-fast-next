from uuid import UUID, uuid4

from kaladin.data_access.customer_dao import CustomerReadDAO, CustomerWriteDAO
from kaladin.data_classes.customer import Customer, CustomerRequest


class CustomerUseCase:

    def __init__(self,
                 customer_read_dao: CustomerReadDAO,
                 customer_write_dao: CustomerWriteDAO):
        self._customer_read_dao = customer_read_dao
        self._customer_write_dao = customer_write_dao

    def get_all_customers(self) -> list[Customer]:
        return self._customer_read_dao.fetch_all_customers()

    def get_customer(self, customer_id: UUID) -> Customer:
        return self._customer_read_dao.fetch_customer_by_id(customer_id)

    def create_customer(self, customer_request: CustomerRequest) -> bool:
        customer = Customer(
            customer_id=uuid4(),
            name=customer_request.name,
            address=customer_request.address,
            note=customer_request.note,
        )
        return self._customer_write_dao.insert_customer(customer)
