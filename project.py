#This is a classic game of tic tac toe
import os
def main():

    positions = {1: '1' , 2: '2' , 3: '3' , 4: '4' , 5: '5' , 6: '6' , 7: '7' , 8: '8', 9: '9'}
    board_template(positions)

    turn = 0
    prev_turn = -1
    complete = False
    play = True

    while play:
        os.system('cls' if os.name =='nt' else 'clear')
        board_template(positions)
        if prev_turn == turn:
            print(has_been_picked(prev_turn, turn))
        prev_turn = turn

        #For user input
        print("")
        print("Player " + str((turn%2)+1) + " turn: Pick your position or you can press q to quit")
        choice = input()

        if choice == "q":
            play = False

        elif str.isdigit(choice) and int(choice) in positions:
            #Update board if valid
            if not positions[int(choice)] in {"X" , "0"}:
                turn += 1
                positions[int(choice)] = track_turn(turn)
        #To indicate there is a winner
        if winnings(positions): play, complete = False, True
        #No winner
        if turn > 8: play = False

    #Print the result and draw board one last time
    os.system('cls' if os.name =='nt' else 'clear')
    board_template(positions)

    #If there is a winner, who wins
    if complete:
        print(tracking_turn(turn))

    else:
        #If a tie happens
        print("Its a tie")

#Board template
def board_template(positions):
    board =(f"|{positions[1]}|{positions[2]}|{positions[3]}|\n|{positions[4]}|{positions[5]}|{positions[6]}|\n|{positions[7]}|{positions[8]}|{positions[9]}|")
    print(board)

#To track the number of turns and the players
def track_turn(turn):
    if turn%2 == 0:
        return '0'
    else:
        return 'X'

#Winning conditions
def winnings(positions):
    if(positions[1] == positions[2] == positions[3]) or (positions[4] == positions[5] == positions[6]) or (positions[7] == positions[8] == positions[9]):
        return True
    elif(positions[1] == positions[4] == positions[7]) or (positions[2] == positions[5] == positions[8]) or (positions[3] == positions[6] == positions[9]):
        return True
    elif(positions[1] == positions[5] == positions[9]) or (positions[3] == positions[5] == positions[7]):
        return True
    else:
        return False

#Preventing overriding of positions
def has_been_picked(prev_turn, turn):

     if prev_turn == turn:
        return "Dude it has already been picked"

#For better orgainsation:
def tracking_turn(turn):
    if track_turn(turn) == 'X':

        return "Player 1 wins"

    else:

        return "Player 2 wins"



if __name__ == "__main__":
    main()