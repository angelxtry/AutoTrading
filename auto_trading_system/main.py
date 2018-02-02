from condition.Condition import Condition
from condition.Price import Price
from condition.Price import AssetPriceLow


def main():
    print('test')
    # price = Price(10000)
    # print(price)
    asset_price_low = AssetPriceLow(10000)
    print(asset_price_low)
    buy_sell_1 = Condition.factory()
    print(buy_sell_1)
    print(Condition.conditions)

if __name__ == '__main__':
    main()
