import React, {useEffect, useState} from 'react';
import { View, Text, Button, TextInput, StyleSheet } from 'react-native';
import DropDownPicker from "react-native-dropdown-picker";
import axios from "axios";

const CreateOrderForm = ({ navigation }: { navigation: any }) => {
    const [openCustomerPicker, setOpenCustomerPicker] = useState(false);
    const [customerValue, setCustomerValue] = useState(null);
    const [customers, setCustomers] = useState([{label: '', value: ''}]);

    const [openProductPicker, setOpenProductPicker] = useState(false);
    const [productValue, setProductValue] = useState<string | null>(null);
    const [products, setProducts] = useState([{label: '', value: ''}]);

    const [availableProductData, setAvailableProductData] = useState([]);
    const [orderNotes, setOrderNotes] = useState('');

    useEffect(() => {
        axios.get("http://localhost:8000/api/customer").then((response) => {
            const allAvailableCustomers = response.data.map((customer : any) => {
                return {label: customer.name, value: customer.customer_id}
            });
            setCustomers(allAvailableCustomers);
        })

        axios.get("http://localhost:8000/api/product").then((response) => {
            setAvailableProductData(response.data);
            const allAvailableProducts = response.data.map((product : ProductDataType) => {
                return {label: product.name, value: product.product_id}
            });
            setProducts(allAvailableProducts);
        })
    }, [])

    useEffect(() => {
        if (productValue) {
            navigation.navigate('Add Product', {
                productData: availableProductData.find((product: ProductDataType) => product.product_id === productValue)
            })
            setProductValue(null);
        }
    }, [productValue])

    return (
        <View>
            <DropDownPicker
                style={styles.dropdownPicker}
                placeholder={"Pick a customer"}
                open={openCustomerPicker}
                value={customerValue}
                items={customers}
                setOpen={setOpenCustomerPicker}
                setValue={setCustomerValue}
                setItems={setCustomers}
                zIndex={1000}
            />

            <DropDownPicker
                placeholder={"Pick a product"}
                style={styles.dropdownPicker}
                open={openProductPicker}
                value={productValue}
                items={products}
                setOpen={setOpenProductPicker}
                setValue={setProductValue}
                setItems={setProducts}
                zIndex={999}
            />

            <TextInput
                style={styles.inputNotes}
                onChangeText={setOrderNotes}
                value={orderNotes}
                placeholder="Additional Notes"
                multiline={true}
            />

            <Button title="Cancel" onPress={() => navigation.goBack()} />
        </View>
    );
};

const styles = StyleSheet.create({
    inputNotes: {
        height: 145,
        marginTop: 15,
        marginBottom: 15,
        borderWidth: 1,
        padding: 20,
        backgroundColor: 'white',
        borderRadius: 8,
        textAlignVertical: 'top',
        width: "96%",
        alignSelf: "center"
    },
    dropdownPicker: {
        marginTop: 10,
        marginBottom: 10,
        width: "96%",
        alignSelf: "center"
    }
});

export default CreateOrderForm;
