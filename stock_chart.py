from enum import Enum


class StockChart(Enum):
    stock_code = 0  # 주식코드
    type = 1  # 1.기간, 2.갯수
    start_date = 2  # 기간 요청 시작일
    end_date = 3  # 기간 요청 종료일
    data_count = 4  # 요청 갯수
    data_type = 5  # 데이터 유형
    # 0: 날짜, 1: 시간, 2: 시가, 3: 고가, 4: 저가,
    # 5: 종가, 6: 전일대비, 8: 거래량, 9: 거래대금, 10: 누적체결매도수량
    data_time_type = 6  # ‘D’: 일, ‘W’: 주, ‘M’: 월, ‘m’: 분, ‘T’: 틱
    modified_price = 9  # 수정주가 ‘0’: 무수정주가, ‘1’: 수정주가
