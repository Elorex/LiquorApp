import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { BarCodeScanner, Permissions, SQLite } from 'expo';
import { BaseModel, types } from 'expo-sqlite-orm';

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
      return <Text style={styles.text}>Requesting for camera permission</Text>;
    }
    if (hasCameraPermission === false) {
      return <Text style={styles.text}>No access to camera</Text>;
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

  handleBarcodeScanned = ({ type, data }) => {
    var liquorType;
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

