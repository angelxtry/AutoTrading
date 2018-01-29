from pandas import Series, DataFrame


# Series 객체 생성
# Series 객체를 생성할 때 인덱스를 지정하지 않았다면
# 0 부터 시작하는 정수로 인덱싱
kakao = Series([123, 345, 234, 567, 123])
print(kakao)

print(kakao[0])

# index 지정
kakao1 = Series([123, 345, 234, 567, 123], index=['2016-02-19',
                                                  '2016-02-18',
                                                  '2016-02-17',
                                                  '2016-02-16',
                                                  '2016-02-15'])
print(kakao1)
print('2016-02-19')

# index 출력
for date in kakao1.index:
    print(date)

# 값 출력
for price in kakao1.values:
    print(price)

mine   = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

# 같은 index를 가진 Series 객체를 더하면
# index를 고려하여 덧셈을 수행한다.
# index의 순서는 고려하지 않아도 된다.
merge = mine + friend
print(merge)

mine1   = Series([10, 20, 30], index=['naver', 'sk2', 'kt'])
friend1 = Series([10, 30, 20], index=['kt', 'naver', 'sk1'])
merge1 = mine1 + friend1
print(merge1)
"""
두 Series에 동일하지 않은 index는 NaN
index 자체는 합집합
kt       40.0
naver    40.0
sk1       NaN
sk2       NaN
dtype: float64
"""