import React, { Component } from 'react';
import { Text, View, StyleSheet, Alert } from 'react-native';
import { Constants, BarCodeScanner, Permissions, SQLite } from 'expo';
const db = SQLite.openDatabase('LiquorAppTest.db');

export default class App extends Component {
  state = {
    hasCameraPermission: null
  };

  componentDidMount() {
    this._requestCameraPermission();
  };

  _requestCameraPermission = async () => {
    const { status } = await Permissions.askAsync(Permissions.CAMERA);
    this.setState({
      hasCameraPermission: status === 'granted',
    });
  };

  _handleBarcodeScanned = ({type, data}) => {
    var liquorType;
    if (type==512) {
      db.transaction ((tx) => {
        tx.executeSql('select upc from Ingredient', [], (tx, result) => {
          if (result & result.rows && result.rows._array) {
            if (result === data) {
              var ing = rows.item(data).ingredient;
              tx.executeSql('insert into useringredient(user, ingredient, upc) values (user, ?, ?);', [ing, data], () => {
                Alert.alert('insert');
              }); 
            }
          }
          Alert.alert('Drink not found');
        });     
      });
   } else {Alert.alert("Barcode format is not supported");}
  }

  render() {
    return (
      <View style={styles.container}>
        {this.state.hasCameraPermission === null ?
          <Text>Requesting for camera permission</Text> :
          this.state.hasCameraPermission === false ?
            <Text>Camera permission is not granted</Text> :
            <BarCodeScanner
              onBarCodeRead={this._handleBarcodeScanned}
              style={StyleSheet.absoluteFill}
            />
        }
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
  }
});
