from noughtscross import*
def main():
    '''This function is the main function through which all of the
    functions are envoked with the passing of necessary arguments in parameters.
    '''
    #Is filled in the empty cells in the board when draw_board is called.
    board=[['1','2','3'],\
           ['4','5','6'],\
            ['7','8','9']]
    #Envokes the welcome function.
    welcome(board)
    #Envokes the draw_board function.
    draw_board(board)
    total_score=0  
    wins =0 
    while True:
        choice=menu()
        if choice=="1":
            score = play_game(board) 
            total_score+= score
            if score==1:
                wins+=1
            print("Your current score is:",total_score)
            
        if choice=="2":
            #This gets executed if choice 2 is selected.
            save_score(score)
        
        if choice=="3":
            #This gets executed if choice 3 is selected.
            leaders=load_scores()
            display_leaderboard(leaders)
            
        if choice=="q":
        #This gets executed if the program is quitted.
             print("Thankyou for playing the 'Unbeatable Noughts and Crosses'game.")
             print("Good bye")
             return
    
if __name__ =="__main__":
    main()
