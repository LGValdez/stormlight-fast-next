// screens/HomeScreen.js
import React from 'react';
import { View, Text, Button } from 'react-native';
import { useAuth } from '../context/AuthContext';

const HomeScreen = ({ navigation }: { navigation: any }) => {
    const { logout } = useAuth();

    return (
        <View>
            <Text>TS Home Screen</Text>
            <Button title="Manage Orders" onPress={() => navigation.navigate('Orders')} />
            <Button title="New Order" onPress={() => navigation.navigate('New Order')} />
            <Button title="Logout" onPress={logout} />
        </View>
    );
};

export default HomeScreen;
