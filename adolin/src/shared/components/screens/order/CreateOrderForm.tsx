import React, {useEffect, useState} from 'react';
import { View, Text, Button } from 'react-native';
import DropDownPicker from "react-native-dropdown-picker";
import axios from "axios";

const CreateOrderForm = ({ navigation }: { navigation: any }) => {
    const [openCustomerPicker, setOpenCustomerPicker] = useState(false);
    const [customerValue, setCustomerValue] = useState(null);
    const [customers, setCustomers] = useState([{label: '', value: ''}]);

    const [openProductPicker, setOpenProductPicker] = useState(false);
    const [productValue, setProductValue] = useState(null);
    const [products, setProducts] = useState([{label: '', value: ''}]);

    useEffect(() => {
        axios.get("http://localhost:8000/api/customer").then((response) => {
            const allAvailableCustomers = response.data.map((customer : any) => {
                return {label: customer.name, value: customer.customer_id}
            });
            setCustomers(allAvailableCustomers);
        })

        axios.get("http://localhost:8000/api/product").then((response) => {
            const allAvailableProducts = response.data.map((product : any) => {
                return {label: product.name, value: product.product_id}
            });
            setProducts(allAvailableProducts);
        })
    }, [])

    return (
        <View>
            <Text>Create Order Screen</Text>

            <Text>Pick a customer</Text>
            <DropDownPicker
                open={openCustomerPicker}
                value={customerValue}
                items={customers}
                setOpen={setOpenCustomerPicker}
                setValue={setCustomerValue}
                setItems={setCustomers}
                zIndex={1000}
            />

            <Text>Pick a product</Text>
            <DropDownPicker
                open={openProductPicker}
                value={productValue}
                items={products}
                setOpen={setOpenProductPicker}
                setValue={setProductValue}
                setItems={setProducts}
                zIndex={999}
            />
            <Button title="Cancel" onPress={() => navigation.goBack()} />
        </View>
    );
};

export default CreateOrderForm;
