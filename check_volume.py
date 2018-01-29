import win32com.client
import time

from data_type import DataType
from stock_chart import StockChart


def check_volume(cp_stock_chart, code):
    cp_stock_chart.SetInputValue(StockChart.stock_code.value, code)
    cp_stock_chart.SetInputValue(StockChart.type.value, ord('2'))  # 갯수
    cp_stock_chart.SetInputValue(StockChart.data_count.value, 60)
    cp_stock_chart.SetInputValue(StockChart.data_type.value,
                                 DataType.trade_amount.value)
    cp_stock_chart.SetInputValue(StockChart.data_time_type.value, ord('D'))
    cp_stock_chart.SetInputValue(9, ord('1'))
    cp_stock_chart.BlockRequest()

    volumes = []
    data_count = cp_stock_chart.GetHeaderValue(3)
    for i in range(data_count):
        volume = cp_stock_chart.GetDataValue(0, i)
        volumes.append(volume)

    average_volume = (sum(volumes) - volumes[0]) / (len(volumes)-1)
    if volumes[0] > (average_volume*10):
        return 1
    else:
        return 0


if __name__ == '__main__':
    cp_stock_chart = win32com.client.Dispatch('CpSysDib.StockChart')
    cp_code_mgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
    code_list = cp_code_mgr.GetStockListByMarket(1)

    buy_list = list()
    for code in code_list:
        if check_volume(cp_stock_chart, code) == 1:
            buy_list.append(code)
            print('거래량 폭등 주 발견: ' + code)
            break
        print('일반주: ' + code)
        time.sleep(1)
