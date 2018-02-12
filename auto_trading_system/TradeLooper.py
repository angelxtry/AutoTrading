"""
내 정보를 받아온다.
Account 갱신
Asset 갱신
BuySell
- Account와 Asset 정보를 이용
- 목표수익률 도달?
- Y : Asset 매도
- N : 계속 진행
- Asset loop
- 5%이상 상숭 -> 매도
- 5%이상 하락 -> 매도
- DataProvider에게 buy 종목 요청
- buy 종목 exist -> 매수
- not exist -> 진행

"""