import time

startgame = input("Enter 'start' to load the game ")

print("Game Loading......")
time.sleep(2)
print("")
print("Welcome to the island")
print("The mission is to find the treasure ")
step = True
while step:
  choice_1 = input("Enter 'left' or 'right' to turn left or right respectively ").lower()
  if choice_1 == "right":
    print("Oops, you have fallen into a ditch")
    print("Game Over !")
    break
  elif choice_1 =="left":
    print("Welcome, Will you like to wait or swim ?")
    while True:
      choice_2 = input("Enter wait or swim ").lower()
      if choice_2 == "wait":
        print("Alright! which door will you like to stay?")
        
        choice_3 = input("choose either 'red', 'yellow', 'blue' ").lower()
        if choice_3 == "red":
          print("Oops! You have been burnt by fire ")
          print("Game over!")
     
        elif choice_3 == "yellow":
          print("Hurray!! You win")
        elif choice_3 == "blue":
          print("You have been eaten by beast")
          
        else:
          print("Game Over")
        break
      
      elif choice_2 == "swim":
        print("Attacked by trout")
        print("Game Over!")
        break
      else:
        print("Please enter wait or swim ")
    
    step = False
  else:
    print("Please enter 'left or 'right' to continue")