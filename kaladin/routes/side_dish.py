from fastapi import APIRouter, Depends

from kaladin.common.container import build_use_case_factory
from kaladin.common.use_case_factory import UseCaseFactory
from kaladin.data_classes.side_dish import SideDishRequest, SideDish

router = APIRouter(
    prefix="/api/side_dish",
    tags=["products"],
)


@router.get("", response_model=list[SideDish])
async def get_all_side_dishes(
    use_cases: UseCaseFactory = Depends(build_use_case_factory)
):
    return use_cases.product_configuration_use_case.get_all_side_dishes()


@router.post("")
async def create_side_dish(
    side_dish_request: SideDishRequest,
    use_cases: UseCaseFactory = Depends(build_use_case_factory)
):
    use_cases.product_configuration_use_case.create_side_dish(side_dish_request)
    return {"success": True}
