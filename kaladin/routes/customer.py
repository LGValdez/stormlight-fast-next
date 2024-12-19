from uuid import UUID

from fastapi import APIRouter, Depends

from kaladin.common.container import build_use_case_factory
from kaladin.common.use_case_factory import UseCaseFactory
from kaladin.data_classes.customer import Customer, CustomerRequest

router = APIRouter(
    prefix="/api/customer",
    tags=["customers"],
)


@router.get("", response_model=list[Customer])
async def get_all_customers(
    use_cases: UseCaseFactory = Depends(build_use_case_factory)
):
    return use_cases.customer_use_case.get_all_customers()


@router.get("/{customer_id}", response_model=Customer)
async def get_customer(
    customer_id: str,
    use_cases: UseCaseFactory = Depends(build_use_case_factory)
):
    return use_cases.customer_use_case.get_customer(UUID(customer_id))


@router.post("")
async def create_customer(
    customer_request: CustomerRequest,
    use_cases: UseCaseFactory = Depends(build_use_case_factory)
):
    use_cases.customer_use_case.create_customer(customer_request)
    return {"success": True}
