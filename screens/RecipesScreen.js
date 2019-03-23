import React, { Component } from 'react';
import { Text, View, StyleSheet, ScrollView } from 'react-native';
import { Constants } from 'expo';
const DATA = Array.from(Array(100)).map((_, i) => <Text>{i}</Text>)

export default class RecipeList extends Component {
  render() {
    
    return (
      <View style={styles.container}>
        <ScrollView style={styles.scrollview} contentContainerStyle={styles.innerview}>
          {DATA}
        </ScrollView>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: Constants.statusBarHeight,
    backgroundColor: '#ecf0f1',
  },
  scrollview: {
    width: 340,
    backgroundColor: 'blue',
  },
  innerview: {
    backgroundColor: 'green',
    width: 100,
  },
});
