import requests
from bs4 import BeautifulSoup

def get_3year_treasury():
    url = ("http://www.index.go.kr/strata/jsp/showStblGams3.jsp?"
           "stts_cd=288401&amp;idx_cd=2884&amp;freq=Y&amp;period=1998:2017")
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    tr_data = soup.find_all('tr', id='tr_288401_1')
    td_data = tr_data[0].find_all('td')

    treasury_3year = {}
    start_year = 1998

    for x in td_data:
        treasury_3year[start_year] = x.text
        start_year += 1

    print(treasury_3year)
    return treasury_3year


def main():
    get_3year_treasury()


if __name__ == '__main__':
    main()
