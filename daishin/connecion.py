import win32com.client

NOT_CONNECT = 0
CONNECT_SUCCESS = 1


def check_connection():
    cp_cybos = win32com.client.Dispatch("CpUtil.CpCybos")
    if cp_cybos.IsConnect == CONNECT_SUCCESS:
        print('Server Connection Success.')
        return True
    else:
        print('Server Connection Error.')  # 접속여부 확인 1: 접속, 0: 미접속
        return False
        # exit()
