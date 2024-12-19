// App.js
import React from 'react';
import { AuthProvider } from './src/shared/components/context/AuthContext';
import AppNavigator from "./src/shared/components/navigation/AppNavigator";

const App = () => (
    <AuthProvider>
      <AppNavigator />
    </AuthProvider>
);

export default App;
