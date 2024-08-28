pos=["-","-","-",
     "-","-","-",
     "-","-","-"]
#create 2 lists one showing presentation of the board and other showing indexes
pos1=[1,2,3,4,5,6,7,8,9]
print('\n')
#function to display the index board called inside the main displayboard function
def displayindex():
    print("|",pos1[0],"|",pos1[1],"|",pos1[2],"|")
    print("|",pos1[3],"|",pos1[4],"|",pos1[5],"|")
    print("|",pos1[6],"|",pos1[7],"|",pos1[8],"|")
#function to display the board called everytime the board is updated
def displayboard(pos):
    print("|",pos[0],"|",pos[1],"|",pos[2],"|")
    print("|",pos[3],"|",pos[4],"|",pos[5],"|")
    print("|",pos[6],"|",pos[7],"|",pos[8],"|")
    print("\n")
    displayindex()

print("..........................WELCOME TO TICTACTOE...........................")
displayboard(pos)
global player1
#select the player 
def selectplayer():
    global player1
    global player2
    player1=input("player1 choose X or O: ")
    player2=''
    if(player1=='X'or player1=='x'):
        player2='O'
        return
    elif(player1=='O' or player1=='o'):
        player='X'
        return 
    else:
        print("please choose valid option:")
        print("enter X or O")
        selectplayer()

gameon=True
#update the board if gameon is true 
def updateboard(currentplayer,pos):
    if(gameon):
        position=int(input("choose a value from 1 to 9 corresponding to a postion on the board: "))
        if (position>9):
            print("oops! invalid index value")
            updateboard(currentplayer,pos)
        elif(pos[position-1]=='-'):
            pos[position-1]=currentplayer
            displayboard(pos)
            return 
        else:
            print(' oops! position already occupied try again: ')
            updateboard(currentplayer,pos)
    else:
        return
#checks if the game is over and who won
def checkwin():
    if(pos[0]==pos[1]==pos[2]!='-'):
        global gameon
        gameon=False
        print("CONGRAGULATIONS "+pos[0]+" you won the game")
    elif(pos[3]==pos[4]==pos[5]!='-'):
        gameon=False
        print("CONGRAGULATIONS "+pos[3]+" you won the game")
    elif(pos[6]==pos[7]==pos[8]!='-'):
        gameon=False
        print("CONGRAGULATIONS "+pos[6]+" you won the game")
    elif(pos[0]==pos[3]==pos[6]!='-'):
        gameon=False
        print("CONGRAGULATIONS "+pos[0]+" you won the game")
    elif(pos[1]==pos[4]==pos[7]!='-'):
        gameon=False
        print("CONGRAGULATIONS "+pos[1]+" you won the game")
    elif(pos[2]==pos[5]==pos[8]!='-'):
        gameon=False
        print("CONGRAGULATIONS "+pos[2]+" you won the game")
    elif(pos[0]==pos[4]==pos[8]!='-'):
        gameon=False
        print("CONGRAGULATIONS "+pos[0]+" you won the game")            
    elif(pos[2]==pos[4]==pos[6]!='-'):
        gameon=False
        print("CONGRAGULATIONS "+pos[2]+" you won the game")
    elif '-' not in pos:
        gameon=False
        print("THE GAME ENDED IN A TIE")
        return 
# main play function that calles all the functions 
def play():
    currentplayer='X'
    selectplayer()
    while gameon==True:
        updateboard(currentplayer,pos)
        checkwin()
        currentplayer='O'
        if(gameon==True):
            updateboard(currentplayer,pos)
            checkwin()
        currentplayer='X'

play()
