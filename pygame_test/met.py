import random

Ccard = ['♣:1', '♣:2', '♣:3', '♣:4', '♣:5', '♣:6', '♣:7', '♣:8', '♣:9', '♣:10', '♣:J', '♣:Q', '♣:K']
Hcard = ['♥:1', '♥:2', '♥:3', '♥:4', '♥:5', '♥:6', '♥:7', '♥:8', '♥:9', '♥:10', '♥:J', '♥:Q', '♥:K']
Scard = ['♠:1', '♠:2', '♠:3', '♠:4', '♠:5', '♠:6', '♠:7', '♠:8', '♠:9', '♠:10', '♠:J', '♠:Q', '♠:K']
Dcard = ['◆:1', '◆:2', '◆:3', '◆:4', '◆:5', '◆:6', '◆:7', '◆:8', '◆:9', '◆:10', '◆:J', '◆:Q', '◆:K']

Deck = ['JOKER']

computer_A = []
computer_B = []
computer_C = []
player = []

# 덱을 모두 합친뒤에 각 플레이어 에게 분배 Player 만 14장 나머지 13장
def suf():
    a = [Hcard, Dcard, Ccard, Scard]
    for i in a:
        Deck.extend(i)

    random.shuffle(Deck)

    for draw in range(13):
        computer_A.append(Deck[0])
        del Deck[0]
        computer_B.append(Deck[1])
        del Deck[1]
        computer_C.append(Deck[2])
        del Deck[2]

    player.extend(Deck)
    return player, computer_A, computer_B, computer_C

# 자동적으로 숫자가 2장으로 중복인 카드들 제거
def auto_c(deck):
    # print("뒷자리 따오기")
    end_list = []
    for i in deck:
        end_list.append(i[-1])

    # print("2배수 제거")
    del2_list = []
    for i in end_list:
        if i not in del2_list:
            del2_list.append(i)
        else:
            del2_list.remove(i)

    # print("아까 뽑앗던것으로 치환")
    card = []
    for j in del2_list:
        for i in deck:
            if j == i[-1]:
                if i[-1] not in card:
                    card.append(i)
                    break
                elif i[-1] in card:
                    continue
            else:
                continue
    return card

# 내카드중 2장 중복카드 제거 선택하는 함수
def PlayerCard():
    while True:
        try:
            print(player)
            snum = input("제거하고 싶은 카드가 있으면 1을, 제거할 카드가 없으면 0을 입력하세요\n입력: ")
            snum = int(snum)
            if snum == 1:
                pass
            elif snum == 0:
                break

        except ValueError:
            print("옳지 않은 값입니다. 다시 입력하세요.")
            continue

        try:
            print(player)
            x, y = input(f"1번째부터 {len(player)}까지 숫자가 같은 카드 2장 입력. 예시 입력 : 2 3\n입력 : ").split(" ")
            x, y = int(x), int(y)

        except ValueError:
            print("옳지 않은 값입니다. 다시 입력하세요.")
            continue

        c1 = player[x - 1]
        c2 = player[y - 1]

        if c1[-1] == c2[-1]:
            player.remove(c1)
            player.remove(c2)
            print(f"{c1} 와 {c2} 를 선택 했습니다.")

        else:
            print("숫자가 같지 않습니다.")

    return player

def PlayerChoice(com_1):
    # 상대방 카드를 뽑을때 발생하는 함수
    while True:
        print("뽑을수 있는 카드")
        print(com_1)
        for i in range(len(com_1)):
            print("┏───┐", end=" ")
        print("")
        for i in range(len(com_1)):
            print("|▒▒▒|", end=" ")
        print("")
        for i in range(len(com_1)):
            print("└───┛", end=" ")
        print("")

        try:
            anum = input(f"1번째부터 {len(com_1)}까지 원하는 카드 선택. 예시 입력 : 1\n입력 : ")
            anum = int(anum)

        except ValueError:
            print("옳지 않은 값입니다. 다시 입력하세요.")
            continue

        if anum > len(com_1) or anum < 1:
            print("옳지 않은 값입니다. 다시 입력하세요.")
            continue
        else:
            player.append(com_1[anum - 1])
            del com_1[anum - 1]
            #return player, com_1
    return player, com_1

def RandCom(com_1, com_2, com_3, player):
    # 컴퓨터 서로 자동 카드 뽑기
    randraw1 = random.randint(0, len(com_2) - 1)
    com_1.append(com_2[randraw1])
    del com_2[randraw1]

    randraw2 = random.randint(0, len(com_3) - 1)
    com_2.append(com_3[randraw2])
    del com_3[randraw2]

    randraw3 = random.randint(0, len(player) - 1)
    com_3.append(player[randraw3])
    del player[randraw3]
    return com_1, com_2, com_3, player

def Tf(com_1, com_2, com_3):
    while True:
        if len(com_1) == 0:
            print("com_1 = 0")
            break

        if len(com_2) == 0:
            print("com_2 = 0")
            break

        if len(com_3) == 0:
            print("com_3 = 0")
            break

        if len(player) == 0:
            print("player = 0")
            break

        else:
            print("안 끝남")
            break
