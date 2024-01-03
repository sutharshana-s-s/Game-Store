import sys
import time

def GAME_MAIN():
    print()
    time.sleep(3)
    print("*************************** WELCOME TO SASS GAMESTORE !!! *********************************")
    print()
    time.sleep(1)
    print(""".....THERE ARE RULES TO LUCK , NOT EVERYTHING IS CHANCE TO BE WISE ; LUCK CAN BE HELPED BY SKILL.....
1. Each game in this game store will input the player's name and their scores will be recorded separately.\n
2. The player is asked to follow the instructions given for each game.\n
\nHOPE YOU WILL ENJOY THE GAME.\nGOOD LUCK!!!\n""")
    while True:
        print("\nTHE GAMES TO PLAY WITH ARE:\n")
        print("1. HANGMAN\n2. JUMBLED WORDS\n3. MAD LIBS GAMES\n4. BATTLESHIP\n5. WORDS IN A WORD\n6. EXIT THE GAME\n")
        option=input("Enter the game you wish to play: ")
        if option=="1":
            import Hangman_Game
            Hangman_Game.Hmain()
        elif option=="2":
            import Jumbled_Words_Game
            Jumbled_Words_Game.Jmain()
        elif option=="3":
            import Mad_Libs_Game
            Mad_Libs_Game.ML_Main()
        elif option=="4":
            import Battleship_Game
            Battleship_Game.BS_Main()
        elif option=="5":
            import Word_Game
            Word_Game.Wmain()
        elif option=="6":
            print()
            print("..............................IN LIFE AND IN GAME , A GOOD PLAYER IS ALWAYS LUCKY..........................")
            time.sleep(2)
            print()
            print("***************************THANK YOU FOR PLAYING OUR GAMES !!! HOPE YOU ENJOYED IT*************************")
            print()
            time.sleep(20)
            sys.exit()
        else:
            print("\nInvalid option entered :(\n")
            continue

GAME_MAIN()
