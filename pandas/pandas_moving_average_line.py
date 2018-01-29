# 이동평균선:
# 일정기간 동안의 주가를 산술 평균한 값인 주가이동평균을 차례로 연결해 만든 선
from pprint import pprint

import matplotlib.pyplot as plt
import pandas as pd


gs = pd.read_csv("GS.csv")

five_days_moving_average = [(gs['Date'][i+4], sum(gs['Adj Close'][i:i+5])/5)
                            for i in range(len(gs)-5)]
pprint(five_days_moving_average)

ma5 = gs['Adj Close'].rolling(window=5).mean()
# pprint(ma5)
# pprint(ma5.tail(10))

# gs['Volume'] != 0 -> True or False

# new_gs = gs[gs['Volume'] !=0]
# 이런식으로 filter를 만들 수 있다.

new_gs = gs
new_gs.insert(len(new_gs.columns), 'MA5', ma5)
# pprint(new_gs)
"""
new_gs에 MA5 컬럼을 추가했다.
"""

ma20 = new_gs['Adj Close'].rolling(window=20).mean()
ma60 = new_gs['Adj Close'].rolling(window=60).mean()
ma120 = new_gs['Adj Close'].rolling(window=120).mean()

new_gs.insert(len(new_gs.columns), 'MA20', ma20)
new_gs.insert(len(new_gs.columns), 'MA60', ma60)
new_gs.insert(len(new_gs.columns), 'MA120', ma120)
# pprint(new_gs)

plt.plot(new_gs.index, new_gs['Adj Close'], label='Adj Close')
plt.plot(new_gs.index, new_gs['MA5'], label='MA5')
plt.plot(new_gs.index, new_gs['MA20'], label='MA20')
plt.plot(new_gs.index, new_gs['MA60'], label='MA60')
plt.plot(new_gs.index, new_gs['MA120'], label='MNA120')

plt.legend(loc='best')
plt.grid()
plt.show()
