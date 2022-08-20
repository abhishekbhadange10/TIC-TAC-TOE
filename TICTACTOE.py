# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:07:18 2021

@author: Abhishek
"""

def board(a):
    print("-------")
    print("|"+a[7]+"|"+a[8]+"|"+a[9]+"|")
    print("|=|=|=|")
    print("|"+a[4]+"|"+a[5]+"|"+a[6]+"|")
    print("|=|=|=|")
    print("|"+a[1]+"|"+a[2]+"|"+a[3]+"|")
    print("-------")

    

gamelist = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
count = 0
for i in range(10):
    print('WELCOME TO TIC-TAC-TOE GAME!!')
    start = input('Are You Ready???(Y/N): ').upper()
    if start == 'Y':
        print("Let's Begin!!!")
    else:
        break
    while start =='Y':
        player1 = input('Player 1 choice(X/O): ').upper()
        if player1 == "X":
            player2 = 'O'
            print(f'Player 2 choice:{player2}')
        else:
            player2 = 'X'
            print(f'Player 2 choice:{player2}')
        
        while count<10:
            p1 = (input(f'Player 1 Enter The Position For {player1}: '))
            
            if gamelist[int(p1)] == ' ': 
                gamelist[int(p1)] = player1
                count += 1
            else:
                continue
            board(gamelist)
            
            if count==5 or count==7:
                if gamelist[1]==gamelist[2]==gamelist[3]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[4]==gamelist[5]==gamelist[6]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[7]==gamelist[8]==gamelist[9]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[1]==gamelist[4]==gamelist[7]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[2]==gamelist[5]==gamelist[8]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[3]==gamelist[6]==gamelist[9]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[1]==gamelist[5]==gamelist[9]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[3]==gamelist[5]==gamelist[7]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
            elif count==9:
                if gamelist[1]==gamelist[2]==gamelist[3]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[4]==gamelist[5]==gamelist[6]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[7]==gamelist[8]==gamelist[9]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[1]==gamelist[4]==gamelist[7]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[2]==gamelist[5]==gamelist[8]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[3]==gamelist[6]==gamelist[9]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[1]==gamelist[5]==gamelist[9]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[3]==gamelist[5]==gamelist[7]==player1:
                    print('Player 1 has won the game!!')
                    start = 'x'
                    break
                else:
                    print('The game is tied')
                    start = 'x'
                    break
                    
            
            while count<9:
                p2 = input(f'Player 2 Enter The Position For {player2}: ')
                if gamelist[int(p2)] == ' ': 
                    gamelist[int(p2)] = player2
                    count+=1
                    board(gamelist)
                    break
                
                else:
                    continue
                board(gamelist)
            

            if count==6 or count==8:
                if gamelist[1]==gamelist[2]==gamelist[3]==player2:
                    print('Player 2 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[4]==gamelist[5]==gamelist[6]==player2:
                    print('Player 2 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[7]==gamelist[8]==gamelist[9]==player2:
                    print('Player 2 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[1]==gamelist[4]==gamelist[7]==player2:
                    print('Player 2 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[2]==gamelist[5]==gamelist[8]==player2:
                    print('Player 2 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[3]==gamelist[6]==gamelist[9]==player2:
                    print('Player 2 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[1]==gamelist[5]==gamelist[9]==player2:
                    print('Player 2 has won the game!!')
                    start = 'x'
                    break
                elif gamelist[3]==gamelist[5]==gamelist[7]==player2:
                    print('Player 2 has won the game!!')
                    start = 'x'
                    break
    else:
        play_again = input('Do you want to play again??(Y/N): ').upper()
        if play_again == 'Y':
            gamelist = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            count = 0
            continue
        else:
            print('Thank you for playing!!')
            break
                
            
            
        
        
            
        