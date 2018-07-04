# encoding: UTF-8
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, date2num
from mpl_finance import candlestick_ohlc
from datetime import datetime


pd.set_option("display.width", 120)
# 设定字体类型，用于正确显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def candlePlot(seriesData, title='a'):
    # 设定日期格式
    Date = [date2num(datetime.strptime(date, '%Y-%m-%d')) for date in seriesData.index]
    seriesData.loc[:, 'Date'] = Date
    # 将DataFrame数据转换成List类型
    listData = []
    for i in range(len(seriesData)):
        a = [seriesData.Date[i], seriesData.Open[i], seriesData.High[i], seriesData.Low[i], seriesData.Close[i]]
        listData.append(a)
    # 设定绘图相关参数
    ax = plt.subplot()
    mondays = WeekdayLocator(MONDAY)
    weekFormatter = DateFormatter('%y %b %d')
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(DayLocator())
    ax.xaxis.set_major_formatter(weekFormatter)
    # 调用candlestick_ohlc函数
    candlestick_ohlc(ax, listData, width=0.7, colorup='r', colordown='g')
    ax.set_title(title)
    # 设定x轴日期显示角度
    plt.setp(plt.gca().get_xticklabels(), rotation=50, horizontalalignment='center')
    return plt.show()


# ssec2015 = pd.read_csv(r'data\SSEC2015.csv')
# ssec2015 = ssec2015.iloc[:, 1:]
# ssec2015.set_index('Date', inplace=True)
# # print(ssec2015.head())
# candlePlot(ssec2015, '上证综指2015年3月份K线图')
ssec2012 = pd.read_csv(r'data\SSEC2012.csv')
ssec2012 = ssec2012.iloc[:, 1:]
ssec2012.set_index('Date', inplace=True)
# ssec2012.index = pd.to_datetime(ssec2012.index, format='%Y-%m-%d')

Close = ssec2012.Close
Open = ssec2012.Open
ClOp = Close - Open
print(ClOp.head())
Shape = [0, 0, 0]
lag1ClOp = ClOp.shift(1)
lag2ClOp = ClOp.shift(2)
# 捕捉绿色实体、十字星和红色实体
for i in range(3, len(ClOp)):
    if all([lag2ClOp[i] < -11, abs(lag1ClOp[i]) < 2, ClOp[i] > 6, abs(ClOp[i]) > abs(lag2ClOp[i] * 0.5)]):
        Shape.append(1)
    else:
        Shape.append(0)
print(Shape.index(1))
# 准备数据
lagOpen = Open.shift(1)
lagClose = Close.shift(1)
lag2Close = Close.shift(2)
# 捕捉符合十字星位置的蜡烛图
Doji = [0, 0, 0]
for i in range(3, len(Open)):
    if all([lagOpen[i] < Open[i], lagOpen[i] < lag2Close[i], lagClose[i] < Open[i], lagClose[i] < lag2Close[i]]):
        Doji.append(1)
    else:
        Doji.append(0)
print(Doji.count(1))
# 定义下跌趋势
# 先计算收益率
ret = Close / Close.shift(1) - 1
lag1ret = ret.shift(1)
lag2ret = ret.shift(2)
# 寻找下跌趋势
Trend = [0, 0, 0]
for i in range(3, len(ret)):
    if all([lag1ret[i] < 0, lag2ret[i] < 0]):
        Trend.append(1)
    else:
        Trend.append(0)
# 寻找“早晨之星”
StarSig = []
for i in range(len(Trend)):
    if all([Shape[i] == 1, Doji[i] == 1, Trend[i] == 1]):
        StarSig.append(1)
    else:
        StarSig.append(0)
# 捕捉上证综指2012年出现“早晨之星”形态的日期
for i in range(len(StarSig)):
    if StarSig[i] == 1:
        print(ssec2012.index[i])

ssec201209 = ssec2012['2012-08-21': '2012-09-30'].copy()
candlePlot(ssec201209, title=u'上证综指2012年9月份的日K线图')
