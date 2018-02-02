import sqlite3


print('sqlite3 모듈 자체 버전: ', sqlite3.version)
print('SQLite 버전: ', sqlite3.sqlite_version)

con = sqlite3.connect('kospi.db')
print(type(con))

cursor = con.cursor()
"""
SQL구문을 호출하기 위해 Cursor 객체가 필요
"""

create_sql = ("CREATE TABLE IF NOT EXISTS kakao("
              "Date text, Open int, High int,"
              "Low int, Closing int, Volumn int)")

print(create_sql)

cursor.execute(create_sql)

insert_sql = ("INSERT INTO kakao VALUES("
              "'16.06.03', 97000, 98600, 96900, 98000, 321405)")
cursor.execute(insert_sql)
con.commit()
con.close()
