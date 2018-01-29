# 동작안함
from datetime import datetime
from pandas_datareader import data
from pandas_datareader.google.daily import GoogleDailyReader

@property
def url(self):
    return "https://finance.google.com/finance/get_price"
GoogleDailyReader.url = url

start = datetime(2016, 2, 19)
end = datetime(2016, 3, 4)

# samsungfire = data.DataReader('KRX: 000810', 'google', start, end)
kospi = data.DataReader("F", 'google', start, end)
print(samsungfire)
