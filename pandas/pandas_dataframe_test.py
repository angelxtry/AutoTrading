from pandas import Series, DataFrame


raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)
print(data['col2'])

print(type(data['col1']))
"""
DataFrame의 각 컬럼은 Series객체
<class 'pandas.core.series.Series'>
"""

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day = DataFrame(daeshin)
print(daeshin_day)

# DataFrame을 생성할 때 컬럼의 순서를 지정
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'])
print(daeshin_day)

# DataFrame을 생성할 때 컬럼의 순서 및 index 지정
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'],
                        index=date)
print(daeshin_day)

# 컬럼 선택
close = daeshin_day['close']
print(type(close))
print(close)

# 특정 index의 row data에 접근하려면 ix 메소드
day_data = daeshin_day.ix['16.02.24']
print(type(day_data))
print(day_data)
"""
<class 'pandas.core.series.Series'>
open     11100
high     11100
low      10950
close    11100
Name: 16.02.24, dtype: int64
"""

print(daeshin_day.columns)
print(daeshin_day.columns[1])
print(daeshin_day.index)
print(daeshin_day.index[2])
"""
Index(['open', 'high', 'low', 'close'], dtype='object')
high
Index(['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23'], dtype='object')
16.02.25
"""
