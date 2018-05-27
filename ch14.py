# encoding: UTF-8

from __future__ import division

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from scipy import stats

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# RandomNumber = np.random.choice([1, 2, 3, 4, 5], size=100, replace=True, p=[0.1, 0.1, 0.3, 0.3, 0.2])
# print(RandomNumber)
# print(pd.Series(RandomNumber).value_counts())
# print(pd.Series(RandomNumber).value_counts() / 100)

HSRet300 = pd.read_csv('./data/return300.csv')
print(HSRet300.head())
# density = stats.kde.gaussian_kde(HSRet300.iloc[:, 1])
# bins = np.arange(-5, 5, 0.02)
# plt.subplot(211)
# plt.plot(bins, density(bins))
# plt.title(u'沪深300收益率序列的概率密度曲线图')
# plt.subplot(212)
# plt.plot(bins, density(bins).cumsum())
# plt.title(u'沪深300收益率序列的累计分布函数图')
# plt.show()

# print(np.random.binomial(100, 0.5, 20))
# print(stats.binom.pmf(20, 100, 0.5))
# print(stats.binom.pmf(50, 100, 0.5))
# dd = stats.binom.pmf(np.arange(0, 21, 1), 100, 0.5)
# print(dd)
# print(dd.sum())
# print(stats.binom.cdf(20, 100, 0.5))

ret = HSRet300.iloc[:, 1]
p = len(ret[ret > 0]) / len(ret)
print(p)
print(stats.binom.pmf(6, 10, p))
