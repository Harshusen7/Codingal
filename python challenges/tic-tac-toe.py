# implemention of two player tic tac toe game in python.






theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)





def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll writethe main function which has all the gameplay functionality.
def game():

    turn ='X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is aldready filled.\nMove to which place?")
            continue


        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': #acros the top
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " +turn + " won. ****")
                break 
            elif  theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': #acros the middle
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " +turn + " won. ****")
                break 
            elif  theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': #acros the bottom
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " +turn + " won. ****")
                break 
            elif  theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': #acros the bottom
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " +turn + " won. ****")
                break 
            elif  theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': #acros the bottom
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " +turn + " won. ****")
                break 
            elif  theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': #acros the bottom
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " +turn + " won. ****")
                break 
            elif  theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': #acros the bottom
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " +turn + " won. ****")
                break 
            elif  theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': #acros the bottom
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " +turn + " won. ****")
                break 

        if count == 9:
            print("\nGame over\n")
            print("it's a tie!!")
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        









if __name__ == "__main__":
    game()

                

                

              
