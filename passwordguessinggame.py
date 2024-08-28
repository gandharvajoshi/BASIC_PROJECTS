#PASSWORD GUESSING GAME 

import random
def correctelement(guess,password):#checks how many correct digits are there
    global correctelements
    correctelements=0
    duplicatecount=len(guess)-len(set(guess))#check how much times elements are repeated 
    for number in guess:
        if number in password:
            correctelements=correctelements+1
    return correctelements-duplicatecount

def correctposition(guess,password):#checks how many correct digits are present in the right position
    global correctpositions
    correctpositions=0

    for i in range(0,len(guess)):
        if guess[i]==password[i]:
            correctpositions=correctpositions+1      
    return correctpositions

game_on=True
def checkwin(guess,password):#checks if game is still on
    global game_on
    if(guess==password):
        print("CONGATULATIONS YOU WON THE GAME :")
        print(f"THE CORRECT PASSWORD WAS {password}")
        game_on=False
        return 
    else:
        return

chances=10
def chancesremaining():#chances remaining
    global chances
    global game_on
    if(chances==0):
        print("OPPS YOU RAN OUT OF CHANCES")
        print(f"THE CORRECT PASSWORD WAS {password}")
        game_on=False
        return 
    else:
        print(f"you have {chances} chances remaining.......\n")
        chances=chances-1
password=str(random.randint(1000,9999))#randomise password generations
def getinput():#gets input from the user with correct format
    global guess
    guess = input("Guess the password (only numbers): ")
    
    # Check if the input consists of digits only
    if not guess.isdigit():
        print('Enter only numbers')
        return getinput()
    
    # Check if the input has the correct length (4 digits)
    if len(guess) != 4:
        print('The password should be 4 digits')
        return getinput()
    
    return guess
print('----------------------------PASSWORD GUESSING GAME----------------------------')
print("WELCOME TO PASSWORD GUESSING GAME\n",'WE WILL GENERATE A RANDOM 4 DIGIT PASSWORD FOR YOU\n ','YOU WILL BE GIVEN 10 CHANCES TO GUESS IT\n','ENJOY :)\n')

def play():#main structure of the game 
    global password
    while(game_on==True):
        getinput()
        print("number of correct digits guessed: ",correctelement(guess,password))
        print("number of correct digits guessed with correct positions: ",correctposition(guess,password))
        print('\n')
        chancesremaining()
        checkwin(guess,password)
play()