import random

# Roll a die until you reach 21. You bust if you go over 21. 
def dice_game():
    total = 0
    while total <= 21:
        i = input("Roll again? (y/n) ")
        if i=="y":
            roll = random.randint(1, 6)
            total += roll
            print(f"You rolled {roll}, total is {total}")
        else:
            if total == 21:
                print("Congrats, you got a perfect score!")
            else:
                print(f"You were {21 - total} away from 21")
            print(f"Final total: {total}")
            quit()
    print(f"Bust! Your total was {total}, which is {total-21} more than 21.")

dice_game()
