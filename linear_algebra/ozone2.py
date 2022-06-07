import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


class Solution(object):
    def __init__(self):
        url = "https://raw.githubusercontent.com/reisanar/datasets/master/ozone.data.csv"
        self.df = pd.read_csv(url)
        self.training_data = self.df[['temp', 'ozone']]
        self.training_data = self.training_data.dropna(how='any')
        self.x_data = self.training_data['temp'].values.reshape(-1, 1)
        self.t_data = self.training_data['ozone'].values.reshape(-1, 1)
        self.model = linear_model.LinearRegression()

    def solution(self):
        self.model.fit(self.x_data, self.t_data)

        # 6. W와 b값을 알아내보자
        # model.coef_ : W / model.intercept_ : b
        print('W : {}, b : {}'.format(self.model.coef_, self.model.intercept_))
        # W : [[2.4287033]], b : [-146.99549097]

        # 7. 예측 수행
        predict_val = self.model.predict([[62]])  # 온도를 이용해서 오존량 예측
        print(predict_val)  # [[3.58411393]]

        # 8. 그래프로 확인해보자
        plt.scatter(self.x_data, self.t_data)
        plt.plot(self.x_data, np.dot(self.x_data, self.model.coef_) + self.model.intercept_, color='r')
        plt.show()


if __name__ == '__main__':
    Solution().solution()