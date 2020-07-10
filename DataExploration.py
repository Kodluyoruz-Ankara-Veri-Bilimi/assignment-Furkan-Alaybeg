import pandas as pd 

class DataExploration:
    def __init__(self, df):
        self.dataframe = df

    def describeData(self):
        print(self.dataframe.describe())
    
    def describeByColumn(self, column):
        print(self.dataframe[column].describe())

    def infoData(self):
            print(self.dataframe.info())
    
    def headData(self, rows):
        print(self.dataframe.head(rows))

    def tailData(self, rows):
        print(self.dataframe.tail(rows))
        
    def checkNullValues(self):
        print(self.dataframe.isnull().sum())
    
    def columnTypes(self):
        print(self.dataframe.dtypes)

    def countData(self):
        print(self.dataframe.count())
    
    def countByColumn(self, column):
        print(self.dataframe[column].count())
    