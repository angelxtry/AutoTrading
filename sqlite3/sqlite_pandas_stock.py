import datetime

import pandas as pd
import pandas_datareader as web
import sqlite3


def get_data_make_df():
    start  = datetime.datetime(2010, 1, 1)
    end = datetime.datetime(2016, 6, 12)
    df = web.DataReader('078930.KS', 'yahoo', start, end)
    # print(df.head())
    return df


def insert_df_to_db(df):
    con = sqlite3.connect('kospi.db')
    df.to_sql('078930', con, if_exists='replace')


def select_db_to_df():
    con = sqlite3.connect('kospi.db')
    read_df = pd.read_sql('SELECT * FROM "078930"', con, index_col='Date')
    return read_df


def main():
    df = get_data_make_df()
    insert_df_to_db(df)
    read_df = select_db_to_df()
    print(read_df.head())


if __name__ == '__main__':
    main()
