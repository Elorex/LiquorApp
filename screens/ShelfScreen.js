import React, { Component } from 'react';
import { Text, View, StyleSheet, ListView, ScrollView } from 'react-native';
import { Constants, SQLite } from 'expo';

export default class ShelfScreen extends Component {
  constructor(props) {
    super(props);
    const ds = new ListView.DataSource({rowHasChanged: (r1, r2) => r1 !== r2});
    
    this.state = {
      inputValue: '',
      dataSource: ds.cloneWithRows([]),
    };
    this._handleRemoval = this._handleRemoval.bind(this);
    this._handleAddToShelf = this._handleAddToShelf.bind(this);
  }

  _handleAddToShelf = () => {
    const textArray = this.state.dataSource._dataBlob.s1;
    textArray.push(this.state.inputValue);
    this.setState(() => ({
      dataSource: this.state.dataSource.cloneWithRows(textArray),
      inputValue: '',
    }));
  };

  _handleRemoval = (id) => {
    this.setState((a) => {
      const newItem = a.dataSource._dataBlob.s1.filter((item, i) => (parseInt(id) !== i));
      return {
        dataSource: this.state.dataSource.cloneWithRows(newItem),
      }
    });
  };
 
  render() {
    return (
      <View style={styles.container}>
        <ListView
          style={styles.listView}
          dataSource={this.state.dataSource}
          renderRow={(rowData, sectionID, rowID) => {
            const handleDelete = () => {
              return this._handleRemoval(rowID);
            }
            const handleAdd = () => {
              return this._handleAddToShelf();
            }
            return (
              <View style={styles.shelflist}>
                <Text style={styles.shelfitem}>{rowData}</Text>
                <Button
                  title="Delete"
                  onPress={handleDelete}
                  style={styles.deleteButton}
                />
              </View>
            );
          }
        }
        />
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
    backgroundColor: '#eee',
  },
  shelflist: {
    borderTopWidth: 1,
    borderColor: '#ccc',
    paddingBottom: 8,
  },
  shelfitem: {
    alignItems: 'center',
    padding: 8,
    width: 320,
    borderTopWidth: 1.5,
    borderColor: '#e0e0e0',
    backgroundColor: '#fff',
    flex: 1,
    flexDirection: 'row',
  },
  element: {
    flex: 1, 
  },
});
