import random
import pyautogui as pag

class Indian_Poker:
    bankruptcy = False      # 파산 했을경우 TRUE 값으로 바뀌면서 게임 종료
    Turn = False            # 차례 구분 변수 False 이면 사용자 차례

    def __init__(self):
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.my_money = 10          # 사용자 보유 코인 초기 값
        self.op_money = 10          # 컴퓨터 보유 코인 초기 값
        self.money = 0              # 매번 입력하는 코인 갯수 초기 값
        self.card_open = False      # 카드 출력시 False면 내카드 비공개 True면 공개


    # 쉬운 모드와 어려운 모드를 선택하는 메소드
    def setMode(self):
        while True:
            try:
                print("난이도 선택: 1.....쉬운모드   2.....어려운모드")
                self.mode = int(input("입력하세요: "))
                if self.mode == 1:
                    print("쉬운 모드를 선택하셨습니다")
                    self.mode = True
                    break
                elif self.mode == 2:
                    print("어려운 모드를 선택하셨습니다")
                    self.mode = False
                    break
                else:
                    print("다시입력하세요")
            except ValueError:
                print("다시입력하세요")

        return self.mode

    # 라운드 시작시 현재 상태를 알려주는 메소드
    def info(self, round):
        print("="*70)
        print("==== 나의 코인: ", self.my_money, " ====== 현재 라운드: ", round, " ====== 상대 코인: ", self.op_money, " ====")
        print("="*70)
        return round

    # 랜덤으로 덱 리스트에서 숫자를 가져온 후 해당 인덱스 삭제 하고,
    # 상대의 카드를 화면에 출력해주는 메소드
    # 출력시 플레이어 카드는 비공개한 후 True 값으로 변경
    def shuf_deck(self):
        self.op_card = random.choice(self.deck)
        del self.deck[self.deck.index(self.op_card)]
        self.my_card = random.choice(self.deck)
        del self.deck[self.deck.index(self.my_card)]

        # 게임 시작시 상대 카드,내카드를 보여주는 메소드 호출
        Indian_Poker.SHOW_OPCARD(self)
        Indian_Poker.SHOW_MYCARD(self)

        # 배팅전에는 무조건 사용자 카드는 비공개 해야하기때문에 True
        self.card_open = True

        return self.op_card, self.my_card

    # 배팅할 코인을 직접 입력하는 메소드
    # 최대로 입력 가능한 코인 갯수는 5코인이며 플레이어와 상대방의 잔여 코인수에 따른 최대량 제한 있음
    # 플레이어 차례가 끝나면 턴을 True로 변경
    def my_bet(self):
        while self.my_money >= 0:
            if self.op_money <= 4:
                print(f"배팅 가능 코인은 1~{self.op_money}원 입니다.")
            elif self.my_money <= 4:
                print(f"배팅 가능 코인은 1~{self.my_money}원 입니다.")
            else:
                print("배팅 가능 코인은 1~5원 입니다.")
            print("="*70)

            self.money = input("배팅 코인 입력: ")
            if self.money == '1' or self.money == '2' or self.money == '3' or self.money == '4' or self.money == '5':
                self.money = int(self.money)

                if self.money > self.my_money:
                    print('보유코인이 부족합니다. 다시 입력하세요.')
                elif self.money < 1:
                    print('배팅코인이 너무 적습니다. 다시 입력하세요.')
                elif self.money > 5:
                    print("배팅코인이 너무 많습니다. 다시 입력하세요.")
                elif self.money > self.op_money:  # 상대방 최대 잔액을 맞춰 주기위한 출력문
                    print("배팅코인이 상대방의 보유코인보다 높습니다.")

                elif 1 <= self.money <= 5 and self.money <= self.op_money:
                    self.my_money = self.my_money - self.money
                    break
            else:
                print("다시 입력하세요")

        Indian_Poker.Turn = True
        return self.my_money, self.op_money

    # 컴퓨터가 배팅금액을 결정하는 메소드( eazy모드 )
    # 플레이어 잔여 코인을 계산후 그에 따른 배팅 코인 값 랜덤 선택
    # 컴퓨터 차례가 끝나면 턴을 False 로 변경
    def op_bet(self):
        while self.op_money >= 0:
            if self.op_money <= 4:
                self.money = random.randint(1, self.op_money)
                print(f"상대방이 {self.money}코인 만큼 배팅 하였습니다")
                print("=" * 70)
                self.op_money -= self.money
                break
            elif self.my_money >= 5:
                self.money = random.randint(1, 5)
                if 1 <= self.money <= 5 :
                    print(f"상대방이 {self.money}코인 만큼 배팅 하였습니다")
                    print("=" * 70)
                    self.op_money -= self.money
                    break

            elif self.my_money <= 4:
                self.money = random.randint(1, self.my_money)
                print(f"상대방이 {self.money}코인 만큼 배팅 하였습니다")
                print("=" * 70)
                self.op_money -= self.money
                break

        Indian_Poker.Turn = False
        return self.op_money

    # 컴퓨터가 Die를 선택했을때 발생하는 메소드
    # Die를 선택할 경우 컴퓨터 보유 코인 - 1
    # 플레이어가 배팅한 코인(self.money)과 1코인을 더한 코인을 플레이어 전체 보유코인(self.my_money)에 저장
    def op_Die(self):
        print("="*70)
        print("상대방이 Die를 선택 했습니다.")
        self.my_money = self.my_money + self.money + 1
        self.op_money = self.op_money - 1

        if self.op_money <= 0:
            print("게임에서 이겼습니다.")
            Indian_Poker.bankruptcy = True

        return self.my_money, self.op_money, self.money

    # 컴퓨터가 Call을 했을때 발생하는 메소드
    # Call 선택시 플레이어가 제시한 코인 만큼 차감 (self.op_money -= money)
    # 승리시 플레이어가 걸었던 코인 두배를 가지고 오고 패배시 플레이어가 제시한 코인을 잃음 무승부일 경우에는 원상복귀
    def op_Call(self):
        print("="*70)
        print("상대방이 call을 선택 했습니다.")
        self.op_money -= self.money
        if self.op_card < self.my_card:
            self.my_money += 2 * self.money
            print("승리하셨습니다.")

            if self.op_money <= 0:
                print("게임에서 이겼습니다.")
                Indian_Poker.bankruptcy = True

        elif self.op_card > self.my_card:
            self.op_money += 2 * self.money
            print("패배하셨습니다.")

            if self.my_money <= 0:
                print("게임에서 졌습니다.")
                Indian_Poker.bankruptcy = True

        else:
            self.my_money += self.money
            self.op_money += self.money
            print("무승부입니다.")


        return self.my_money, self.op_money

    # 상대방 차례일때 플레이어가 call, die 를 선택하는 메소드
    def my_select(self):
        while True:
            print("1.................Call                        2....................Die")
            self.select = input("입력하세요: ")
            if self.select == '1':
                self.select = 1
                print("=" * 70)
                print("당신은 call을 선택 하셨습니다.")
                self.my_money -= self.money
                if self.op_card < self.my_card:
                    self.my_money += 2 * self.money
                    print("승리하셨습니다.")

                    if self.op_money <= 0:
                        print("게임에서 이겼습니다.")
                        Indian_Poker.bankruptcy = True

                elif self.op_card > self.my_card:
                    self.op_money += 2 * self.money
                    print("패배하셨습니다.")

                    if self.my_money <= 0:
                        print("게임에서 졌습니다.")
                        Indian_Poker.bankruptcy = True

                else:
                    self.my_money += self.money
                    self.op_money += self.money
                    print("무승부입니다")


                Indian_Poker.result(self)
                return self.my_money, self.op_money
                #break

            elif self.select == '2':
                self.select = 2

                print("=" * 70)
                print("당신은 Die를 선택 하셨습니다.")
                self.op_money = self.op_money + self.money + 1
                self.my_money = self.my_money - 1

                if self.my_money <= 0:
                    print("게임에서 졌습니다.")
                    Indian_Poker.bankruptcy = True

                Indian_Poker.result(self)
                return self.my_money, self.op_money, self.money
                #break

            else:
                print("다시입력하세요")


    # 게임의 결과를 출력하는 메소드
    # 결과를 보여줄때는 self.card_open 값이 True 이므로 플레이어 카드도 공개하고 다시 False로 바꿔줌
    def result(self):
        print("=" * 70)
        Indian_Poker.SHOW_OPCARD(self)
        print("결과")
        Indian_Poker.SHOW_MYCARD(self)
        self.card_open = False

    # 10번째 턴까지 모두 진행되었을때 발생하는 메소드
    def end_turn(self):
        print("=" * 70)
        print("======= 나의 코인: ", self.my_money, " ========== 결과 ========== 상대 코인: ", self.op_money, " =======")
        print("=" * 70)
        if self.my_money < self.op_money:
            print("게임에서 졌습니다.")

        elif self.op_money < self.my_money:
            print("게임에서 이겼습니다.")

        else:
            print("비겼습니다.")

    # 내 카드를 보고 컴퓨터의 표정을 출력해주는 메소드 (eazy모드)
    def eazy_mode(self):
        print("="*70)
        if self.my_card == 1:
            print("컴퓨터가 당신의 카드를 보고 크게 비웃습니다.")
        elif 4 >= self.my_card > 1:
            print("컴퓨터가 당신의 카드를 보고 살짝 웃습니다.")
        elif 6 >= self.my_card > 4:
            print("컴퓨터가 당신의 카드를 보고 고민합니다.")
        elif 8 >= self.my_card >= 7:
            print("컴퓨터가 당신의 카드를 보고 안절부절 못합니다.")
        elif 10 >= self.my_card > 8:
            print("컴퓨터가 당신의 카드를 보고 절망 합니다.")

    # 컴퓨터의 결정을 랜덤으로 하는 메소드
    def op_select(self):
        op_rand_choice = random.randint(1, 2)

        if op_rand_choice == 1:
            Indian_Poker.op_Die(self)
            Indian_Poker.result(self)

        elif op_rand_choice == 2:
            Indian_Poker.op_Call(self)
            Indian_Poker.result(self)

    # 플레이어의 차례에는 컴퓨터가 플레이어의 카드를 계산해서 배팅.
    # 컴퓨터 차례에는 랜덤으로 결정
    def hard_mode(self):
        if self.op_card > self.my_card:
            Indian_Poker.op_Call(self)
        elif self.op_card < self.my_card:
            Indian_Poker.op_Die(self)
        else:
            Indian_Poker.op_select(self)

        Indian_Poker.result(self)

    # 나의 카드 정보 출력 메소드
    def SHOW_MYCARD(self):
        if self.card_open == False:
             print("내카드 :".rjust(35))
             print("┏───┐".rjust(35))
             print("|▒▒▒|".rjust(35))
             print("└───┛".rjust(35))

        elif self.card_open == True:
            if self.my_card == 10:
                print("내카드 :".rjust(35))
                print("┏───┐".rjust(35))
                print("|1 0|".rjust(35))
                print("└───┛".rjust(35))
            else:
                print("내카드 :".rjust(35))
                print("┏───┐".rjust(35))
                print(f"| {self.my_card} |".rjust(35))
                print("└───┛".rjust(35))

    # 상대 카드 정보 출력 메소드
    def SHOW_OPCARD(self):
        if self.op_card == 10:
            print("상대카드 :".rjust(35))
            print("┏───┐".rjust(35))
            print("|1 0|".rjust(35))
            print("└───┛".rjust(35))

        else:
            print("상대카드 :".rjust(35))
            print("┏───┐".rjust(35))
            print(f"| {self.op_card} |".rjust(35))
            print("└───┛".rjust(35))
