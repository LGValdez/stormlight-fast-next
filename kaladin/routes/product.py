from uuid import UUID

from fastapi import APIRouter, Depends

from kaladin.common.container import build_use_case_factory
from kaladin.common.use_case_factory import UseCaseFactory
from kaladin.data_classes.product import Product, ProductRequest, ProductWithSideDishes

router = APIRouter(
    prefix="/api/product",
    tags=["products"],
)


@router.get("", response_model=list[Product])
async def get_all_products(
    use_cases: UseCaseFactory = Depends(build_use_case_factory)
):
    return use_cases.product_configuration_use_case.get_all_products()


@router.get("/{product_id}", response_model=ProductWithSideDishes)
async def get_product_with_side_dishes(
    product_id: str,
    use_cases: UseCaseFactory = Depends(build_use_case_factory)
):
    return use_cases.product_configuration_use_case.get_product_with_side_dishes(UUID(product_id))


@router.post("")
async def create_product(
    product_request: ProductRequest,
    use_cases: UseCaseFactory = Depends(build_use_case_factory)
):
    use_cases.product_configuration_use_case.create_product(product_request)
    return {"success": True}
