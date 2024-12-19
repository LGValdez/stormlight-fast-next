// screens/RegisterScreen.js
import React from 'react';
import { View, Text, Button } from 'react-native';

const RegisterScreen = ({ navigation }: { navigation: any }) => (
    <View>
        <Text>TS Register Screen</Text>
        <Button title="Go to Login" onPress={() => navigation.navigate('Login')} />
    </View>
);

export default RegisterScreen;
