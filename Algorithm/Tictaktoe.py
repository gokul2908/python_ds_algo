def solved(A):
    A1 = ["","","","","","","",""]
    for i in range(3):
        A1[0] += A[i] 
        A1[1] += A[i+3] 
        A1[2] += A[i+6]
    for i in [0,3,6]:
        A1[3] += A[i]
        A1[4] += A[i+1]
        A1[5] += A[i+2]
    A1[6] = A[0]+A[4]+A[8]
    A1[7] = A[2]+A[4]+A[6]

    for i in A1:
        if i == "XXX" or i =="OOO":
            return False
    return True

def player_input(playerx):
    who = playerx[-1]
    player = int(input(f'Player {who}: '))
    if player < 10:
        if A[player-1] != "X" and A[player-1] != "O":
            if who == "1": 
                A[player-1] = "X"
            else: 
                A[player-1] = "O"
        else:
            print("already exist at the place")
            player_input(playerx)
    else:
        print("invalid input")
        player_input(playerx)

    print(f'{A[0]} |{A[1]} |{A[2]} ')
    print( "________")
    print(f'{A[3]} |{A[4]} |{A[5]} ')
    print( "________")
    print(f'{A[6]} |{A[7]} |{A[8]} ')
    con = solved(A)
    if con == False:
        print('Player 1 won')
    return con
        
A = [" "," "," "," "," "," "," "," "," "]

while True:
    print("Enter a value range of 1 to 9")
    con = player_input("Player_1")
    if con == False:
        break
    con = player_input("Player_2")
    if con == False:
        break
