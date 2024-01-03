import time
import random
import pickle
import mysql.connector as conn
from tabulate import tabulate


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
    Query="CREATE TABLE if not exists Madlibs_Scores(Name varchar(50),Topic varchar(100),Story varchar(100),Score int)"
    Exe.execute(Query)
    Query="INSERT INTO Madlibs_Scores values(%s,%s,%s,%s)"
    val=(name,choice,topic,points)
    Exe.execute(Query,val)
    Database.commit()

def Madlibs_Scoreboard():
    print("\n1. Just add the score.\n2. Add and display the scoreboard.\n")
    ch=input("Enter your choice:")
    if ch=="1":
        SQL_conn()
        print("Your scores are added to the Score Board !!!")

    elif ch=="2":
        SQL_conn()
        Query="SELECT * FROM Madlibs_Scores ORDER BY Score DESC"       
        Exe.execute(Query)
        str=Exe.fetchall()
        print("---------------SCORE BOARD----------------")
        print(tabulate(str, headers=['NAME OF THE PLAYER','TOPIC CHOSEN','STORY NAME','POINTS SCORED'],tablefmt='psql'))

    else:
        print("Invalid option")
        Madlibs_Scoreboard()

    
def Madlibs_Instructions():
    f=open("Madlibs_Instructor.txt","w")
    s="""WELCOME TO MAD LIBS !!!\n\n
    The instructions and rules to play this game are as follows:\n
    1. The player can choose the interested subgame among the given.\n
    2. The player will get an incomplete story / Collective Noun / Proverb.\n
    3. He/she is supposed to guess the words based on the clues given inside the brackets for stories.\n
    4. The player will be given one chance to guess each answer.\n
    5. For every correct guess the player will be awarded 5 points and will lose 2 points for every wrong guess.\n
    6. If the player finds all the words correctly in the stories,he/she will be awarded 10 extra points .\n
    NOTE: The player is asked to enter the words succeeding full stops with first letter in uppercase.\n
          For the clues given as numbers in stories,the player is asked to enter the number in full form. Eg: '7' to be entered as 'seven'.\n
          The player is not supposed to enter invalid characters like symbols,digits.\n
    \nHope you will enjoy the game.\nGOOD LUCK!!!\n"""
    f.write(s)
    f.close()
    f=open("Madlibs_Instructor.txt","r")
    inst=f.read()
    print(inst)
    print()
    f.close()


def Story_Score():
    global points
    if turns==0:
        points+=10
        print()
        print("You completed the story successfully")
        print("Your score is:",points)
        Madlibs_Scoreboard()
    else:
        print()
        print("You missed",turns,"words")
        print("Your score is:",points)
        Madlibs_Scoreboard()
    

def Story():
    global topic
    global points
    global turns
    turns=0
    print("The stories to play with are:\n")
    print("""1. Sleeping Beauty.\n2. The Golden Egg.\n3. Max's Encounter with the Aliens.\n4. The Lion and the Mouse.\n5. Boy who Cried Wolf\n6. The Bear and the Two Friends.
7. Count Wisely.\n8. Exit.\n""")
    ch=input("Enter your choice:")
    if ch=="1":
        points=0
        topic="Sleeping Beauty"
        import Sleeping_Beauty
        f=open("Sleeping_Beauty.txt","r")
        s=f.read()
        print(s)
        f.close()
        f=open("Sleeping_Beauty_ans.dat","rb")
        ans={}
        while True:
            try:
                ans=pickle.load(f)
            except EOFError:
                break
        f.close()
        print()
        for i in range(1,16):
            answer=input("Guess the word "+str(i)+":")
            if (answer.strip()).isalpha()!=True:
                print("\nInvaild answer entered\n")
                turns+=1
                continue
            if answer==ans[i]:
                points+=5
            else:
                points-=2
                turns+=1
        time.sleep(2)
        f=open("Sleeping_Beauty_final.txt","r")
        s=f.read()
        print()
        print("The correct story is:\n\n")
        print(s)
        Story_Score()
    elif ch=="2":
        points=0
        topic="The Golden Egg"
        import Golden_Egg
        f=open("Golden_Egg.txt","r")
        s=f.read()
        print(s)
        f.close()
        f=open("Golden_Egg_ans.dat","rb")
        ans={}
        while True:
            try:
                ans=pickle.load(f)
            except EOFError:
                break
        f.close()
        print()
        for i in range(1,16):
            answer=input("Guess the word "+str(i)+":")
            if (answer.strip()).isalpha()!=True:
                print("\nInvaild answer entered\n")
                turns+=1
                continue
            if answer==ans[i]:
                points+=5
            else:
                points-=2
                turns+=1
        time.sleep(2)
        f=open("Golden_Egg_final.txt","r")
        s=f.read()
        print()
        print("The correct story is:\n\n")
        print(s)
        Story_Score()
    elif ch=="3":
        points=0
        topic="Max's Encounter with the Aliens"
        import Max_Aliens
        f=open("Max_Aliens.txt","r")
        s=f.read()
        print(s)
        f.close()
        f=open("Max_Aliens_ans.dat","rb")
        ans={}
        while True:
            try:
                ans=pickle.load(f)
            except EOFError:
                break
        f.close()
        print()
        for i in range(1,16):
            answer=input("Guess the word "+str(i)+":")
            if (answer.strip()).isalpha()!=True:
                print("Invaild answer entered")
                turns+=1
                continue
            if answer==ans[i]:
                points+=5
            else:
                points-=2
                turns+=1
        time.sleep(2)
        f=open("Max_Aliens_final.txt","r")
        s=f.read()
        print()
        print("The correct story is:\n\n")
        print(s)
        Story_Score()
    elif ch=="4":
        points=0
        topic="The Lion and The Mouse"
        import The_Lion_Mouse
        f=open("The_Lion_Mouse.txt","r")
        s=f.read()
        print(s)
        f.close()
        f=open("The_Lion_Mouse_ans.dat","rb")
        ans={}
        while True:
            try:
                ans=pickle.load(f)
            except EOFError:
                break
        f.close()
        print()
        for i in range(1,16):
            answer=input("Guess the word "+str(i)+":")
            if (answer.strip()).isalpha()!=True:
                print("\nInvaild answer entered\n")
                turns+=1
                continue
            if answer==ans[i]:
                points+=5
            else:
                points-=2
                turns+=1
        time.sleep(2)
        f=open("The_Lion_Mouse_final.txt","r")
        s=f.read()
        print()
        print("The correct story is:\n\n")
        print(s)
        Story_Score()
    elif ch=="5":
        points=0
        topic="Boy who Cried Wolf"
        import Boy_Wolf
        f=open("Boy_Wolf.txt","r")
        s=f.read()
        print(s)
        f.close()
        f=open("Boy_Wolf_ans.dat","rb")
        ans={}
        while True:
            try:
                ans=pickle.load(f)
            except EOFError:
                break
        f.close()
        print()
        for i in range(1,16):
            answer=input("Guess the word "+str(i)+":")
            if (answer.strip()).isalpha()!=True:
                print("\nInvaild answer entered\n")
                turns+=1
                continue
            if answer==ans[i]:
                points+=5
            else:
                points-=2
                turns+=1
        time.sleep(2)
        f=open("Boy_Wolf_final.txt","r")
        s=f.read()
        print()
        print("The correct story is:\n\n")
        print(s)
        Story_Score()
    elif ch=="6":
        points=0
        topic="The Bear and the Two Friends"
        import Bear_Friends
        f=open("Bear_Friends.txt","r")
        s=f.read()
        print(s)
        f.close()
        f=open("Bear_Friends_ans.dat","rb")
        ans={}
        while True:
            try:
                ans=pickle.load(f)
            except EOFError:
                break
        f.close()
        print()
        for i in range(1,16):
            answer=input("Guess the word "+str(i)+":")
            if (answer.strip()).isalpha()!=True:
                print("\nInvaild answer entered\n")
                turns+=1
                continue
            if answer==ans[i]:
                points+=5
            else:
                points-=2
                turns+=1
        time.sleep(2)
        f=open("Bear_Friends_final.txt","r")
        s=f.read()
        print()
        print("The correct story is:\n\n")
        print(s)
        Story_Score()
    elif ch=="7":
        points=0
        topic="Count Wisely"
        import Count_Wisely
        f=open("Count_Wisely.txt","r")
        s=f.read()
        print(s)
        f.close()
        f=open("Count_Wisely_ans.dat","rb")
        ans={}
        while True:
            try:
                ans=pickle.load(f)
            except EOFError:
                break
        f.close()
        print()
        for i in range(1,16):
            answer=input("Guess the word "+str(i)+":")
            if (answer.strip()).isalpha()!=True:
                print("\nInvaild answer entered\n")
                turns+=1
                continue
            if answer==ans[i]:
                points+=5
            else:
                points-=2
                turns+=1
        time.sleep(2)
        f=open("Count_Wisely_final.txt","r")
        s=f.read()
        print()
        print("The correct story is:\n\n")
        print(s)
        Story_Score()      
    elif ch=="8":
        print()
        print("Thank you for playing !!! Hope you will come back!!!")
    else:
        print("Invalid option :(")
        Story()


def Coll_Nouns():
    import Collective_Nouns
    global points
    points=0
    c="1"
    f=open("Collective_Nouns_ans.dat","rb")
    ans={}
    while True:
        try:
            ans=pickle.load(f)
        except EOFError:
            break
    while c=="1":
        f=open("Collective_Nouns.txt","r")
        L=f.readlines()
        s=random.choice(L)
        pos=L.index(s)
        print(s)
        f.close()
        f=open("Collective_Nouns_final.txt","r")
        N=f.readlines()
        sentence=N[pos]
        answer=input("Enter the collective noun:")
        if (answer.strip()).isalpha()!=True:
                print("\nInvaild answer entered\n")
                print("The correct answer was:")
                print(sentence)
                continue
        if answer==ans[pos]:
            points+=5
            print("You got it right\n")
            print("The correct answer was:")
            print(sentence)
            c=input("Press 1 to continue or 0 to exit:")
            if c not in ["0","1"]:
                print("Invalid option entered")
                c="1"
                continue
        else:
            points-=2
            print("Your answer is wrong\n")
            print("The correct answer was:")
            print(sentence)
            c=input("Press 1 to continue or 0 to exit:")
            if c not in ["0","1"]:
                print("Invalid option entered")
                c="1"
                continue
    else:
        print("Your score is:",points)
        Madlibs_Scoreboard()
    
def Proverbs():
    import Proverb_Filling
    global points
    points=0
    c="1"
    f=open("Proverbs_ans.dat","rb")
    ans={}
    while True:
        try:
            ans=pickle.load(f)
        except EOFError:
            break
    while c=="1":
        f=open("Proverbs.txt","r")
        L=f.readlines()
        s=random.choice(L)
        pos=L.index(s)
        print(s)
        f.close()
        f=open("Proverbs_final.txt","r")
        N=f.readlines()
        sentence=N[pos]
        answer=input("Enter the misssing word in the proverb:")
        if (answer.strip()).isalpha()!=True:
                print("\nInvaild answer entered\n")
                print("The correct answer was:")
                print(sentence)
                continue
        if answer==ans[pos]:
            points+=5
            print("You got it right")
            print("The correct proverb was:")
            print(sentence)
            c=input("Press 1 to continue or 0 to exit:")
            if c not in ["0","1"]:
                print("Invalid option entered")
                c="1"
                continue
        else:
            points-=2
            print("Your answer is wrong")
            print("The correct proverb was:\n")
            print(sentence)
            c=input("Press 1 to continue or 0 to exit:")
            if c not in ["0","1"]:
                print("Invalid option entered")
                c="1"
                continue
    else:
        print("Your score is:",points)
        Madlibs_Scoreboard()
    
def Mmain():
    global choice
    global topic
    con=True
    while con:
        time.sleep(2)
        print("The subgames available are:\n")
        print("1. Mad Libs for Stories.\n2. Mad Libs for Collective Nouns.\n3. Mad Libs for Proverbs.\n4. Exit\n")
        op=input("Enter your choice:")
        if op=="1":
            topic="NULL"
            choice="Stories"
            Story()
        elif op=="2":
            topic="NULL"
            choice="Collective Nouns"
            Coll_Nouns()
        elif op=="3":
            topic="NULL"
            choice="Proverbs"
            Proverbs()
        elif op=="4":
            print()
            print("Thank you for playing !!! Hope you will come back!!!")
            con=False
            time.sleep(2)
        else:
            print("Invalid choice entered :(")
            continue


def ML_Main():
    global name
    name = input("What is your name? ")
    print()
    while True:
        ch=input("Do you want to read the instructions of this game " + name +" ?? (y/n): ")
        print()
        if ch=="y":
            Madlibs_Instructions()
            time.sleep(2)
            break
        elif ch=="n":
            break
        else:
            print("Invalid option entered")
            continue
        print("All the best! ", name)
    Mmain()
