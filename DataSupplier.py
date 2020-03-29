import json
import pandas as pd

from DataTypeSource import DataTypeSource

class DataSupplier:

    COUNTY_DATA = DataTypeSource.COUNTY.name + ".csv"
    STATE_DATA = DataTypeSource.STATE.name + ".csv"

    def __init__(self):
        return

    def __getDataFrame(self, fileName):
        return pd.read_csv(fileName)

    def __extractData(self, row, dataType):
        data = {}
        prefix = dataType.value[0]
        data[prefix] = row[prefix]
        data[prefix + 'Cases'] = str(row['cases'])
        data[prefix + 'Deaths'] = str(row['deaths'])
        data[prefix + 'AsOf'] = row['date']
        return data

    def __getData(self, stateName, countyName = None):
        print(stateName)
        state = stateName.lower()
        state_df = self.__getDataFrame(self.STATE_DATA)
        data = {}
        if countyName:
            county = countyName.lower()
            county_df = self.__getDataFrame(self.COUNTY_DATA)
            county_match = county_df.loc[(county_df['county'] == county) & (county_df['state'] == state)]
            if len(county_match.index) == 1:
                county_row = county_match.iloc[0]
                county_data = self.__extractData(county_row, DataTypeSource.COUNTY)
                data.update(county_data)

        state_match = state_df[state_df['state'] == state]
        if len(state_match.index) == 1:
            state_row = state_match.iloc[0]
            state_data = self.__extractData(state_row, DataTypeSource.STATE)
            data.update(state_data)
        return json.dumps(data)

    def getData(self, params):
        if 'state' not in params.keys():
            return json.dumps({})
        stateNames = params.get('state')
        countyNames = params.get('county', [None])
        if len(stateNames) != 1 or len(countyNames) != 1:
            return json.dumps({})

        return self.__getData(stateNames[0], countyNames[0])