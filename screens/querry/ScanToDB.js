import { Component } from 'react';
import { Alert } from 'react-native';
import { SQLite } from 'expo';
const db = SQLite.openDatabase('LiquorAppTest (1).db');
export default class ScanToDB extends Component {
    state = {
      'user': 'User',
      'ingredient': 0,
      'upc': 0,
      data: 0,
      type: 0,
    };
    
    componentDidMount() {
        this._scan();
    }

    _scan = () => {
        if (this.state.type === 512) {
            db.transaction ((tx) => {
                tx.executeSql('select upc from Ingredient', [], (tx, result) => {
                if (result & result.rows && result.rows._array) {
                    if (result.row._array === data) {
                    this.setState({'upc': data});
                    var ingredient = rows.item(data).ingredient;
                    this.setState({'ingredient': ingredient});
                    Alert.alert("Added ${ingredient} to Shelf");
                    return;
                    }; 
                    Alert.alert('Drink not found');
                    }
                });
            }); 
        } else {Alert.alert("Barcode format is not supported");}
    };
}
