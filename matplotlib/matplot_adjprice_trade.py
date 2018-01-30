# 동작안함
import matplotlib.pyplot as plt
import pandas_datareader.data as web

sk_hynix = web.DataReader("000660.KS", "yahoo")

fig = plt.figure(figsize=(12, 8))
"""
figsize 인자를 이용해 Figure 객체의 크기를 조정
"""

"""
subplot2grid
(4, 4) 4*4 grid
(0, 0) 시작지점
rowspan, colspan 4*4 gird에서 차지하는 크기
"""
top_axes = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
bottom_axes = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)
"""
하단 그래프에서 거래량 값이 큰 값이 발생할 때
그 값을 오일러 상수(e)의 지수형태로 표시되지 않도록 설정
"""

top_axes.plot(sk_hynix.index, sk_hynix['Adj Close'], label='Adjusted Close')
bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'])

"""
subplot들이 Figure 객체의 영역 내에서 자동으로 최대 크기로 출력
"""
plt.tight_layout()
plt.show()
