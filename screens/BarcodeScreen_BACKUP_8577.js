import React, { Component } from 'react';
import { Text, View, StyleSheet, Alert } from 'react-native';
import { Constants, BarCodeScanner, Permissions, SQLite } from 'expo';
import ScanToDB from '../screens/querry/ScanToDB';

export default class App extends Component {
  state = {
    hasCameraPermission: null
  };

  componentDidMount() {
    this._requestCameraPermission();
  }

  _requestCameraPermission = async () => {
    const { status } = await Permissions.askAsync(Permissions.CAMERA);
    this.setState({
      hasCameraPermission: status === 'granted',
    });
  };

  _handleBarcodeScanned = ({type, data}) => {
    ScanToDB.type = type;
    ScanToDB.data = data;
    ScanToDB._scan();
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
<<<<<<< HEAD
import { BaseModel, types } from 'expo-sqlite-orm';

=======

export default class BarcodeScanner extends React.Component {
>>>>>>> 74c4a1f1b50cf0ae9acd58eb0c05efc1266e8263
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
<<<<<<< HEAD
});
  handleBarCodeScanned = ({ type, data }) => {

    if (type==512){barcodeToUPC(data);}
    else if (type==32){barcodeToEAN(data);}
    else{
    //alert(`Bar code with type ${type} and data ${data} has been scanned!`);
    alert("Barcode format is not supported");
    }
  }
}

=======
});*/
>>>>>>> 74c4a1f1b50cf0ae9acd58eb0c05efc1266e8263
