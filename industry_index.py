import win32com.client


def check_connection():
    cp_cybos = win32com.client.Dispatch('CpUtil.CpCybos')
    cp_cybos.IsConnect
    if cp_cybos.IsConnect == 1:
        print('PLUS 연결!')
    else:
        print('PLUS가 정상적으로 연결되지 않음.')
        exit()


def get_industry_code_name_list():
    cp_code_mgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')

    industry_code_list = cp_code_mgr.GetIndustryList()

    for industry_code in industry_code_list:
        print(industry_code, cp_code_mgr.GetIndustryName(industry_code))


def get_stock_info_by_industry_code(industry_code):
    cp_code_mgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
    stock_code_list = cp_code_mgr.GetGroupCodeList(industry_code)

    for code in stock_code_list:
        print(code, cp_code_mgr.CodeToName(code))


def get_average_industry_per(industry_code):
    cp_code_mgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
    cp_market_eye = win32com.client.Dispatch('CpSysDib.MarketEye')

    industry_stock_list = cp_code_mgr.GetGroupCodeList(industry_code)
    cp_market_eye.SetInputValue(0, 67)
    cp_market_eye.SetInputValue(1, industry_stock_list)
    cp_market_eye.BlockRequest()
    stock_count = cp_market_eye.GetHeaderValue(2)

    sumPer = 0
    for i in range(stock_count):
        sumPer += cp_market_eye.GetDataValue(0, i)
    return sumPer / stock_count


if __name__ == '__main__':
    check_connection()
    get_industry_code_name_list()
    get_stock_info_by_industry_code(5)
    print(get_average_industry_per(5))
