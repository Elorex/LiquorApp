import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { BarCodeScanner, Permissions } from 'expo';

function barcodeToUPC (data){
  var UPC = data.slice(1,data.length);
  alert(UPC);
}

function barcodeToEAN (data){
  var EAN = data.slice(2,data.length);
  alert(EAN);
}

function addToLib(bcode){
  //Insert into SHELF the data from the Library, where the UPC matches the entered data.
}

export default class BarcodeScannerExample extends React.Component {
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
  handleBarCodeScanned = ({ type, data }) => {

    if (type==512){barcodeToUPC(data);}
    else if (type==32){barcodeToEAN(data);}
    else{
    //alert(`Bar code with type ${type} and data ${data} has been scanned!`);
    alert("Barcode format is not supported");
    }
  }
}