import matplotlib.pyplot as plt
import numpy as np


# plt.plot([1, 2, 3, 4])
# plt.show()
"""
y축 값 1, 2, 3, 4를 지나는 직선
plot 함수 호출 시 x 축 값을 지정하지 않으면 자동으로 실수값이 할당됨
y축 값이 네 개였으므로 x축 값은 0.0, 1.0, 2.0, 3.0이 할당
"""

# x = range(100)
# y = [v*v for v in x]
# plt.plot(x, y, 'r.')
# plt.show()
"""
plot 함수에 x축, y축 값을 동시에 전달 가능
축 값 외에 인자를 설정하지 않으면 기본 포멧은 파란색 직선 'b-'
'ro' 빨간색 원
'r--' 빨간색 대쉬라인
'bs' 파란색 사각형
'g^' 녹색 삼각형
'y+' 노란색 플러스
'k.' 검은색 점
"""

"""
한 화면에 여러 개의 그래프를 그리기 위해서 figure 함수 사용
figure 함수를 통해 Figure 객체를 먼저 만든 후 add_subplot 메서드를 통해
그래프 개수만큼 subplot을 만든다.
"""
# fig = plt.figure()
# # ax1 = fig.add_subplot(2, 1, 1)
# # ax2 = fig.add_subplot(2, 1, 2)
# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)
# plt.show()
"""
(2, 1, 1)은 2행 1열 중 1번째 그래프를 의미
(2, 1, 2)는 2행 1열 중 2번째 그래프를 의미
즉, 그래프가 위 아래로 2개가 생긴다.

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
그래프가 가로에 2개 생긴다.
"""

# fig = plt.figure()
# ax1 = fig.add_subplot(2, 1, 1)
# ax2 = fig.add_subplot(2, 1, 2)

# x = range(0, 100)
# y = [v*v for v in x]

# ax1.plot(x, y)
# ax2.bar(x, y)
# plt.show()
"""
plot는 선 그래프, bar는 막대그래프
"""

# x = np.arange(0.0, 2*np.pi, 0.1)
# sin_y = np.sin(x)
# cos_y = np.cos(x)

# fig = plt.figure()
# ax1 = fig.add_subplot(2, 1, 1)
# ax2 = fig.add_subplot(2, 1, 2)

# ax1.plot(x, sin_y, 'b--', label='sin(x)')
# ax2.plot(x, cos_y, 'r--', label='cos(x)')

# ax1.set_xlabel('x')
# ax1.set_ylabel('sin(x)')
# ax2.set_xlabel('x')
# ax2.set_ylabel('cos(x)')

# plt.legend(loc='best')

# plt.show()
"""
x는 0.0부터 2*파이까지 0.1씩 증가
set_xlabel, set_ylabel은 x축, y축의 label 출력
legend는 plot() 함수의 label param을 이용하여 범례를 생성
"""

fig = plt.figure()
print(type(fig))
# <class 'matplotlib.figure.Figure'>
# fig는 Figure instance

ax = fig.add_subplot(1, 1, 1)
print(type(ax))
