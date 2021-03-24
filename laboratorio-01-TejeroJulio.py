import random
import numpy as np

print("Hi! Welcome to the game Meomorice")
n_pairs = int(input("With how many pairs do you want to play? "))
points_p1 = int(0)
points_p2 = int(0)
number_list = []

n = 1
while n <= n_pairs:
    number_list.append(n)
    number_list.append(n)
    n += 1

random.shuffle(number_list)

hidden_board = []
number_board = []
n = int((2*n_pairs)**(1/2))
z = 0

if (n**2) == 2*n_pairs:

    for x in range(0,n):
        hidden_board_add = []

        for i in range(0,n):
            hidden_board_add.append("*")

        hidden_board.append(hidden_board_add)

    for a in range(0,n):
        number_board_add = []

        for b in range(0,n):
            number_board_add.append(int(number_list[z]))
            z += 1

        number_board.append(number_board_add)
            
else:
    row_number = int((2*n_pairs)**(1/2)) + 1
    column_number = row_number  
    z = 0 
    
    for i in range(0,row_number):
        hidden_board_add = []

        for x in range(0, column_number):

            if z < len(number_list):
                hidden_board_add.append("*")
                z += 1

            else:
                hidden_board_add.append ("")
                z += 1
        
        hidden_board.append(hidden_board_add)

    z = 0

    for i in range(0,row_number):
        number_board_add = []

        for x in range(0, column_number):

            if z < len(number_list):
                number_board_add.append(int(number_list[z]))
                z += 1

            else:
                number_board_add.append ("")
                z += 1

        number_board.append(number_board_add)

"""
for i in tablero_numeros:
    print(*i)
"""

n = 0

while (points_p1 + points_p2) < n_pairs:
    points_p1_rec = points_p1
    points_p2_rec = points_p2
    n = 0

    while points_p1 != points_p1_rec or n == 0:
        print("")
        print("Player 1 turn!")
        print("")

        for i in hidden_board:
            print(*i)

        n = 1
        points_p1_rec = points_p1

        print("")
        
        chosen_column_j11 = (int(input ("Choose a column (from 1 to n): ")) - 1)
        chosen_row_j11 = (int(input ("Choose a row (from 1 to n): ")) - 1) 
        number_1 = number_board[chosen_row_j11][chosen_column_j11]
        print("")
        print("Card number: ", number_1)
        print("")
        hidden_board[chosen_row_j11][chosen_column_j11] = number_1
        for i in hidden_board:
            print(*i)

        print("")
        chosen_column_j12 = (int(input ("Choose a column (from 1 to n): ")) - 1)
        chosen_row_j12 = (int(input ("Choose a row (from 1 to n): ")) - 1) 
        number_2 = number_board[chosen_row_j12][chosen_column_j12]
        print("")
        print("Card number: ", number_2)
        print("")
        hidden_board[chosen_row_j12][chosen_column_j12] = number_2

        for i in hidden_board:
            print(*i)

        hidden_board[chosen_row_j11][chosen_column_j11] = "*"
        hidden_board[chosen_row_j12][chosen_column_j12] = "*"

        if number_1 == number_2:
            points_p1 += 1
            print("")
            print("You won a point")
            print("")
            print("Total points player1: ", points_p1)
            print("")
            hidden_board[chosen_row_j11][chosen_column_j11] = "-"
            hidden_board[chosen_row_j12][chosen_column_j12] = "-"

            if points_p1 + points_p2 == n_pairs:
                n = 3
                break

    while points_p2 != points_p2_rec or n == 1:
        print("")
        print("Player 2 turn!")
        print("")

        for i in hidden_board:
            print(*i)
        
        n = 2
        points_p2_rec = points_p2

        chosen_column_j21 = (int(input ("Choose a column (from 1 to n): ")) - 1)
        chosen_row_j21 = (int(input ("Choose a row (from 1 to n): ")) - 1) 
        number_1 = number_board[chosen_row_j21][chosen_column_j21]
        print("")
        print("Card number: ", number_1)
        print("")
        hidden_board[chosen_row_j21][chosen_column_j21] = number_1

        for i in hidden_board:
            print(*i)

        chosen_column_j22 = (int(input ("Choose a column (from 1 to n): ")) - 1)
        chosen_row_j22 = (int(input ("Choose a row (from 1 to n): ")) - 1) 
        number_2 = number_board[chosen_row_j22][chosen_column_j22]
        print("")
        print("Card number: ", number_2)
        print("")
        hidden_board[chosen_row_j22][chosen_column_j22] = number_2

        for i in hidden_board:
            print(*i)

        hidden_board[chosen_row_j21][chosen_column_j21] = "*"
        hidden_board[chosen_row_j22][chosen_column_j22] = "*"

        if number_1 == number_2:
            points_p2 += 1
            print("")
            print("You won a point")
            print("")
            print("Total points player 2: ", points_p2)
            print("")
            hidden_board[chosen_row_j21][chosen_column_j21] = "-"
            hidden_board[chosen_row_j22][chosen_column_j22] = "-"

            if points_p1 + points_p2 == n_pairs:
                break

if points_p1 > points_p2:
    print("Player 1 won!")

elif points_p1 < points_p2:
    print("Player 2 won!")

else:
    print("It's a tie!")

print("")