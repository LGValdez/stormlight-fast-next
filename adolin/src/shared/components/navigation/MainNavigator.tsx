import DashboardNavigator from "./dashboard/DashboardNavigator.tsx";
import React from "react";
import {createNativeStackNavigator} from "@react-navigation/native-stack";
import OrderNavigator from "./order/OrderNavigator.tsx";
import CreateOrderForm from "../screens/order/CreateOrderForm.tsx";

const Stack = createNativeStackNavigator();

const MainNavigator = () => {

    return <Stack.Navigator>
        <Stack.Screen name="Dashboard" component={DashboardNavigator} />
        <Stack.Screen name="Orders" component={OrderNavigator} />
        <Stack.Screen name="New Order" component={CreateOrderForm} />
    </Stack.Navigator>
};

export default MainNavigator;