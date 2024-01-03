import random
import time
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
    Query="CREATE TABLE if not exists Jumble_Scores(Name varchar(50),Topic varchar(100),Score int)"
    Exe.execute(Query)
    Query="INSERT INTO Jumble_Scores values(%s,%s,%s)"
    val=(name,topic,points)
    Exe.execute(Query,val)
    Database.commit()

def Jumble_Scoreboard():
    print("\n1. Just add the score.\n2. Add and display the scoreboard.\n")
    ch=input("Enter your choice:")
    if ch=="1":
        SQL_conn()
        print("Your scores are added to the Score Board !!!")

    elif ch=="2":
        SQL_conn()
        Query="SELECT * FROM Jumble_Scores ORDER BY Score DESC"       
        Exe.execute(Query)
        str=Exe.fetchall()
        print("---------------SCORE BOARD----------------")
        print(tabulate(str, headers=['NAME OF THE PLAYER','TOPIC CHOSEN','POINTS SCORED'],tablefmt='psql'))

    else:
        print("Invalid option")
        Jumble_Scoreboard()

def Jumble_Instructions():
    f=open("Jumble_Instructor.txt","w")
    print()
    s="""WELCOME TO THE GAME : JUMBLED WORDS !!!\n\n
    The instructions and rules to play this game are as follows:\n
    1. The player can choose the interested topics among the given.\n
    2. Based on the topic,words will be chosen at random and will be jumbled. The player is asked to guess the word at one go.\n
    3. The player can play a topic until when he/she wish to continue and will be awarded 5 points for each correct word and will lose 2 points if the guess was wrong.\n
    4. The player is advised not to use any special characters or uppercase letters,if done so 1 point will be deducted.\n
    NOTE: The words with space inbetween is also considered neglecting the space.
    Eg: 'silver jubliee' is considered as 'silverjubliee'.
    \nHope you will enjoy the game.\nGOOD LUCK!!!\n"""
    f.write(s)
    f.close()
    f=open("Jumble_Instructor.txt","r")
    inst=f.read()
    print(inst)
    print()
    f.close()
    

def Jmain():
    global name
    global pick
    global words
    global topic
    name=input("Please Enter your name :") 
    print()
    while True:
        ch=input("Do you want to read the instructions of this game " + name +" ?? (y/n): ")
        print()
        if ch=="y":
            Jumble_Instructions()
            time.sleep(2)
            break
        elif ch=="n":
            break
        else:
            print("Invalid option entered")
            continue
    print("All the best !!!",name)
    while True:
        print("The choices available are:")
        print("1. Indian States\n2. Olympic Sports\n3. Rivers\n4. Planets\n5. Elements\n6. Colours\n7. Cartoons\n8. Super Heroes\n9. Exit")
        choice=input("Enter the topic to play with:")
        if choice=="1":
            topic="Indian States"
            words=["tamilnadu","andhrapradesh","arunachalpradesh","bihar","chhattisgarh","goa","haryana","himachalpradesh","jharkhand","karnataka","madhyapradesh","manipur","meghalaya",
                   "mizoram","nagaland","odisha","sikkim","tripura","uttarpradesh","uttarkhand","westbengal","rajasthan","gujarat","kerala","punjab","assam","maharashtra","telangana"]
        elif choice=="2":
            topic="Olympic Sports"
            words=["diving","waterpolo","mountainbiking","artistic","rhythmic","trampoline","jumping","baseball","softball","archery","athletics","boxing","fencing","handball","judo",
                   "karate","pentathlon","rowing","rugbysevens","skateboarding","sportclimbing","surfing","tabletennis","taekwondo","triathlon","weightlifting","cricket","basketball",
                   "badminton","tennis","football","swimming","volleyball","wrestling","sailing","shooting","cycling","hockey","golf"]
        elif choice=="3":
            topic="Rivers"
            words=["brahmaputra","betwa","gomti","ghaghra","son","gandak","kosi","tsangpo","siang","dibang","lohit","teesta","jamuna","padma","sutlej","chenab","jhelum","ravi","beas","shyok",
                   "zanskar","galwan","ganga","indus","yamuna","narmada","kaveri","mahanadi","krishna","godavari","chambal","hooghly"]
        elif choice=="4":
            topic="Planets"
            words=["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","pluto"]
        elif choice=="5":
            topic="Elements"
            words=["rubidium","thorium","neon","sulphur","molybdenum","wolfram","samarium","xenon","arsenic","livermorium"] 
        elif choice=="6":
            topic="Colours"
            words=["ivory","cyan","teal","maroon","lime","magenta","crimson","olive","gold","silver","blue","black","yellow","red","orange","brown","white","grey","purple",
                  "green","pink","violet","sandal"]
        elif choice=="7":
            topic="Cartoons"
            words=["mrbean","mickeymouse","minniemouse","donaldduck","daisyduck","goofy","scoobydoo","spongebob","bugsbunny","homersimpson","bartsimpson","charliebrown","grinch",
                   "popeye","daffyduck","porkypig","shaggy","pinkpanther","underdog","speedracer","winniethepooh","alvinthechipmunck","powerpuffgirls","doraemon","shinchan","tom",
                   "jerry","nobita","hattori","bheem","robin","beastboy","starfire","raven","dora"]
        elif choice=="8":
            topic="Super Heroes"
            words=["superman","batman","spiderman","ironman","hulk","thor","wonderwoman","captainamerica","captainmarvel","blackwidow","blackpanther","thanos","hawkeye","aquaman",
                   "wanda","deadpool","gamora","groot","loki","nebula","antman","ghostrider","drstrange","drax","starlord","rocketraccoon","yondu","supernova","joker","vision","flash",
                   "arrow","shazam","harleyquinn","wasp"]
        elif choice=="9":
            print("Thank you !!!. Hope you will come back")
            time.sleep(2)
            break
        else:
            print("Invalid option :(")
            continue
        play()

    
def play():
    global points
    global turns
    turns=0
    points= 0
    while True:
        pick=random.choice(words)
        random_word = random.sample(pick, len(pick))
        jumbled = ''.join(random_word)
        print()
        print("Jumbled word is : ", jumbled)
        print() 
        ans = input("Find the correct word: ")
        if (ans.isalpha() == False) or (ans.islower() == False):
            print("Invalid character entered")
            print("The word was:",pick)
            print()
            points-=1
            turns-=1
            c=input("Press 1 to continue or 0 to exit:")
            if c not in ["0","1"]:
                print("Invalid option entered")
                continue
            if c=="0":
                print("Your score is:",points)
                print("Thanks for playing")
                Jumble_Scoreboard()
                break
        elif ans == pick:  
            points += 5
            c=input("Press 1 to continue or 0 to exit:")
            if c not in ["0","1"]:
                print("Invalid option entered")
                continue
            if c=="0":
                print("Your score is:",points)
                print("Thanks for playing")
                Jumble_Scoreboard()
                break
        else:
            print("Better luck next time ..")
            print("The word was:",pick)
            print()
            points-=2
            turns-=1
            c=input("Press 1 to continue or 0 to exit:")
            if c not in ["0","1"]:
                print("Invalid option entered")
                continue
            if c=="0":
                print("Your score is:",points)
                print("Thanks for playing")
                Jumble_Scoreboard()
                break
            print()
    else:
        print("Game Over !!!")
        print(name,"your score is:",points)
        print("Thank you for playing")
        Jumble_Scoreboard()
        print()
        time.sleep(2)
