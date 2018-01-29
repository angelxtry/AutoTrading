from daishin import auto_login
from daishin import connecion
from daishin.daishin_user_info import UserInfo


def main():
    if connecion.check_connection():
        print('이미 접속 중입니다.')
    else:
        auto_login.execute_cybosplus(UserInfo.id, UserInfo.pw, UserInfo.cert)

    # order_book 확인
    # order_book에 등록된 내용을 조회
    # 판단
    # 매수 or 매도

    # 판단 함수에서 종목 조회 함수를 실행
    # 판단 함수에서 매수 매도를 수행
    # 판단 함수에서 결과 통보

    # 판단 함수가 프로그램 전체를 컨트롤?
    # 매수매도는 각 클래스에 정보를 던지면 처리
        # 매수매도결과는 어떻게 통보할까?

if __name__ == '__main__':
    main()
