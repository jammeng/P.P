from met import *
import random

suf = suf()
print("초기값")
print(computer_A)
print(computer_B)
print(computer_C)
print(player)
print("------------------------------------------")


while True:
    print("player 버릴 카드 선택 및 컴퓨터 중복 카드 자동 제거")
    com_1 = auto_c(computer_A)
    com_2 = auto_c(computer_B)
    com_3 = auto_c(computer_C)
    #player = auto_c(player)

    PlayerCard()
    print(com_1)
    print(com_2)
    print(com_3)
    print(player)



    # sorted(player, key=player[-1])
    print("-------------------------------------------")


    print("player가 뽑을 카드 선택 및 컴퓨터간 자동 카드 뽑기")
    print(com_1)
    print(com_2)
    print(com_3)
    print(player)
    print("------------------------------------------")

    PlayerChoice(com_1)

    #RandCom(com_1, com_2, com_3, player)

    print(com_1)
    print(com_2)
    print(com_3)
    print(player)




