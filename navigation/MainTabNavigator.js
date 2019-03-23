import React from 'react';
import { Platform } from 'react-native';
import { createStackNavigator, createBottomTabNavigator } from 'react-navigation';

import TabBarIcon from '../components/TabBarIcon';
import RecipesScreen from '../screens/RecipesScreen';
import BarcodeScreen from '../screens/BarcodeScreen';
import ShelfScreen from '../screens/ShelfScreen';

const RecipesStack = createStackNavigator({
  Recipes: RecipesScreen,
});

RecipesStack.navigationOptions = {
  tabBarLabel: 'Recipes',
  tabBarIcon: ({ focused }) => (
    <TabBarIcon
      focused={focused}
      name={
        Platform.OS === 'ios'
          ? `ios-information-circle${focused ? '' : '-outline'}`
          : 'md-information-circle'
      }
    />
  ),
};

const BarcodeStack = createStackNavigator({
  Barcode: BarcodeScreen,
});

BarcodeStack.navigationOptions = {
  tabBarLabel: 'Barcode Scanner',
  tabBarIcon: ({ focused }) => (
    <TabBarIcon
      focused={focused}
      name={Platform.OS === 'ios' ? 'ios-barcode-outline' : 'md-barcode'}
    />
  ),
};

const ShelfStack = createStackNavigator({
  Shelf: ShelfScreen,
});

ShelfStack.navigationOptions = {
  tabBarLabel: 'Shelf',
  tabBarIcon: ({ focused }) => (
    <TabBarIcon
      focused={focused}
      name={Platform.OS === 'ios' ? 'ios-options' : 'md-options'}
    />
  ),
};

export default createBottomTabNavigator({
  RecipesStack,
  BarcodeStack,
  ShelfStack,
});
