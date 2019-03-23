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

/*import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { BarCodeScanner, Permissions, SQLite } from 'expo';

export default class BarcodeScanner extends React.Component {
  state = {
    hasCameraPermission: null,
  }

  async componentDidMount() {
    const { status } = await Permissions.askAsync(Permissions.CAMERA);
    this.setState({ hasCameraPermission: status === 'granted' });
    }

  render() {
    const { hasCameraPermission } = this.state;

    if (hasCameraPermission === null) {
      return <Text>Requesting for camera permission</Text>;
    }
    if (hasCameraPermission === false) {
      return <Text>No access to camera</Text>;
    }
    return (
      <View style={{ flex: 1 }}>
        <BarCodeScanner
          onBarCodeScanned={this.handleBarCodeScanned}
          style={StyleSheet.absoluteFill}
        />
      </View>
    );
  }

  var db = SQLite.openDatabase('LiquorAppTest.db');

  handleBarcodeScanned = ({ type, data }) => {
    var liquorType;
    alert(data);
    if (type==512) {
      db.transaction ((tx) => {
        tx.executeSql('SELECT type FROM ingredient where upc=?', [data], (tx, results) => {
          var len = results.rows.length;
          if (len > 0) {
            liquorType = results.rows.items(0).type;
          } else {
            alert('UPC does not exist');
            return;
          }
        });
        tx.executeSql('INSERT into useringredient(user, ingredient) values (?, ?)', ['user', liquorType], (tx));
        alert('Added to Shelf');
      });

   } else {alert("Barcode format is not supported");}
  }
}

const styles = StyleSheet.create({
  text: {
    flex: 1,
    fontSize: 50,
    textAlign: 'center',
    paddingTop: 200,
  },
});*/