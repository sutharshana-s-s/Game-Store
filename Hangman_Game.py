import random
import time
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
    Query="CREATE TABLE if not exists Hang_Scores(Name varchar(50),Topic varchar(100),Score int)"
    Exe.execute(Query)
    Query="INSERT INTO Hang_Scores values(%s,%s,%s)"
    val=(name,topic,points)
    Exe.execute(Query,val)
    Database.commit()

def Hang_Scoreboard():
    print("\n1. Just add the score.\n2. Add and display the scoreboard.\n")
    ch=input("Enter your choice:")
    if ch=="1":
        SQL_conn()
        print("Your scores are added to the Score Board !!!")

    elif ch=="2":
        SQL_conn()
        Query="SELECT * FROM Hang_Scores ORDER BY Score DESC"       
        Exe.execute(Query)
        str=Exe.fetchall()
        print("---------------SCORE BOARD----------------")
        print(tabulate(str, headers=['NAME OF THE PLAYER','TOPIC CHOSEN','POINTS SCORED'],tablefmt='psql'))

    else:
        print("Invalid option")
        Hang_Scoreboard()

        
def Hang_Instructions():
    f=open("Hang_Instructor.txt","w")
    s="""WELCOME TO HANGMAN !!!\n\n
    The instructions and rules to play this game are as follows:\n
    1. The player can choose the interested topics among the given.\n
    2. Based on the topic words will be chosen at random and the player is asked to guess the word character by character.\n
    3. The player will get 5 chances for guessing and will be awarded 5 points for each correct guess and 1 point will be deducted for each wrong guess.\n
    4. If the character entered is contained in the word,the character is displayed in that place.\n
    5. As the game progresses, a segment of the gallows and of the player is added for every guessed letter not in the word.\n
    6. The player is advised not to use symbols,digits or more than one character while guessing.\n
    7. The contestant is not supposed to repeat the guesses which are already made.\n
    8. After the participant finds the complete word,he/she is awarded with 10 extra points.\n
    NOTE: The words with space in between is also considered neglecting the space.
    Eg: 'silver jubliee' is considered as 'silverjubliee'.
    \nHope you will enjoy the game.\nGOOD LUCK!!!\n"""
    f.write(s)
    f.close()
    f=open("Hang_Instructor.txt","r")
    inst=f.read()
    print(inst)
    print()
    f.close()
    
def Hmain():
    global topic
    global name
    name=input("Enter you name:")
    print()
    while True:
        ch=input("Do you want to read the instructions of this game " + name +" ?? (y/n): ")
        print()
        if ch=="y":
            Hang_Instructions()
            time.sleep(2)
            break
        elif ch=="n":
            break
        else:
            print("Invalid option entered")
            continue
    print("All the best! ", name)
    while True:
        print("Topics are:")
        print("1. Indian States\n2. Olympic Sports\n3. Rivers\n4. Planets\n5. Elements\n6. Colours\n7. Cartoons\n8. Super Heroes\n9. Exit\n")
        choice=input("Enter the topic to play with:")
        if choice=="1":
            topic="Indian States"
            words=["tamilnadu","andhrapradesh","arunachalpradesh","bihar","chhattishgarh","goa","haryana","himachalpradesh","jharkhand","karnataka","madhyapradesh","manipur","meghalaya",
                   "mizoram","nagaland","odisha","sikkim","tripura","uttarpradesh","uttarkhand","westbengal","rajasthan","gujarat","kerala","punjab","assam","maharashtra","telangana"]
            word=random.choice(words)
        elif choice=="2":
            topic="Olympic Sports"
            words=["diving","waterpolo","mountainbiking","artistic","rhythmic","trampoline","jumping","baseball","softball","archery","athletics","boxing","fencing","handball","judo",
                   "karate","pentathlon","rowing","rugbysevens","skateboarding","sportclimbing","surfing","tabletennis","taekwondo","triathlon","weightlifting","cricket","basketball",
                   "badminton","tennis","football","swimming","volleyball","wrestling","sailing","shooting","cycling","hockey","golf"]
            word=random.choice(words)
        elif choice=="3":
            topic="Rivers"
            words=["brahmaputra","betwa","gomti","ghaghra","son","gandak","kosi","tsangpo","siang","dibang","lohit","teesta","jamuna","padma","sutlej","chenab","jhelum","ravi","beas","shyok",
                   "zanskar","galwan","ganga","indus","yamuna","narmada","kaveri","mahanadi","krishna","godavari","chambal","hooghly"]
            word=random.choice(words)
        elif choice=="4":
            topic="Planets"
            words=["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","pluto"]
            word=random.choice(words)
        elif choice=="5":
            topic="Elements"
            words=["rubidium","thorium","neon","sulphur","molybdenum","wolfram","samariam","xenon","arsenic","livermorium"]
            word=random.choice(words)
        elif choice=="6":
            topic="Colours"
            words=["ivory","cyan","teal","maroon","lime","magenta","crimson","olive","gold","silver","blue","black","yellow","red","orange","brown","white","grey","purple",
                   "green","pink","violet","sandal"]
            word=random.choice(words)
        elif choice=="7":
            topic="Cartoons"
            words=["mrbean","mickeymouse","minniemouse","donaldduck","daisyduck","goofy","scoobydoo","spongebob","bugsbunny","homersimpson","bartsimpson","charliebrown","grinch",
                   "popeye","daffyduck","porkypig","shaggy","pinkpanther","underdog","speedracer","winniethepooh","alvinthechipmunck","powerpuffgirls","doraemon","shinchan","tom",
                   "jerry","nobita","hattori","bheem","robin","beastboy","starfire","raven","dora"]
            word=random.choice(words)
        elif choice=="8":
            topic="Super Heroes"
            words=["superman","batman","spiderman","ironman","hulk","thor","wonderwoman","captainamerica","captainmarvel","blackwidow","blackpanther","thanos","hawkeye","aquaman",
                   "wanda","deadpool","gamora","groot","loki","nebula","antman","ghostrider","drstrange","drax","starlord","rocketraccoon","yondu","supernova","joker","vision","flash",
                   "arrow","shazam","harleyquinn","wasp"]
            word=random.choice(words)
        elif choice=="9":
            print()
            print("Thank you !!!. Hope you will come back")
            time.sleep(2)
            break
        else:
            print("Invalid option :(")
            continue
        print("Guess the characters")
        def check():
            global points
            global guesses
            global c
            global turns
            c=5
            guesses =[]
            turns = 0
            points=0
            print("_ " * len(word))
            while c>0 :
                failed = 0
                guess = input("\nGuess a character:")
                if guess in guesses:
                    print("Already entered the guess\nTry a new guess")
                guesses.append(guess)
                if len(guess.strip())==0 or len(guess.strip()) >= 2 or guess.isdigit():
                    print("Invalid Input, Try a letter\n")
                    guesses.remove(guess)
                for char in word:
                    if char in guesses:
                        print(char,end=" ")
                    else:
                        print("_ ",end=" ")
                        failed += 1
                if guess.lower() not in word:
                    turns+=1
                    c-=1
                    print()
                    print("Wrong")
                    points-=1
                    hangman(turns)
                    print("You have",c,'more guesses')
                else:
                    if guesses.count(guess)==1:
                        points+=5
                if failed == 0:
                    points+=10
                    print()
                    print("You Win\nThe word was:",word)
                    print("You scored:",points)
                    Hang_Scoreboard()
                    print()
                    break
            if c==0:
                print("You Loose")
                print("The word was:",word)
                print("You scored:",points)
                Hang_Scoreboard()
                print()
        check()
def hangman(count):
    if count == 1:
        time.sleep(1)
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. ")
    elif count == 2:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. ")
    elif count == 3:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. ")
    elif count == 4:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. ")
    elif count == 5:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")
        print("Wrong guess. You are hanged!!!\n")

