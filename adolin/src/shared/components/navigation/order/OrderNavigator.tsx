// navigation/DashboardNavigator.js
import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import OrderListScreen from '../../screens/order/OrderListScreen.tsx';

const Tab = createBottomTabNavigator();

const OrderNavigator = ({ navigation }: { navigation: any }) => {
    return <Tab.Navigator screenOptions={{headerShown: false}}>
        <Tab.Screen
            name="Ongoing"
            children={() => <OrderListScreen state={"Ongoing"} navigation={navigation}/>}
        />
        <Tab.Screen
            name="Completed"
            children={() => <OrderListScreen state={"Completed"} navigation={navigation}/>}
        />
        <Tab.Screen
            name="Cancelled"
            children={() => <OrderListScreen state={"Cancelled"} navigation={navigation}/>}
        />
    </Tab.Navigator>
};

export default OrderNavigator;
