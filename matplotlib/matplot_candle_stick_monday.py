import datetime

import pandas_datareader.data as web
import matplotlib.finance as matfin
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


start = datetime.datetime(2017, 3, 1)
end = datetime.datetime(2017, 3, 31)
skhynix = web.DataReader('000660.KS', 'yahoo', start, end)
skhynix = skhynix[skhynix['Volume'] > 0]

day_list = [(i, day.strftime('%y-%m-%d')+'(Mon)')
            for i, day in enumerate(skhynix.index) if day.dayofweek == 0]
print(day_list)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_major_locator(ticker.FixedLocator([i for i, day in day_list]))
ax.xaxis.set_major_formatter(
    ticker.FixedFormatter([day for i, day in day_list]))
"""
x축의 ticker를 설정
"""

# ax.set_xticks([i for i, day in day_list])
# ax.set_xticklabels([day for i, day in day_list])
"""
set_xticks는 set_major_locator를 wrapping 한 것 같다.
"""

matfin.candlestick2_ohlc(ax,
                         skhynix['Open'], skhynix['High'],
                         skhynix['Low'], skhynix['Close'],
                         width=0.5, colorup='r', colordown='b')
"""
1. AxesSubplot
2. 시가, 3.고가, 4. 저가, 5. 종가
6. 봉의 너비, 7. 양봉의 색깔, 8. 음봉의 색깔
"""
plt.show()
