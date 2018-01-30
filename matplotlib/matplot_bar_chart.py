import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib import style
import numpy as np


font_name = font_manager.FontProperties(
    fname=u'c:\windows\Fonts\malgun.ttf').get_name()
rc('font', family=font_name)
# print(font_name)
"""
font_manager를 이용하여 해당 폰트 파일의 이름을 가져온다.
rc 함수는 configuration을 동적으로 변경한다.
"""
# plt.style.use('ggplot')
"""
plot의 style을 변경
"""

industry = ['통신업', '의료정밀', '운수창고업', '의약품', '음식료품',
            '전기가스업', '서비스업', '전기전자', '종이목재', '증권']
fluctuations = [1.83, 1.30, 1.30, 1.26, 1.06, 0.93, 0.77, 0.68, 0.65, 0.61]


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

"""
plt.barh() 수평 막대 그래프
plt.bar() 수직 막대 그래프
param
1. bar의 위치, 2. bar의 수치, 3. align: bar의 정렬위치
4. height 수평 bar의 높이
plt.yticks 수평 bar는 y축에 ticker를 표시
yticks 함수: ticker의 위치와 각 위치에서의 label

ax.text 함수: 차트에 text를 출력
1. text가 출력되는 x축의 위치
2. text가 출력되는 y축의 위치
3. 출력될 text
4. ha: 수평방향 정렬, va: 수직방향 정렬
"""
# ypos = np.arange(len(industry))
# rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
# plt.yticks(ypos, industry)
# [ax.text(0.95 * rect.get_width(), rect.get_y() + rect.get_height() / 2.0,
# str(fluctuations[i]) + '%', ha='right', va='center')
# for i, rect in enumerate(rects)]

pos = np.arange(len(industry))
rects = plt.bar(pos, fluctuations, align='center', width=0.5)
plt.xticks(pos, industry)
[ax.text(rect.get_x() + rect.get_width() /2.0,
0.95 * rect.get_height(), str(fluctuations[i]) + '%', ha='center')
for i, rect in enumerate(rects)]

plt.xlabel('등락률')
plt.show()
