from enum import Enum


class OrderParam(Enum):
    order_type = 0
    account_number = 1
    stock_code = 3
    order_count = 4
    order_price = 5


class Order(Enum):
    sell = 1
    buy = 2
