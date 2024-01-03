import random
import time
import pickle
from tabulate import tabulate
import mysql.connector as conn


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
    Query="CREATE TABLE if not exists Word_Scores(Name varchar(50),Score int)"
    Exe.execute(Query)
    Query="INSERT INTO Word_Scores values(%s,%s)"
    val=(name,points)
    Exe.execute(Query,val)
    Database.commit()

def Word_Scoreboard():
    print("\n1. Just add the score.\n2. Add and display the scoreboard.\n")
    ch=input("Enter your choice:")
    if ch=="1":
        SQL_conn()
        print("Your scores are added to the Score Board !!!")

    elif ch=="2":
        SQL_conn()
        Query="SELECT * FROM Word_Scores ORDER BY Score DESC"       
        Exe.execute(Query)
        str=Exe.fetchall()
        print("---------------SCORE BOARD----------------")
        print(tabulate(str, headers=['NAME OF THE PLAYER','POINTS SCORED'],tablefmt='psql'))

    else:
        print("Invalid option")
        Word_Scoreboard()

        
def Word_Instructions():
    f=open("Word_Instructor.txt","w")
    s="""WELCOME TO THE GAME - WORDS IN A WORD !!!\n\n
    The instructions and rules to play this game are as follows:\n
    1. The player will be given a word.\n
    2. From the letters of the given word,the player is asked to form three valid words of minimum three letters.\n
    3. The player will be awarded 5 points for each correctly formed word.\n
    4. The player will lose 2 points for every wrongly formed words.\n
    5. The player will be awarded 10 extra points if he/she forms all 3 words correctly.\n
    6. He/She is advised not to use invalid characters like symbols,digits and letters that are not present in the given word.\n
    NOTE : The letters of the word must not be repeated more than its occurrence in the word.
    Eg : 'ALONE' --- The words formed shouldn't be 'LOON'.\n
    \nHope you will enjoy the game.\nGOOD LUCK!!!\n"""
    f.write(s)
    f.close()
    f=open("Word_Instructor.txt","r")
    inst=f.read()
    print(inst)
    print()
    f.close()


def Words():
    f=open("Words_ans.dat","wb")
    ans={"SMILE":["LIE","LIME","MILE","LIMES","MILES","SLIME","SLIM","LIES","MISE","SEMI","SIM"],
         "SMART":["ART","RAT","ARM","MART","MARS","MARTS","TRAMS","TRAM","ARMS","ARTS","MAST","MATS","MAT","RATS","RAM","SAT","STAR","TAR"],
         "HOUSE":["USE","SUE","HUE","HUES","HOSE","SHOE"],
         "PIZZAS":["ZIP","ZAP","SIP","PIZZA","ZIPS","SAP","SPA","ZAPS"],
         "HEART":["ART","HAT","HEAT","EARTH","HATE","HATER","HARE","HEAR","RATE","TEAR","ATE","EAT","EAR","ERA","TAR","TEA","RAT"],
         "WATER":["ART","RAT","TEA","RATE","TEAR","TAWER","TAR","WARE","WART","WEAR","ATE","EAT","EAR","AWE","ERA","RAW","WAR","WET"],
         "PARTY":["ART","RAY","RAT","PRAY","RAPT","TRAP","TRAY","PART","APT","PAY","RAP","TAP","TAR","TRY"],
         "ANGEL":["LEG","GEL","AGE","GLEAN","ANGLE","GALE","GANE","LANE","LANG","LEAN","ALE","LAG","NAG"],
         "WOMEN":["MEN","NEW","WON","NOW","ONE","OWE","OWN","OMEN"],
         "PIANO":["PIN","NAP","PAN","PAIN","ION"],
         "PEACE":["CAP","PEA","APE","PACE","ACE","CAPE"],
         "JESUS":["USES","USE","SUE","SUES","JESS"],
         "ADMIN":["AID","AIM","DAM","MAID","MAIN","MIND","AMIN","MAD","DIM","MAN","MID"],
         "ACCESS":["ACE","SEA","SEC","CASE","CASES","ACES","SEAS","SECS"],
         "BISHOP":["HOP","BOSH","HIP","HIPS","HOBS","HOB","SHIP","SHOP","BOP","PHI","SIP","SOB"],
         "GARDEN":["RED","EAR","END","GANDER","RANGED","DENAR","GRADE","GRAND","RAGE","RAGED","AGED","DANGER","RANGE","ANGER","AGE","DARE","AGER","DARN","DEAN","DEAR","RAG","EARN","GANE",
                   "GEAR","NEAR","RANG","READ","REND","DAG","DEN","DNA","ERA","GAD","GAN","NAG","RAN"],
         "LIGHTS":["HIT","LIGHT","LIT","SLIGHT","GILTS","GILT","HILTS","SIGHT","HILT","GIST","GST","HITS","LIST","SIGH","SILT","SLIT","SIT"],
         "OXFORD":["FOX","FORD","ROD","DOOR","FOOD","ROOF","ROOD","OXO"],
         "SUMMER":["SUM","SUE","USE","SERUM","USER","MUSER","MURE","MUSE","SURE","EMU","MURES","RUM"],
         "WINNER":["WIN","NEW","NINE","WINE","REIN","RIN","WIRE","INN","REWIN","INNER"],
         "SPIRIT":["SPIT","TIP","SIT","STRIP","TRIPS","TRIP","IRIS","PIT","SPIRT","PITS","RIPS","RIP","STIR","TIPS","SPRIT","SIP","SIR"]}
    pickle.dump(ans,f)
    f.close()
         
    
def Wmain():
    global name
    global points
    global curr_count
    points=0
    c="1"
    name=input("Enter you name:")
    print()
    print("Let's play the game of forming words out of word !!!")
    print()
    time.sleep(1)
    while True:
        ch=input("Do you want to read the instructions of this game " + name +" ?? (y/n): ")
        print()
        if ch=="y":
            Word_Instructions()
            time.sleep(2)
            break
        elif ch=="n":
            break
        else:
            print("Invalid option entered")
            continue
    print("All the best! ", name)
    while c=="1":
        curr_count=0
        words=["SMILE","SMART","HOUSE","PIZZAS","HEART","WATER","PARTY","ANGEL","WOMEN","PIANO","PEACE","JESUS","ADMIN","ACCESS","BISHOP","GARDEN","LIGHTS","OXFORD","SUMMER","WINNER","SPIRIT"]
        word=random.choice(words)
        print("The word is:",word)
        for i in range(3):
            w=(input("Form the word "+str(i+1)+" : ").strip()).upper()
            if w.isalpha()!=True:
                print("Invalid character entered")
            else:
                Words()
                f=open("Words_ans.dat","rb")
                ans={}
                while True:
                    try:
                        ans=pickle.load(f)
                    except EOFError:
                        break
                f.close()
                if w in ans[word]:
                    print("Your answer is correct")
                    points+=5
                    curr_count+=1
                else:
                    print("Your answer is wrong")
                    points-=2
        print("The words that can be formed out of:",word,"are:",ans[word][0],",",ans[word][1],",",ans[word][2],".")
        if curr_count==3:
            points+=10
        c=input("Press 1 to continue or 0 to quit:")
        print()
        if c=="0":
            print("Your score is:",points)
            Word_Scoreboard()
            print("Thank you for playing !!! Hope you will come back !!!")
            time.sleep(2)
            break
        elif c not in ["0","1"]:
            print("Invalid option entered")
            c="1"
