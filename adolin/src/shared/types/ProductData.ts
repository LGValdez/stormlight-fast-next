type SideDishDataType = {
    side_dish_id: string,
    name: string,
    extra_price: number,
    description: string,
    product_id: number | null,
}


type ProductDataType = {
    product_id: string,
    name: string,
    price: number,
    min_side_dish: number,
    max_side_dish: number,
    description: string,
    side_dish: SideDishDataType[]
}
