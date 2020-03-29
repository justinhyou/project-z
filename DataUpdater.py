import io
import pandas as pd
import requests

from DataTypeSource import DataTypeSource
import Util

class DataUpdater: 

    def __init__(self):
        return

    def __getCSV(self, uriString):
        with requests.Session() as s:
            download = s.get(uriString)
            return download.content.decode('utf-8')

    def __updateCSV(self, dataTypeSource):
        content = self.__getCSV(dataTypeSource.value[1])
        pd_frame = pd.read_csv(io.StringIO(content))
        pd_frame['date'] = pd_frame['date'].apply(lambda dateString: Util.parseDate(dateString))
        pd_frame['state'] = pd_frame['state'].apply(lambda stateName: stateName.lower())

        group_by = ["state"]
        sourceName = dataTypeSource.value[0]
        if sourceName != 'state':
            pd_frame[sourceName] = pd_frame[sourceName].apply(lambda name: name.lower())
            group_by.append(dataTypeSource.value[0])

        collapsed_content = pd_frame.groupby(group_by, as_index = False).max()

        fileName = dataTypeSource.name + ".csv"

        collapsed_content.to_csv(Util.workspace() + "/" + fileName, index = False)

    def update(self):
        self.__updateCSV(DataTypeSource.COUNTY)
        self.__updateCSV(DataTypeSource.STATE)
