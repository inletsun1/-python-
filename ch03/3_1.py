# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
        {'自民投票率': [41.4, 76.3, 59.2, 51.8, 52.5, 53.2, 62.4, 55.0, 57.5], 
         '持ち家比率': [52.8, 71.2, 72.6, 63.7, 81.3, 81.8, 70.9, 74.0, 73.2]},
        columns=['自民投票率', '持ち家比率'],
        index=['北海道', '青森', '岩手', '宮城', '秋田', '山形', '福島', '茨城', '栃木'])

df.plot(kind='scatter', x='自民投票率', y='持ち家比率')
plt.show()
