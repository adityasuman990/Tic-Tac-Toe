# Date : 19th jan tic tac toe without any extra module
import random
import numpy as np

arr = np.zeros((3, 3))

def ran():
    return random.randint(0, 2)

def a(arr, t):
    row = ran()
    col = ran()

    if arr[row, col] in [1, 2]:
        # If the cell already contains 1 or 2, call a again
        a(arr, t)
    else:
        arr[row, col] = t
        return arr

def check(arr):
    for i in range(3):
        if arr[i, 0] == arr[i, 1] == arr[i, 2] == 1 or arr[i, 0] == arr[i, 1] == arr[i, 2] == 2:
            return True

    for i in range(3):
        if arr[0, i] == arr[1, i] == arr[2, i] == 1 or arr[0, i] == arr[1, i] == arr[2, i] == 2:
            return True

    if arr[0, 0] == arr[1, 1] == arr[2, 2] == 1 or arr[0, 0] == arr[1, 1] == arr[2, 2] == 2:
        return True
    if arr[0, 2] == arr[1, 1] == arr[2, 0] == 1 or arr[0, 2] == arr[1, 1] == arr[2, 0] == 2:
        return True
    
    for i in range(3):
        for j in range(3):
            if arr[i, j] == 0:
                return False  #  empty cell, game is not  tie
    
    return True  #  no empty cells game is a tie

print("Welcome to Tic-tac-toe:")
# print("Rules: There are two players automatically playing the game, you and bet upon player of your choice")
# x1 = int(input("Enter 1 or 2 to try your luck:"))

def turn(play, x):
    player = (play % 2) + 1
    play = play + 1
    print(f"Now it's the turn of player {player}")
    a(arr, player)
    print(arr)
    val = check(arr)
    
    if val:
        if not any(arr.flatten()):
            print("It's a tie!")
        else:
            print(f"Player {player} wins!")
        return

    turn(play, x + 1)

turn(1, 0)

