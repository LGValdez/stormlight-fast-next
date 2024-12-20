from uuid import UUID

from fastapi import APIRouter, Depends

from kaladin.common.container import build_use_case_factory
from kaladin.common.use_case_factory import UseCaseFactory
from kaladin.data_classes.order import OrderDetail, OrderRequest

router = APIRouter(
    prefix="/api/order",
    tags=["orders"],
)


@router.get("/{order_id}", response_model=OrderDetail)
async def get_order_details(
    order_id: str,
    use_cases: UseCaseFactory = Depends(build_use_case_factory)
):
    return use_cases.order_use_case.get_order_details(UUID(order_id))


@router.post("")
async def create_order(
    order_request: OrderRequest,
    use_cases: UseCaseFactory = Depends(build_use_case_factory)
):
    new_order_id = use_cases.order_use_case.create_order(order_request)
    return {"success": new_order_id is not None, "order_id": new_order_id}
