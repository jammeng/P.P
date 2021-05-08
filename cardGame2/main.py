from Poker import Indian_Poker as IP

# 키보드 입력을 자동으로 입력해주는 모듈
import pyautogui as clear

play = IP()

mode = play.setMode()

# 본격적인 게임 시작 코드블록
# 10 라운드 동안 진행
for i in range(1, 11):

    # 누군가가 파산(잔여 코인 0)했을때 발생하는 코드블록
    if IP.bankruptcy == True:
        play.end_turn()
        break

    # 라운드별 정보 출력
    play.info(i)

    # 랜덤으로 리스트에서 숫자를 가져온 후 해당 인덱스 삭제
    play.shuf_deck()

    if mode == True:            # 쉬운모드
        if IP.Turn == False:    # 내턴
            play.eazy_mode()
            play.my_bet()
            play.op_select()

        elif IP.Turn == True:   # 상대턴
            play.eazy_mode()
            play.op_bet()
            play.my_select()

    elif mode == False:         #어려운모드
        if IP.Turn == False:    # 내턴
            play.my_bet()
            play.hard_mode()

        elif IP.Turn == True:   # 상대턴
            play.op_bet()
            play.my_select()

    # 10 라운드가 진행 되었을때 결과
    if i >= 10:
        play.end_turn()
        break

    if IP.bankruptcy == True:
        play.end_turn()
        break

    # 게임 중간에 빠져나가기 위한 코드 및 Run창 clear 기능
    while True:
        try:
            print("=" * 70)
            rq = int(input("계속 하시겠습니까?:1.......yes    2........no \n입력: "))
            if rq == 1:
                # Run 창에서 ; 를 누르면 Run 창이 초기화 되도록 설정 후
                # ; 를 자동으로 입력받을수 있도록 하는 코드
                clear.press(";")
                break
            elif rq == 2:
                print("게임을 강제종료합니다")
                clear.press("/")
            else:
                print("값을 잘못 입력 하셨습니다")

        except ValueError:
            print("값을 잘못 입력 하셨습니다")
