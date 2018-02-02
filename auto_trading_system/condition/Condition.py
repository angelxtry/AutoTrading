class Condition:
    conditions = []
    @classmethod
    def factory(cls):
        for v in Condition.conditions:
            if isinstance(v, cls):
                return v
        temp = cls._factory()
        Condition.conditions.append(temp)
        return temp

    @classmethod
    def _factory(cls):
        pass

    def __init__(self):
        pass

    def isOk(self, buySell):
        pass

    def forAsset(self):
        return False

