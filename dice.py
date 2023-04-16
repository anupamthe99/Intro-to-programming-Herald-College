import random
def roll_dice():
    first_dice=random.randint(1,6)
    secound_dice=random.randint(1,6)
    guess_value=first_dice+secound_dice

    return guess_value

def guess_dice():
        times=0
        wins=0
        while True:
            dice_value=roll_dice()
            print(dice_value)
            guess_value_user=int(input("Enter the guess value of two dice :"))
            if dice_value!=guess_value_user:
                times+=1
            else:
                print(f"You guess the right ans in the {times} try")
                wins+=1
                times+=1

            continue_game=input("Do you want to continue or not (Y/N):").upper()

            if continue_game=="N":
                win_percentage(times,wins)
                break
            else:
                continue
def win_percentage(times,wins):
    print(times,wins)
    percent=(wins/times)*100 if times>0 else 0
    print(f"The winning percentage of the users is {percent} %")
    

guess_dice()
