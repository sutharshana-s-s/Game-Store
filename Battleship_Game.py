import time
from random import randint
import mysql.connector as conn
from tabulate import tabulate


def Battle_Instructions():
    f=open("Battle_Instructor.txt","w")
    s="""WELCOME TO BATTLE SHIP !!!\n\n
    The instructions and rules to play this game are as follows:\n
    1. The player is supposed to guess the location of the ship located by the computer and destroy it.\n
    2. The player will be given an initial score of 10 points.\n
    3. If the guess of location is correct,then the player will be awarded 10 points.\n
    4. If the guess of the location is wrong and is within the battleship area,then the player will loose 1 point.\n
    5. If the guess of the location is wrong and is not within the battleship area,then the player will loose 2 points.\n
    6. The guesses are supposed to be entered as digits,else it would be considered invalid and the player will lose 1 point.\n
    \nHope you will enjoy the game.\nGOOD LUCK!!!\n"""
    f.write(s)
    f.close()
    f=open("Battle_Instructor.txt","r")
    inst=f.read()
    print(inst)
    print()
    f.close()

def Replay():
    global choice
    choice=input("Do you want to play again ??? (y/n):")
    if choice=="y":
        Bmain()
    elif choice=="n":
        print("Thank you for playing the game !!!")
        time.sleep(2)
    else:
        print("Invalid choice entered")
        Replay()

def SQL_conn():
    global Database
    global Exe
    global Query
    Database=conn.connect(host="localhost",user="root",password="s12345")
    Exe=Database.cursor()
    Query="CREATE DATABASE if not exists Score_Board"
    Exe.execute(Query)
    Query="USE Score_Board"
    Exe.execute(Query)
    Query="CREATE TABLE if not exists Battle_Scores(Name varchar(50),Score int)"
    Exe.execute(Query)
    Query="INSERT INTO Battle_Scores values(%s,%s)"
    val=(name,points)
    Exe.execute(Query,val)
    Database.commit()

def Battle_Scoreboard():
    print("\n1. Just add the score.\n2. Add and display the scoreboard.\n")
    ch=input("Enter your choice:")
    if ch=="1":
        SQL_conn()
        print("Your scores are added to the Score Board !!!")

    elif ch=="2":
        SQL_conn()
        Query="SELECT * FROM Battle_Scores ORDER BY Score DESC"       
        Exe.execute(Query)
        str=Exe.fetchall()
        print("---------------SCORE BOARD----------------")
        print(tabulate(str, headers=['NAME OF THE PLAYER','POINTS SCORED'],tablefmt='psql'))

    else:
        print("Invalid option")
        Battle_Scoreboard()

def Correct_ans():
    print()
    correct_board = []
    for x in range(6):
        correct_board.append(["O"] * 6)
    correct_board[ship_row-1][ship_col-1]="$"
    
    for row in correct_board:
        print((" ").join(row))

def display(board):
    for row in board:
        print((" ").join(row))
        
def Bmain():
    global ship_row
    global ship_col
    global choice
    global points
    board=[]
    points=10
    turns=0
    print("All the best!", name)
    for x in range(6):
        board.append(["O"] * 6)
    print("Let's play the Battleship Game !!!\n")
    time.sleep(1)
    display(board)
    ship_row=randint(1,len(board))
    ship_col=randint(1,len(board[0]))
    while turns<5:
        turns+= 1
        print("The turn number is:",turns)
        g_row = input("Guess the Row of the ship:")
        g_col = input("Guess the Column of the ship:")
        if g_row.isdigit() and g_col.isdigit():
            guess_row = int(g_row)-1
            guess_col = int(g_col)-1
        else:
            print()
            print("Invalid row or column entered")
            points-=1
            continue
            
        if int(g_row) == ship_row and int(g_col) == ship_col:
            print()
            print("Congratulations!\nYou sunk my battleship!")
            points+=10
            print("The position of the battleship was:")
            print("Row:",ship_row,"Column:",ship_col)
            time.sleep(1)
            Correct_ans()
            print()
            time.sleep(1)
            print("Your score is:",points)
            time.sleep(1)
            Battle_Scoreboard()
            print()
            Replay()
            break
        else:
            if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
                time.sleep(1)
                print()
                print("Oops, that's not even in the ocean.")
                points-=2
            elif(board[guess_row][guess_col] == "X"):
                time.sleep(1)
                print()
                print("You guessed it already.")
            else:
                time.sleep(1)
                print()
                print("You missed my battleship :( ")
                points-=1
                board[guess_row][guess_col] = "X"
        display(board)
        
    else:
        print("Game Over !!! \n")
        print()
        time.sleep(1)
        print("The position of the battleship was:")
        if turns==5:
            print("Row:",ship_row,"Column:",ship_col)
            Correct_ans()
            print()
            print("Your score is:",points)
            time.sleep(1)
            Battle_Scoreboard()
            print()
            Replay()

def BS_Main():
    global name
    global choice
    choice="y"
    name=input("Enter your name:")
    print()
    while True:
        ch=input("Do you want to read the instructions of this game " + name +" ?? (y/n): ")
        print()
        if ch=="y":
            Battle_Instructions()
            time.sleep(2)
            break
        elif ch=="n":
            break
        else:
            print("Invalid option entered")
            continue
    Bmain()
