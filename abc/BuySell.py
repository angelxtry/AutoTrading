class BuySell:
    def __init__(self, ts):
        self.conditions = {
            'sell':[],
            'buy':[]
        }
        self.ts = ts

    def add_condition(self, _type, condition, op):
        target = self.conditions[_type]
        target.append(op)
        target.append(condition)

    def remove_condition(self, _type, condition):
        target = self.conditions[_type]
        i = target.index(condition)
        target.remove(i)
        target.remove(i-1)

    def buy(self):
        result = {
            'items' : [{
                'item':1111,
                'qty':3,
                'price':[10000, 11000, 12000]
            }]
        }

        for asset in self.ts.getAccount().getAsset():
            for condition in self.conditions['buy']:
                (qty, low, high) = condition.isOk(self, asset)
                if low == -1:
                    continue

                result['items'].append({
                    'item':asset.item,
                    'qty':qty,
                    'price':[low, high]
                })






