from abc.Condition import Condition

class Price(Condition):
    def __init__(self, price):
        self.price = price

class AssetPriceLow(Price):
    @classmethod
    def _factory(cls, price):
        return Price(price)

    def __init__(self, price):
        super(self, price)

    def isOk(self, buySell):
        for asset in buySell.getAsset():
            if(asset.price )

