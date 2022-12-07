import random
import os
import time
os.system("cls")
deck=['A♣','A♠','A♥','A♦','2♣','2♠','2♥','2♦','3♣','3♠','3♥','3♦','4♣','4♠','4♥','4♦','5♣','5♠','5♥','5♦','6♣','6♠','6♥','6♦','7♣','7♠','7♥','7♦','8♣','8♠','8♥','8♦','9♣','9♠','9♥','9♦','10♣','10♠','10♥','10♦','J♣','J♠','J♥','J♦','Q♣','Q♠','Q♥','Q♦','K♣','K♠','K♥','K♦']


finish = False
#---------------------------------------
def game():
    if difficulté==1:
        bank = 1000
    elif difficulté==2:
        bank = 500
    elif difficulté==3:
        bank = 250
    elif difficulté==4:
        bank = 100
    print("Bienvenue cher joueur de poker ! ")
    print("vous avez {} jetons".format(bank))
    while bank>0:
        random.shuffle(deck)
        hand=deck[1]+deck[2]
        board_1 = deck[3]+deck[4]+deck[5]
        board_2 = deck[3]+deck[4]+deck[5]+deck[6]
        board_3 = deck[3]+deck[4]+deck[5]+deck[6]+deck[7]
        adversaire_1 = deck[8]+deck[9]
        while finish != True:
            if bank <20:
                choix_1=5
            else:
                choix_1 = ask_questions("voici votre main {} que souhaitez vous faire ? ".format(hand),"fold","raise {} jetons".format(round(bank/20,0)),"raise {} jetons".format(round(bank/5,0)),"raise {} jetons".format(round(bank/5,0)),"all-in {}".format(bank))   
            
            pot = round(bank,2)
            os.system("cls")
            if choix_1 == 1:
                print("vous vous etes coucher avec {} \n voici le board complet {} \n voici la main de votre adversaire {}".format(hand,board_3,adversaire_1))
            elif choix_1 == 2:   
                print("vous avez parier {}".format(round(bank/20,0)))
                bank = bank-round(bank/20,0)
                print("\n carte du board : {} \n vos cartes : {}".format(board_1,hand))
            elif choix_1 == 3:
                print("vous avez parier {}".format(round(bank/10,0)))
                bank = bank-round(bank/10,0)
                print("\n carte du board : {} \n vos cartes : {}".format(board_1,hand))
            elif choix_1 == 4:
                print("vous avez parier {}".format(round(bank/5,0)))
                bank = bank-round(bank/5,0)
                print("\n carte du board : {} \n vos cartes : {}".format(board_1,hand))
            elif choix_1 == 5:
                print("ALL IN BABY !!!")
                print("vous avez parier {}".format(round(bank,0)))
                bank = 0
            #--------- suite ----------
            
            os.system("cls")
            if (choix_1==2 or choix_1==3 or choix_1==4):
                print("voici le board {} : ".format(board_1))
                choix_2 = ask_questions("voici votre main {} que souhaitez vous faire ? ".format(hand),"fold","raise {} jetons".format(round(bank/20,0)),"raise {} jetons".format(round(bank/5,0)),"raise {} jetons".format(round(bank/5,0)),"all-in {} jetons".format(bank))   
            os.system("cls")
            if choix_2 == 1:
                print("vous vous etes coucher avec {} \n voici le board complet {} \n voici la main de votre adversaire {}".format(hand,board_3,adversaire_1))
            elif choix_2 == 2:   
                print("vous avez parier {}".format(round(bank/20,0)))
                bank = bank-round(bank/20,0)
                print("\n carte du board : {} \n vos cartes : {}".format(board_1,hand))
            elif choix_2 == 3:
                print("vous avez parier {}".format(round(bank/10,0)))
                bank = bank-round(bank/10,0)
                print("\n carte du board : {} \n vos cartes : {}".format(board_1,hand))
            elif choix_2 == 4:
                print("vous avez parier {}".format(round(bank/5,0)))
                bank = bank-round(bank/5,0)
                print("\n carte du board : {} \n vos cartes : {}".format(board_1,hand))
            elif choix_2 == 5:
                print("ALL IN BABY !!!")
                print("vous avez parier {}".format(round(bank,0)))
            continue




#réponse au question
def ask_questions(questions, *choices):
    c = 1
    print(questions)

    for q in choices:
        print(f'({c}) ' + str(q))
        c += 1

    answer = int(input("veuillez choisir une des réponse : "))
    if answer > 0 and answer <= len(choices):
        return answer
    else:
        os.system("cls")
        print("veuillez réessayer...")
        ask_questions(questions, *choices)
#lancement de la game
game_1 = ask_questions("voulez vous jouez ? ","oui","non")
os.system("cls")
#veut t'il jouer ?
if (game_1==1):
    #si oui alors =>
    difficulté = ask_questions("Quelle difficulté ? ","facile","intermédiaire","difficile","hardcore")
    os.system("cls")
    game()
else:
    #si non seconde question
    game_2 = ask_questions("c'est embarassant... non ? ","oui","non")
    if (game_2==1):
        print("ok alors si c'est embarassant allons y !!")
        time.sleep(2)
        os.system("cls")
    else:
        print("bon...")
        time.sleep(2)
        print(" allez finit de rire c'est partie !! ")
        time.sleep(2)
        os.system("cls")
        #renvoie difficulté
    difficulté = ask_questions("Quelle difficulté ? ","facile","intermédiaire","difficile","hardcore")
    os.system("cls")
    game()