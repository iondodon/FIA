import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import preprocessing


class ValuePredictModel:
    def __init__(self):
        self.model = linear_model.LinearRegression()
        self.__read_data()
        self.__fit()

    def __read_data(self):
        self.pd_data = pd.read_csv('data/apartmentComplexData.txt', delimiter=',')
        self.__normalize_data()
        self.pd_data.columns = [
            '1',
            '2',
            'complexAge',
            'totalRooms',
            'totalBedrooms',
            'complexInhabitants',
            'apartmentsNr',
            '8',
            'medianCompexValue'
        ]
        # take randomly 80% of the data for training purposes
        # and the remaining 20% remain for test purposes
        msk = np.random.rand(len(self.pd_data)) < 0.8
        self.train_data = self.pd_data[msk]
        self.test_data = self.pd_data[~msk]

    def __normalize_data(self):
        data = self.pd_data.values  # returns a numpy array
        self.min_max_scaler = preprocessing.MinMaxScaler()
        data_scaled = self.min_max_scaler.fit_transform(data)
        self.pd_data = pd.DataFrame(data_scaled)

    def __fit(self):
        self.model = self.model.fit(
            self.train_data[[
                '1',
                '2',
                'complexAge',
                'totalRooms',
                'totalBedrooms',
                'complexInhabitants',
                'apartmentsNr',
                '8',
            ]],
            self.train_data[['medianCompexValue']]
        )

    def predict(self, pd_test_data):
        return self.model.predict(
            pd_test_data[[
                '1',
                '2',
                'complexAge',
                'totalRooms',
                'totalBedrooms',
                'complexInhabitants',
                'apartmentsNr',
                '8'
            ]]
        )
