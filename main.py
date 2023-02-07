

#  The Text Based Game topic- Looking for a treasure in the Sparkle city.
import random  # imports random package
greeting = """
          Hello Seeker! You are welcome to Sparkle City, we hope you find the hidden treasure.
          Select the following options to navigate your way through the villages in Sparkle City
          Option 1: pick 1 to access Engratia Village.
          Option 2: pick 2 to access Gnosis Village.
          Option 3: pick 3 to access Koinonia Village.
          Option 4: pick 4 to access Agape Village.
          Option 5: pick 5 to access Light Village.
    """  # Greeting for seeker
while True:
  money_pouch = 0  # placeholder for coins gained
  bag = ["a hat"]  # list of items in bag
  health_status = 50  # placeholder for health status
  user_option = 0  # user option
  greetings = input(greeting)  # user picks option after greeting
  def intro():  # a function to allow users select an option
      if greetings == '1':
        print("Hello this is Engratia village")
      elif greetings == '2':
        print("Hello this is Gnosis village")
      elif greetings == '3':
        print("Hello this is Koinonia village")
      elif greetings == '4':
        print("Hello this is Agape village")
      elif greetings == '5':
        print("Hello this is Light village")
      else:
        print(str(input("Please input a valid number")))
        
  def guess_game( Name = '', Code = ''):  # a function that allows user play a guessing game
      print(f"Now you are required to play a guessing game with me as a the leader of {Name} to gain  access to the next village")
      leader_guess = random.randint(1,5)  # leader selects a random number
      seeker_guess = int(input("""
      I have selected my number, now guess what number I have chosen between 1 and 5, 
      to get your access code to the next village. Note that you have just 2 trials, 
      if you miss the second attempt, you remain here forever: """))  # seeker inputs his/her guess
      while True:
        if seeker_guess == leader_guess:  # if seeker guess equates leader's guess
          print("Access Granted")  # result
          print(f"Your access code is {Code}")  # access code given
          print(f" Your guess is {seeker_guess}")  # seeker guess
          print(f"My guess is {leader_guess}")  # leaders guess
        else:
          print("Access Denied")  # result if seeker first guess doesn't equate leaders guess
          seeker_guess = int(input("You have one more trail left, guess again: "))  # second trial
          if seeker_guess == leader_guess: # result if seeker guess equates leader's guess
            print(f"Your access code is {Code}")  # acccess code
            print(f" Your guess is {seeker_guess}")  # seeker guess
            print(f" My guess is {leader_guess}")  # leaders guess
          else:
            seeker_guess != leader_guess  # seeker guess doesn't equates leader's guess
            print("You stay here forever HAHAHAHA.")  # seeker remains in that village
            print(f" Your guess is {seeker_guess}")
            print(f"My guess is {leader_guess}")
            break  # program ends
        break   

  def treasure( Name = ''):  # function to locate treasure
    print(f"Now you are required to play a guessing game with me as a the leader of {Name} to gain access to the hidden treasure")  # guessing game
    leader_guess = random.randint(1,5)  # leader selects a number 
    seeker_guess = int(input("""
    I have selected my number, now guess what number I have chosen between 1 and 5, 
    to get your access code to the hidden treasure. Note that you have just 2 trials, 
    if miss the second attempt, you remain here forever: """))  # seeker picks a number
    while True:
      if seeker_guess == leader_guess:  # if seeker value equates leaders value
        print("Access Granted")  # access granted
        print("This is the treasure that has been hidden for ages, it is Code number COL 1:27")  # treasure
        print(f" Your guess is {seeker_guess}")  # seeker guess
        print(f"My guess is {leader_guess}")  # leader's guess
      else:
        print("Access Denied")  # result if seeker guess doesn't equates leader's guess
        seeker_guess = int(input("You have one more trail left, guess again: "))  # second trial
        if seeker_guess == leader_guess:  # if seeker guess equates leader's guess
          print("Access Granted")
          print("This is the treasure that has been hidden for ages, it is Code number COL 1:27")  # treasure
          print(f" Your guess is {seeker_guess}")  # seeker guess
          print(f" My guess is {leader_guess}")  # leader's guess
        else:
          seeker_guess != leader_guess  # result if seeker guess doesn't equates leader's guess
          print("You stay here forever HAHAHAHA.")
          print(f" Your guess is {seeker_guess}")
          print(f"My guess is {leader_guess}")
      break  # program ends
      
  # the first village 
  while True:
    intro()
    Engratia_village_leader = print(f"""
    Welcome to Engratia village, I am the village head of this village and you must be seeking for        the hidden treasure.
    To go ahead in this journey you need to have important things in place which are the following:
    1. A Good Health Status as the Light Village is very challenging to survive in.
    2. A bag to store your items.
    3. A money pouch to keep your acquired coins.
    Your current health status is {health_status}, your available coins is {money_pouch} and the item     in your bag currently is {bag}. To increase any of the 3 options, carefully select one of the   
    options below:
    """)  # introduction to the first village
    # booster1()
    booster = input("""
      Please pick between options 1 and 3:
      1. A bottle of water
      2. A music player
      3. 3 pieces of coin
      """)  # opportunity for user to boost a point
    if booster == '1':
      health_status += 20   # increase of health status
      print(f"Your current Health Status is {health_status}.")
    elif booster == '2':
      bag.append(" a music player")  # adding 'a music player' to list of items in the bag
      print(bag)
      print(f"You now have{bag} in addition to the items in your bag.")
    else:
      booster == '3'
      money_pouch += 3  # adding 3 coins to money_pouch
      print(f"Your total coins in your pouch is {money_pouch}")
    print()  # indicates a space
    guess_game(Name = 'Engratia village', Code ='K N 2 Q 8') # guessing game with its access code to the next village
    
 # Second village
    Gnosis_village_leader = input("""
    Welcome to Gnosis village, I am the village head of this village and you must be seeking for           the hidden treasure.
    Please kindly input the code given to you at Engratia Village: 
    """)  # user inputting the access code
    if Gnosis_village_leader == 'KN2Q8'.casefold(): # code if user's input equates the access code
      print(f"""To go ahead in this journey you need to have important things in place which are                 the following: 
      1. A Good Health Status as the Light Village is very challenging to survive in.
      2. A bag to store your items.
      3. A money pouch to keep your acquired coins.
      Your current health status is {health_status}
      your available coins is {money_pouch} and the items in your bag currently is {bag}. 
      To increase any of the 3 options, carefully select one of the options below:
      """)  # introduction to the second village
      
      booster2 = input("""
        Please pick between options 1 and 3:
        1. A bottle of Alcohol
        2. A map
        3. 1 piece of coin
        """)  # user allowed to boost points
        
      if booster2 == '1':
        health_status -= 30  # subtracts value from current health status
        print(f"Your current Health Status is {health_status}.")
      elif booster2 == '2':
        bag.append(" a map")  #addition of a map
        print(f"You now have {bag} in addition to the items in your bag.")
      else:
        booster2 == '3'
        money_pouch += 1  # increasing the value of money pouch
        print(f"Your total coins in your pouch is {money_pouch}")
      print()  # indicates a space
    else:
      Gnosis_village_leader != 'KN2Q8'.casefold()  # wrong access code input result
      print("You can't have access to this village without the access code")  # user not allowed to access this village
      input("Type exit to exit: ")
      break
    guess_game(Name = 'Gnosis village', Code ='W K 9 C Y')  # guessing game with its access code to the next village

    # Third village
    # Koinonia Village  Village 3
    Koinonia_village_leader = input("""
    Welcome to Koinonia village, I am the village head of this village and you must be seeking for           the hidden treasure.
    Please kindly input the code given to you at Gnosis Village: 
    """)  # user inputs access code
    if Koinonia_village_leader == 'WK9CY'.casefold():
      print(f"""To go ahead in this journey you need to have important things in place which are                 the following: 
      1. A Good Health Status as the Light Village is very challenging to survive in.
      2. A bag to store your items.
      3. A money pouch to keep your acquired coins.
      Your current health status is {health_status}
      your available coins is {money_pouch} and the items in your bag currently is {bag}. 
      To increase any of the 3 options, carefully select one of the options below:
      """)  # welcome message to the Koinonia village
      
      booster3 = input("""
        Please pick between options 1 and 3:
        1. A bottle of herbs
        2. A biro
        3. 2 piece of coin
        """)  # boosting points for user
        
      if booster3 == '1':
        health_status += 10  # increament of health status
        print(f"Your current Health Status is {health_status}.")
      elif booster3 == '2':
        bag.append(" a biro")  # appending of biro to bag items
        print(f"You now have a {bag} in addition to the items in your bag.")
      else:
        booster3 == '3'
        money_pouch += 2  # increasing the value of money_pouch
        print(f"Your total coins in your pouch is {money_pouch}")
      print()  # indicates a space
    else:
      Koinonia_village_leader != 'WK9CY'.casefold()  # code for invalid access code
      print("You can't have access to this village without the access code")
      input("Type exit to exit: ")
      break  # ends program
    guess_game(Name = 'Koinonia village', Code ='A 6 R 1 Y')  # guessing game with access code for the fourth village

    # Fourth village
    # Agape Village  Village 3
    Agape_village_leader = input("""
    Welcome to Agape village, I am the village head of this village and you must be seeking for           the hidden treasure.
    Please kindly input the code given to you at Koinonia Village: 
    """)  # user inputs access code
    if Agape_village_leader == 'A6R1Y'.casefold():  # code if user input is valid
      print(f"""To go ahead in this journey you need to have important things in place which are                 the following: 
      1. A Good Health Status as the Light Village is very challenging to survive in.
      2. A bag to store your items.
      3. A money pouch to keep your acquired coins.
      Your current health status is {health_status}
      your available coins is {money_pouch} and the items in your bag currently is {bag}. 
      To increase any of the 3 options, carefully select one of the options below:
      """)  # introduction message for fourth village
      
      booster4 = input("""
        Please pick between options 1 and 3:
        1. A bottle of soap
        2. A rope
        3. 1000 pieces of coin
        """)  # boosting time for user
        
      if booster4 == '1':
        health_status -= 20  # reduction of ealth status
        print(f"Your current Health Status is {health_status}.")
      elif booster4 == '2':
        bag.append(" a rope")  # adding a rope to bag list
        print(f"You now have a {bag} in addition to the items in your bag.")
      else:
        booster4 == '3'
        money_pouch -= 5  # subtracting value of money_pouch
        print(f"Your total coins in your pouch is {money_pouch}")
        print("You acted like a greedy person and did not pick what was necessary")
      print()  # indicates a space
    else:
      Agape_village_leader != 'A6R1Y'.casefold()  # code for invalid input of access code
      print("You can't have access to this village without the access code")
      input("Type exit to exit: ")
      break
    guess_game(Name = 'Agape village', Code ='7 T 3 P F')  # guessing game and access code for the next village

    # Fifth village
    # Light Village  Village 3
    Light_village_leader = input("""
    Welcome to Light village, I am the village head of this village and you must be seeking for           the hidden treasure.
    Please kindly input the code given to you at Agape Village: 
    """)  # user inputs access code
    if Light_village_leader == '7T3PF'.casefold():  # code if user input is correct
      print(f"""To go ahead in this journey you need to have important things in place which are                 the following: 
      1. A Good Health Status as the Light Village is very challenging to survive in.
      2. A bag to store your items.
      3. A money pouch to keep your acquired coins.
      Your current health status is {health_status}
      your available coins is {money_pouch} and the items in your bag currently is {bag}.
      """)
      if health_status < 50:  # code if value of health status is lower than 50
        print("Sorry we can't allow you in this village, you have a poor health status")
        print("Therefore, you cannot go further you remain here in the village forever")
        input("Type exit to exit: ")
        break  # ends program
      else:
        health_status >= 50  # code if value of health status is higher than 50
        print("Move on you're almost there.")
        if money_pouch < 3:  # code if value of money_pouch is lower than 3
          print("Sorry, you can't go ahead, you need to pay tax of 3 coins to enter this village.")
          print("Therefore, you cannot go further you remain here in the village forever")
          input("Type exit to exit: ")
          break
        else:
          money_pouch > 3  # code if value of money_pouch is higher than 3
          print(" Move on you are almost there.")
          if ' a rope' in bag:  # code if a code is the bag
            print("Use the rope you have with you to climb the wall")
            treasure( Name = 'Light Village')
            input("Type exit to end the game: ")
            break
          else:  # code if a code is not the bag
            ' a rope' not in bag
            print("You almost got there, but you have no rope with you to climb the wall") 
            print("Therefore, you cannot go further you remain here in the village forever")
            input("Type exit to exit")
            break
          break
    else:
      Light_village_leader != '7T3PF'.casefold() # code if access code is invalid
      print("You can't have access to this village without the access code")
      input("Type exit to exit: ")
      break
  break  # end of game

    
    
    
        

    
    
    
    
   