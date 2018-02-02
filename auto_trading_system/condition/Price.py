from .Condition import Condition


class Price(Condition):
    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f'{self.price}'


"""
case1
asset의 평균매수가, 현재 시장가격 비교
AssetPriceLow의 instance가 buy에 들어간다면 추가매수
sell에 들어간다면 손절
favorite에 포함된 item의 희망 매수가, 현재 시장가격 비교
buy
asset의 평균 매수가, favorite item의 희망 매수가 - target_price
현재 시장 가격 - market_pice
퍼센트 rate
"""
class AssetPriceLow(Price):
    def __init__(self, price):
        super().__init__(price)

    def isOk(self, buySell):
        # for asset in buySell.getAsset():
            # if(asset.price )
        pass
    
    def __str__(self):
        return f'{self.price}'

    @classmethod
    def _factory(cls, price):
        return Price(price)
