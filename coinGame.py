# importing the random module
import random
import time
play = True 
print("Welcome to the coin game")
print("")
name = input("Player Name: ")
print("")
while play:
    print(f"Hi { name },  choose between a Head or Tail as your guess to the outcome of tossing a fair coin ")
    print("")
    validation = True
    while validation:
        choice = input("Head or Tail: ")
        print("")
        choice = choice.lower()
        if choice != "head" and choice != "tail":
            print("Please input only 'Head' or 'Tail'")
        else:
            validation = False
    if choice == 'head' :
        print("You have chosen 'Head' ")
    else:
        print("You have chosen 'Tail' ")

    print("Tossing Coin.....................")
    print("")
    time.sleep(2.4)
    value = random.randint(0, 100000) % 2
    if choice == "head" and value =="1":
        print(f"Hello { name }, Congratulation you got a 'HEAD' you are saved !")
    elif choice == "tail" and value != 1:
        print(f"{ name }, Congratulation you got a 'TAIL', you are saved!")
    else: 
        print("Oops! you are out of the game !")
        print("")
        print("Thanks for playing")
    print("")
    valid_continue = True
    while valid_continue:
        cont_value = input("Would you like to continue the game? (Yes or No):  ").lower()    
        if cont_value != "no" and cont_value != 'yes':
            print("Please inpute 'Yes' or ' No' ")
        else:
            valid_continue = False
    if cont_value == "no":
        print("Game shutting done ............")
        time.sleep(2)
        play = False
    elif cont_value == "yes":
        print("Thank you")
        print("")
        print("Loading new game .......")
        time.sleep(2)
        print("") 