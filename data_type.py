from enum import Enum


class DataType(Enum):
    date = 0
    time = 1
    open_price = 2
    high_price = 3
    low_price = 4
    end_price = 5
    diff_price_before_biz_day = 6
    trade_amount = 8
    trade_money = 9
    accum_amount = 10

# 0: 날짜, 1: 시간, 2: 시가, 3: 고가, 4: 저가,
# 5: 종가, 6: 전일대비, 8: 거래량, 9: 거래대금, 10: 누적체결매도수량
