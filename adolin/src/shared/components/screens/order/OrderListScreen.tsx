import React from 'react';
import { View, Text, Button } from 'react-native';

const OrderListScreen = ({state, navigation}: { state: string; navigation: any }    ) => {

    return (
        <View>
            <Text>{state} Orders</Text>
            <Button title="Exit" onPress={() => navigation.goBack()} />
        </View>
    );
};

export default OrderListScreen;
