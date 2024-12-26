import React, {useState} from 'react';
import { View, Text, Button } from 'react-native';
import DropDownPicker from "react-native-dropdown-picker";


const AddProductForm = ({ route, navigation }: { route: any, navigation: any }) => {

    const { productData } : { productData: ProductDataType } = route.params;

    const [openQuantityPicker, setOpenQuantityPicker] = useState(false);
    const [quantityValue, setQuantityValue] = useState(null);
    const [quantity, setQuantity] = useState(
        ['1', '2', '3', '4', '5'].map((i) => {
            return {label: i, value: i}
        }));

    return (
        <View>
            <Text>Add Product to Current Order</Text>

            {productData && (
                <>
                    <Text>Adding {productData.name}</Text>

                    <Text>Pick a quantity</Text>
                    <DropDownPicker
                        open={openQuantityPicker}
                        value={quantityValue}
                        items={quantity}
                        setOpen={setOpenQuantityPicker}
                        setValue={setQuantityValue}
                        setItems={setQuantity}
                        zIndex={1000}
                    />

                    {productData.side_dish && productData.side_dish.map((side_dish: SideDishDataType) => (
                        <Text>{side_dish.name}</Text>
                    ))}
                </>
            )}

            <Button title="Cancel" onPress={() => navigation.goBack()} />
        </View>
    );
};

export default AddProductForm;
