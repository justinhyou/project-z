from enum import Enum, unique

@unique
class DataTypeSource(Enum):
  COUNTY = ('county', "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
  STATE = ('state', "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
  COUNTRY = ""
