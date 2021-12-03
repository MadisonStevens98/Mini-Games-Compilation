import random #1st step


#this is just a collection of fun games, no betting our cost to play

#List of games/things to add
#dice: x
#number guessing: x
#slots: X
#hangman: x
#rock paper scissors: x
#coin flip: x
#keep track of all wins and losses

#cards: this will be a seperate py file, 

#we can also incorporate our shop/inventory

print("Welcome to our collection of mini games!")
Players_name = input("What is your name?")

#will keep track of all of the players wins and losses
total_wins = 0
total_losses = 0


#tokens = 100

###############################################################################################
#DICE
###################################################################################################
def dice():
  
  number_of_dice = input("How many dice do you want to roll?")#input always returns a string
  number_of_dice = int(number_of_dice)
  
  #dice can only be even numbers!
  type_of_dice = input("Please type the number of sides on your dice: ")
  type_of_dice = int(type_of_dice)
  
  
  roll = input("Roll your dice!") #you dont always need to check what input holds!!!
  
  total = 0
  
  #for loop loops a specific number of times
  for i in range(number_of_dice):
 
    dice = random.randint(1, type_of_dice)
    total += dice
    print(dice)
    
  print("Total roll is " + str(total))


#############################################################################################
#COIN FLIP
############################################################################################
#first step, make def
def coin_flip():
  #second step, write what we need
  #might add more user friendly logic later
  #we need a player variable, a computer/coin, and logic to compare
  player = input("Heads or Tails?(Upper case please)")
  coinlist = ["Heads", "Tails"]
  computer = random.choice(coinlist)
  print(computer)
  #if values match, we win, otherwise we lose
  if player == computer:
    print(Players_name +" won!")
  elif player != computer:
    print(Players_name + " lost")
  
#coin_flip();  

#############################################################################################
#SLOTS
###############################################################################################
def slots():
  
  #list of picutes for slots
  symbol_list = ["7", "$", "!", "<3", "(="]
  print("Welcome to slots!")
  lever = input("Start the slot machine!")
  
  slot1 = random.choice(symbol_list)
  slot2 = random.choice(symbol_list)
  slot3 = random.choice(symbol_list)
  print(slot1 + "  " + slot2 + "  " + slot3)
  
  if slot1 == slot2 and slot2 == slot3:
      #tokens += 3
      print("JACKPOT! " + Players_name  + " TRIPLED THEIR MONEY!")
      #print(tokens)
      
    #checking if two of our symbols match
  elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
      #tokens += 2
      print("Close!" + Players_name + " doubled their money though!")
      #print(tokens)
    
  else:
      print("Nope!" + Players_name + " lost.")

#############################################################################################
#NUMBER GUESSING
###############################################################################################
def Number_Guessing():
  #logic to check our guess
  max_number = input("What is the max number for your guessing range?")
  max_number = int(max_number)
  computer_number = random.randint(1, max_number)
  print(computer_number)
  player_number = input("Please guess a number")
  player_number = int(player_number)

  if computer_number == player_number:
    print(  Players_name + " won!")
  elif computer_number > player_number:
    print(  Players_name + "'s guess was too low")
  elif computer_number < player_number:
    print( Players_name + "'s guess was too high")
  else:
    print("error please guess a number")


#############################################################################################
#ROCK PAPER SCISSORS
###############################################################################################
def rps(): #def short for definition, rps short for rock paper scissors
 
  players_choice = input("\n" +"Please type rock paper or scissors") #the player is picking rock paper or scissors
  
  computers_choice = random.choice(["rock", "paper", "scissors"]) #list is in [] #the computers choice of rps
   
  print("The computer chose: " + "\n" +computers_choice) #prints out computers pick
  
  #if.. first 
  #elif(else if) middle
  #else last
  
  #TIE
  if players_choice == computers_choice: #if they both picked the same thing, then tie!
    print(Players_name + " tied")
    Ties += 1
  
  #PLAYER PICK ROCK
  elif players_choice == "rock" and computers_choice == "paper": #we picked rock and lost
    print(Players_name + " lost, Computer won") 
  
  elif players_choice == "rock" and computers_choice == "scissors": #we picked rock and won
    print(Players_name + " won, Computer lost")

  #PLAYER PICKED PAPER  
  elif players_choice == "paper" and computers_choice == "rock": #we picked paper and win
    print(Players_name + " won, Computer lost") 
  
  elif players_choice == "paper" and computers_choice == "scissors": #we picked paper and lost
    print(Players_name + " lost, Computer won")
    
  #PLAYER PICKED SCISSORS
  elif players_choice == "scissors" and computers_choice == "paper": #we picked scissors and win
    print(Players_name + " won, Computer lost") 
  
  elif players_choice == "scissors" and computers_choice == "rock": #we picked scissors and lost
    print(Players_name + " lost, Computer won")
  
  else: #we should never get the error message, if we do something is wrong
    print("error")

#############################################################################################
#HANGMAN
###############################################################################################
def hangman():
  wrongguesses = 0
  
  words2 = ["ice cream", "cupcake", "chocolate", "brownies", "pizza"]
  
  #list of only animals
  #this is a list, a list always uses []
  words = ["dogs", "cats", "bunnies", "rats", "hamsters"] #second step, make a list of words
  
  ourword = random.choice(words) #third step, make a variable to randomly select word from list
  
  print(ourword) #uncomment to test
  
  print("Welcome to Hangman!") #polish
  
  def drawhangman(wrongguesses):
    if wrongguesses == 1:
      print("The head has been drawn")
    elif wrongguesses == 2:
      print("The head and body are drawn")
    elif wrongguesses >= 6:
      print("You lose!")
      exit()
    else:
      print("error")
    
  #def is short for definition
  #let us guess a letter
  #recursive definition, means it calls itself, makes it loop 
  def guess(ourword, wrongguesses):
    
    #indent means code is inside
    letter = input("Please guess a letter: ")  #fourth step, ask player for letter=
    if letter in ourword: #fifth step, check if the letter they guessed is in string
      print("Niceeeee")#guessed right
      ourword = ourword.replace(letter, "")#removes the correctly guesse letter from the word
      print(ourword)
      
    else:
      print("Nope")#guessed wrong
      wrongguesses += 1
      print("You have guesses wrong " + str(wrongguesses) + " times")
      drawhangman(wrongguesses)
      
    #this call make our denition loop, forever!  
    guess(ourword, wrongguesses)
  
  #call, has to be below your definition!
  #to write a call you write the name of the defition followed by the () and any variables
  #def guess wont run without this!
  #called it the first time
  guess(ourword, wrongguesses)

#############################################################################################
#MAIN
###############################################################################################
#main is not required in python, but it is helpful
#main menu/controller for our player
def main():
  #triple quotes for large info to print
  print("\n"+"""Game Menu:
  1. Slots
  2. Number Guessing
  3. Cards
  4. Dice
  5. Rock, Paper, Scissors
  6. Hangman
  7. Coin Flip
  8. Cards/Card Games
  9. Quit
  """)
  game_input = input("Please type the number of the game you want to play.")
  #add in ORs here for the name of the game
  if game_input == "1":
    slots()
  elif game_input == "2":
    Number_Guessing()
  elif game_input == "3":
    print("cards")
  elif game_input == "4":
    #print("Dice")
    dice()
  elif game_input == "5":
    rps() 
  elif game_input == "6":
    hangman()
  elif game_input == "7":
    coin_flip()
  elif game_input == "8":
    print("cards")
  elif game_input == "9":
    exit()   #always ends the program
  else: #checking for bad input, never assume your player will do what you want!
    print("error")
    main() #this loops if they wrote in gibberish
  main()#this loops after each game
main()#this is our first call, calls our def the first time
