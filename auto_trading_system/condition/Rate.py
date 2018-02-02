"""
Asset: 내가 보유하고 있는 item
Favorite: 내가 관심있는 item
----
Asset
UpperRate (+5%) 평균매수가: 10000
평균매수가 + (평균매수가*rate)
sell cond -> 매도
buy cond -> 매수(더 오를 것 같다.)

UnderRate (-5%) 평균매수가: 10000
평균매수가 + (평균매수가*rate)
sell cond -> 매도
buy cond -> 매수
"""
class Rate:
    def __init__(self, rate):
        self.rate = rate


class UnderRate(Rate):
    def __init__(self, rate):
        super().__init__(rate)

    """
    buy_sell은 item을 가지고 있다.
    item은 평균매수가, 희망
    """
    def is_ok(self, buy_sell):
        for asset
