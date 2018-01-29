import win32com.client

from daishin import connecion

ST_CODE = 0
ST_NAME = 1
ST_FULL_CODE = 2


def get_name_to_code(stock_name):
    cp_stock_code = win32com.client.Dispatch("CpUtil.CpStockCode")
    return tuple(cp_stock_code.GetData(ST_CODE, i)
                 for i in range(cp_stock_code.GetCount())
                 if cp_stock_code.GetData(ST_NAME, i) == stock_name)


def get_stock_info_to_name(stock_name):
    cp_stock_code = win32com.client.Dispatch("CpUtil.CpStockCode")
    code = cp_stock_code.NameToCode(stock_name)
    name = cp_stock_code.CodeToName(code)
    full_code = cp_stock_code.CodeToFullCode(code)
    index = cp_stock_code.CodeToIndex(code)
    return index, name, code, full_code
    # print(f'Stock Name: {# stock_name}, Stock Name: {name}, Full Code: {full_code} Index: {index}')


def get_code_to_name(code):
    cp_stock_code = win32com.client.Dispatch("CpUtil.CpStockCode")
    return cp_stock_code.CodeToName(code)


def get_kospi_code_name_dict():
    cp_code_mgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
    code_list = cp_code_mgr.GetStockListByMarket(1)
    return {code:cp_code_mgr.CodeToName(code) for code in code_list}


def make_dict_to_csv(dictionary, filename):
    # pprint.pprint(dict)
    with open(filename, 'wt', encoding='utf-8') as f:
        for key, value in dictionary.items():
            f.write(f'{key},{value}\n')


def print_section():
    cp_code_mgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    code_list = cp_code_mgr.GetStockListByMarket(1)

    for i, code in enumerate(code_list):
        second_code = cp_code_mgr.GetStockSectionKind(code)
        name = cp_code_mgr.CodeToName(code)
        print(i, code, second_code, name)


def get_kospi_section(section_code):
    cp_code_mgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    code_list = cp_code_mgr.GetStockListByMarket(1)

    section_code_gene = ((code,
                          cp_code_mgr.CodeToName(code),
                          cp_code_mgr.GetStockSectionKind(code))
                         for code in code_list)
    return [(code, name)
            for code, name, section in section_code_gene
            if section == section_code]


def get_last_price_history(code, count):
    # check_connection()
    cp_stock_chart = win32com.client.Dispatch('CpSysDib.StockChart')
    cp_stock_chart.SetInputValue(0, code)
    cp_stock_chart.SetInputValue(1, ord('2'))
    cp_stock_chart.SetInputValue(4, count)
    cp_stock_chart.SetInputValue(5, 5)
    cp_stock_chart.SetInputValue(6, ord('D'))
    cp_stock_chart.SetInputValue(9, ord('1'))
    cp_stock_chart.BlockRequest()

    data_count = cp_stock_chart.GetHeaderValue(3)
    return [cp_stock_chart.GetDataValue(0, i) for i in range(data_count)]


# def check_connection():
#     instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
#     print(instCpCybos.IsConnect)  # 접속여부 확인 1: 접속, 0: 미접속


def get_multi_data_history():
    cp_stock_chart = win32com.client.Dispatch('CpSysDib.StockChart')

    cp_stock_chart.SetInputValue(0, 'A003540')
    # cp_stock_chart.SetInputValue(1, ord('1'))
    # cp_stock_chart.SetInputValue(2, '20170101')
    # cp_stock_chart.SetInputValue(1, '20170115')
    cp_stock_chart.SetInputValue(1, ord('2'))
    cp_stock_chart.SetInputValue(4, 10)
    cp_stock_chart.SetInputValue(5, (0, 2, 3, 4, 5, 8))
    cp_stock_chart.SetInputValue(6, ord('D'))
    cp_stock_chart.SetInputValue(9, ord('1'))
    cp_stock_chart.BlockRequest()

    data_count = cp_stock_chart.GetHeadValue(3)
    field_count = cp_stock_chart.GetHeadValue(1)

    for i in range(data_count):
        for j in range(field_count):
            print(cp_stock_chart.GetDataValue(j, i), end=' ')
        print("")


def get_data_by_market_eye():
    cp_market_eye = win32com.client.Dispatch('CpSysDib.MarketEye')
    cp_market_eye.SetInputValue(0, (4, 67, 70, 111))
    cp_market_eye.SetInputValue(1, 'A003540')
    cp_market_eye.BlockRequest()

    print('현재가', cp_market_eye.GetDataValue(0, 0))
    print('PER', cp_market_eye.GetDataValue(1, 0))
    print('EPS', cp_market_eye.GetDataValue(2, 0))
    print('최근분기년월', cp_market_eye.GetDataValue(3, 0))


def get_average_volume_60_days():
    cp_stock_chart = win32com.client.Dispatch('CpSysDib.StockChart')
    cp_stock_chart.SetInputValue(0, 'A003540')
    cp_stock_chart.SetInputValue(1, ord('2'))
    cp_stock_chart.SetInputValue(4, 60)
    cp_stock_chart.SetInputValue(5, 8)
    cp_stock_chart.SetInputValue(6, ord('D'))
    cp_stock_chart.SetInputValue(9, ord('1'))
    cp_stock_chart.BlockRequest()

    volumes = list()
    data_count = cp_stock_chart.GetHeaderValue(3)
    for i in range(data_count):
        volume = cp_stock_chart.GetDataValue(0, i)
        volumes.append(volume)

    # 가장 최근일을 제외한 59일치 평균
    averge_volume = (sum(volumes) - volumes[0]) / (len(volumes)-1)

    if volumes[0] > (averge_volume * 10):
        print('대박')
    else:
        print('일반')


KOSPI_STOCK = 1
KOSPI_ETF = 10
KOSPI_ETN = 17


def main():
    connecion.check_connection()
    stock_name = 'SK텔레콤'
    stock_info = get_stock_info_to_name(stock_name)
    print(stock_info)
    # print(get_stock_info_to_name('NAVER'))

    # make_dict_to_csv(get_kospi_code_name_dict(), 'kospi.csv')
    # print_section()
    # pprint.pprint(get_kospi_section(KOSPI_ETF))
    # print(get_last_price_history('A003540', 10))
    # get_multi_data_history()
    # get_data_by_market_eye()
    # get_average_volume_60_days()


if __name__ == '__main__':
    main()
