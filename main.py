"""
Made By:- Kamal Kumar Jena
Date:- 25 August,2020
Made For:- As a Practice problem(CodeWithHarry)
"""

import random
try:
    a = int(input("ENTER THE STARTING NUMBER OF RANGE\n"))
    b = int(input("ENTER THE LAST NUMBER OF RANGE\n"))
    c = random.randint(a, b)
    j1 = input("ENTER THE PLAYER 1 NAME\n")
    j2 = input("ENTER THE PLAYER 2 NAME\n")
    moves = 0
    print(f"TURN OF PLAYER 1 ({j1})")
    while True:
        k1 = int(input("ENTER THE NUMBER\n"))
        moves = moves + 1
        if k1 != c:
            if k1 > c:
                print("WRONG NUMBER\nENTER A SMALLER NUMBER\n")
            if k1 < c:
                print("WRONG NUMBER\nENTER A BIGGER NUMBER\n")
        if k1 == c:
            break
        else:
            continue
    print("CONGRATS YOU FOUND THE NUMBER!!!")
    print(f"IT'S TURN OF PLAYER 2 ({j2})")
    d = random.randint(a, b)
    moves1 = 0
    while True:
        k2 = int(input("ENTER THE NUMBER\n"))
        moves1 = moves1 + 1
        if k2 != d:
            if k2 > d:
                print("WRONG NUMBER\nENTER A SMALLER NUMBER\n")
            if k2 < d:
                print("WRONG NUMBER\nENTER A BIGGER NUMBER\n")
        if k2 == d:
            break
        else:
            continue
    print(f"MOVES TAKEN BY {j1} {moves}")
    print(f"MOVES TAKEN BY {j2} {moves1}")
    print(f"NUMBER OF PLAYER 1 WAS {c}")
    print(f"NUMBER OF PLAYER 2 WAS {d}")
    print(d)
    if moves == moves1:
        print("YOU BOTH HAD A DRAW")
    elif moves > moves1:
        print(f"{j2} WON!!!!!!!!!!!!!!!")
        print(f"{j1} YOU CAN TAKE {j2} TO A MOVIE AS A LOSING PUNISHMENT")
    elif moves < moves1:
        print(f"{j1} WON!!!!!!!!!!!!!!!")
        print(f"{j2} YOU CAN TAKE {j1} TO A MOVIE AS A LOSING PUNISHMENT")
except ValueError:
    while True:
        print("ENTER AN INTEGER ONLY\n")
        break
