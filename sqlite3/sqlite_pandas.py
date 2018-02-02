import datetime
import pandas as pd
from pandas import Series, DataFrame
import pandas_datareader.data as web
import sqlite3


def write_db_by_df():
    con = sqlite3.connect('kospi.db')

    raw_data = {'col0': [1, 2, 3, 4],
                'col1': [10, 20, 30, 40],
                'col2': [100, 200, 300, 400],}

    df = DataFrame(raw_data)
    df.to_sql('test', con)
    """
    DataFrame 객체 내의 데이터를 데이터 베이스로 저장하기 위해 to_sql 함수 사용
    """

def read_db_by_df():
    con = sqlite3.connect('kospi.db')
    df = pd.read_sql('select * from test', con, index_col=None)
    """
    db데이터를 DataFrame에 바로 담는다.
    """
    print(df)


if __name__ == '__main__':
    read_db_by_df()

"""
DataFrame.to_sql(name, con, flavor='sqlite', schema=None,
                 if_exists='fail', index=True, index_label=None,
                 chunksize=None, dtype=None)
name: 테이블명
con: cursor 객체
flavor: DBMS 지정, 기본값은 sqlite
schema: Schema 지정, 기본값 None
if_exists: DB에 테이블이 존재할 때, 기본값 fail
    fail: DB에 테이블이 이미 존재한다면 아무것도 하지 않는다.
    replace: 테이블이 존재하면 기존 테이블을 삭제하고 새로 생성 후 데이터 insert
    append: 테이블이 존재하면 데이터만 추가
index: DataFrame의 index를 DB에 추가할지 여부, 기본값 True
index_label: index 컬럼에 대한 label 지정, 기본값 None
chunksize: 한 번에 써지는 row의 크기, 정수, 기본값 None(df의 모든 컬럼을 한번에)
dtype: 컬럼에 대한 SQL 타입을 python dict로 넘겨줄 수 있다.

df 객체에 데이터가 많을 경우 패킷 사이즈 제약으로 에러가 발생할 수 있다.
이럴때는 chunksize를 지정한다.
"""
