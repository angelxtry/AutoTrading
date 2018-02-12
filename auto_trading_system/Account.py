from auto_trading_system import Asset


class Account:
    def __init__(self):
        self.d2deposit = 0
        self.assets = []

    def set_d2deposit(self, deposit):
        self.d2deposit = deposit

    def set_assets(self, stocks):
        append = self.assets.append()
        for stock_name, number, buy_price, cur_price, profit_loss, _yield in stocks:
            asset = new Asset(stock_name, number, buy_price)
            append(asset)

