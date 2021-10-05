import random


# Bonus added:
    
# Guess the number game with unlimited guesses at a random number 0-1000,
# displays if the guess is above or below the hidden number and when the number is guessed
# it displays you have guessed it and how many tries it took

# Mad lib game with three story options that takes string inputs to fill the blanks
# of the stories and then prints out the story with the blanks filled to the user


def main():
    print('Welcome to the game menu!\n')
    display_menu()
    menu_choice = input('Enter the number of the item you wish to use in the menu: ')
    
    # Keep user in menu until they choose to exit
    while menu_choice != '6':
        if menu_choice == '1':
            rps_game()
        elif menu_choice == '2':
            draw_game()
        elif menu_choice == '3':
            currency_calc()
        elif menu_choice == '4':
            number_guess()
        elif menu_choice == '5':
            mad_lib()
        elif menu_choice == '6':
            pass
        else:
            print('Invalid option, please enter a valid menu choice.')
        display_menu()
        menu_choice = input('Enter the number of the item you wish to use in the menu: ')
        
    #Tell user goodbye 
    exit_game()

def rps_game():
    # User enters choice
    print('Welcome to the Rock, Paper, Scissors game')
    user_choice = input('Please enter Rock, Paper, or Scissors: ').lower()
    input_check = is_valid_rps(user_choice)
    
    # Check user choice
    while input_check == False:
        print('Incorrect Value.')
        user_choice = input('Please enter Rock, Paper, or Scissors: ').lower()
        input_check = is_valid_rps(user_choice)
        
    # Generate computer choice(0: rock, 1:paper, 2:scissor)
    com_choice = random.randint(0,2)
    
    # Compare choices and define winner
    if user_choice == 'rock':
        print('\nYou chose rock')
        if com_choice == 0:
            print('Computer chose rock. You Tied\n')
        elif com_choice == 1:
            print('Computer chose paper. You Lose\n')
        elif com_choice == 2:
            print('Computer chose scissor. You Win!\n')
    elif user_choice == 'paper':
        print('\nYou chose paper')
        if com_choice == 0:
            print('Computer chose rock. You Win!\n')
        elif com_choice == 1:
            print('Computer chose paper. You Tied\n')
        elif com_choice == 2:
            print('Computer chose scissor. You Lose\n')
    elif user_choice == 'scissor':
        print('\nYou chose scissor')
        if com_choice == 0:
            print('Computer chose rock. You Lose\n')
        elif com_choice == 1:
            print('Computer chose paper. You Win!\n')
        elif com_choice == 2:
            print('Computer chose scissor. You Tied\n')

# Check if user choice is valid
def is_valid_rps(user_choice):
    if user_choice == 'rock':
        return True
    elif user_choice == 'paper':
        return True
    elif user_choice == 'scissors':
        return True
    else:
        return False

def draw_game():
    # User selects triangle or rectangle
    print('Welcome to the drawing game')
    user_choice = input('Please enter triangle or rectangle: ').lower()
    input_check = is_valid_draw(user_choice)
    
    # Check user choice for trinagle or rectangle
    while input_check == False:
        print('Incorrect Value.')
        user_choice = input('Please enter triangle or rectangle: ').lower()
        input_check = is_valid_draw(user_choice)
    
    # User selects character they want to draw with
    draw_character = input('Please enter a single character you wish to draw with: ')
    char_check = is_valid_char(draw_character)
    
    # Check user choice for single char
    while char_check == False:
        print('Invalid selection')
        draw_character = input('Please enter a single character you wish to draw with: ')
        char_check = is_valid_char(draw_character)
        
    # User selects L & W
    # Triangle Length
    if user_choice == 'triangle':
        LW_input = input('Please enter the desired length of the two equal sides of the triangle: ')
        LW_check = is_valid_LW(LW_input)
        
        # Make sure valid Length or Width
        while LW_check == False:
            print('Invalid choice, please enter an integer above 1')
            LW_input = input('Please enter the desired length of the two equal sides of the triangle: ')
            LW_check = is_valid_LW(LW_input)
        
        # Set length of triangle
        length = int(LW_input)
    
    # Rectangle length and width
    else:
        # rectangle length
        LW_input = input('Please enter the desired length of the rectangle: ')
        LW_check = is_valid_LW(LW_input)
        
        # Make sure valid Length or Width
        while LW_check == False:
            print('Invalid choice, please enter an integer above 1')
            LW_input = input('Please enter the desired length of the two equal sides of the triangle: ')
            LW_check = is_valid_LW(LW_input)
            
        length = int(LW_input)
        
        # rectangle width
        LW_input = input('Please enter the desired width of the rectangle: ')
        LW_check = is_valid_LW(LW_input)
        
        # Make sure valid Length or Width
        while LW_check == False:
            print('Invalid choice, please enter an integer above 1')
            LW_input = input('Please enter the desired length of the two equal sides of the triangle: ')
            LW_check = is_valid_LW(LW_input)
            
        width = int(LW_input)
            
    # Print shapes
    print('\n')
    # Triangle Print
    if user_choice == 'triangle':
        for i in reversed(range(length+1)):
            for j in range(i):
                print(draw_character, end='')
            print()
    # Rectangle Print
    else:
        for x in range(width):
            print('@', end='')
            for y in range(length-1):
                x*=y
                print('@', end='')
            print()
    print('\n')
     
# Check if user choice is valid
def is_valid_draw(user_choice):
    if user_choice == 'triangle':
        return True
    elif user_choice == 'rectangle':
        return True
    else:
        return False

# Check is user choice is single character not space
def is_valid_char(draw_character):
    if draw_character == ' ':
        return False
    elif len(draw_character) > 1:
        return False
    elif len(draw_character) < 1:
        return False
    else:
        return True
    
def is_valid_LW(LW_input):
    # Check that value is integer
    try:
        int(LW_input)
    except ValueError:
        print('Value is not an integer')
        return False
    
    # Check that value is greater than or equal to 2
    if int(LW_input) >= 2:
        return True
    else:
        return False

def currency_calc():
    print('Welcome to the currency calculator')
    user_dolla = input('Please enter a dollar amount : $')
    dolla_check = is_valid_dolla(user_dolla)
    
    # Check for valid dollar amount
    while dolla_check == False:
        user_dolla = input('Please enter a dollar amount : $')
        dolla_check = is_valid_dolla(user_dolla)
    
    # Create amount as float and variables for types of currency
    amount = float(user_dolla)
    start_amount = amount
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    
    # Calculate amount of each type of currency and subtract out
    while amount != 0:
        if amount-1 >= 0:
            amount -= 1
            dollars += 1
        elif amount-0.25 >= 0:
            amount -= 0.25
            quarters += 1
        elif amount-0.10 >= 0:
            amount -= 0.10
            dimes += 1
        elif amount-0.05 >= 0:
            amount -= 0.05
            nickels += 1
        elif amount-0.01 >= 0:
            amount -= 0.01
            pennies += 1
        # Needed to add round because decimals looked like 0.010000000000000142
        amount = round(amount, 2)
        
    # Print amount of each currency with correct plural endings
    print(f"\n${start_amount} has , ", end='')
    if dollars == 1:
        print(f"{dollars} dollar, ", end='')
    else:
        print(f"{dollars} dollars, ", end='')
    if quarters == 1:
        print(f"{quarters} quarter, ", end='')
    else:
        print(f"{quarters} quarters, ", end='')
    if dimes == 1:
        print(f"{dimes} dime, ", end='')
    else:
        print(f"{dimes} dimes, ", end='')
    if nickels == 1:
        print(f"{nickels} nickel, and ", end='')
    else:
        print(f"{nickels} nickels, and ", end='')
    if pennies == 1:
        print(f"{pennies} penny, ", end='')
    else:
        print(f"{pennies} pennies, ", end='')
    print('\n')
    
def is_valid_dolla(user_dolla):
    # Check that value is float
    try:
        float(user_dolla)
    except ValueError:
        print('Improper value, not a dollar amount')
        return False
    
    # Check that value is positive
    if float(user_dolla) >= 0:
        return True
    else:
        print('Value must be a positive dollar amount')
        return False
    
def number_guess():
    print('Welcome to guess the number')
    
    # Generate THE number and guess count
    THE_num = random.randint(0,1000)
    count = 0
    user_guess = -1
    
    # Check if guess is accurate
    while int(user_guess) != THE_num:
        user_guess = input('Guess the number between 0-1000: ')
        guess_check = is_valid_guess(user_guess)
    
        # check guess validity
        while guess_check == False:
            user_guess = input('Guess the number between 0-1000: ')
            guess_check = is_valid_guess(user_guess)
        
        count += 1
        
        # check guess to number
        if int(user_guess) > THE_num:
            print('You guessed above the number. Try again')
        elif int(user_guess) < THE_num:
            print('You guessed below the number. Try again')
    
    # Confirm correct guess and number of attempts
    print(f"Correct! The number was {THE_num}, it took you {count} guesses to find it\n")
    
    
def is_valid_guess(user_guess):
    # check guess is number
    try:
        int(user_guess)
    except ValueError:
        print('Invalid input, not a number')
        return False
    
    # check guess is between 0-1000
    if 0 <= int(user_guess) <= 10000:
        return True
    else:
        print('Inavlid input, must be between 0-1000')
        return False
    

def mad_lib():
    print('\nWelcome to the mad lib game\n')
    print('1. MIS 541 class\n2. Camping Trip\n3. Cafeteria Lunch')
    user_choice = input('Please select the number of the story you wish to play: ')
    valid_choice = is_valid_choice(user_choice)
    
    # confirm user menu choice
    while valid_choice == False:
        print('1. MIS 541 class\n2. Camping Trip\n3. Cafeteria Lunch')
        user_choice = input('Please select the number of the story you wish to play: ')
        valid_choice = is_valid_choice(user_choice)
    
    # route to different mad lib story paths
    if user_choice == '1':
        MIS_mad_lib()
    elif user_choice == '2':
        camp_mad_lib()
    elif user_choice == '3':
        lunch_mad_lib()


def MIS_mad_lib():
    # Collect the blanks
    adjective1 = input('Enter an adjective: ')
    verb1 = input('Enter a verb: ')
    plural_noun1 = input('Enter a plural noun: ')
    adjective2 = input('Enter an adjective: ')
    noun1 = input('Enter a noun: ')
    adverb1 = input('Enter an adverb: ')
    animal1 = input('Enter an animal: ') 
    number1 = input('Enter a number: ') 
    adjective3 = input('Enter an adjective: ')
    noun2 = input('Enter a noun: ')
    
    # Print the story
    print(f"\n{adjective1} Danish started out class with some easy python lessons. ", end='')
    print(f"He made the students {verb1} while they coded, ", end='')
    print(f"and they had to use {plural_noun1} as keyboards. Gehrig showed up late, ", end='')
    print(f"bringing a/an {adjective2} {noun1} claiming it would help us code. ", end='')
    print(f"Ryland stood up {adverb1} and proclaimed that his pet {animal1} died. ", end='')
    print(f"Danish gave the class {number1} bonus points and threw a/an {adjective3} funeral. ", end='')
    print(f"Since class was disrupted we had to do an extra PA about a/an {noun2}. Thanks Ryland!\n")

def camp_mad_lib():
    # Collect the blanks
    noun1 = input('Enter a noun: ')
    adjective1 = input('Enter an adjective: ')
    verb1 = input('Enter a verb: ')
    noun2 = input('Enter a noun: ')
    number1 = input('Enter a number: ') 
    adjective2 = input('Enter an adjective: ')
    animal1 = input('Enter an animal: ')
    adjective3 = input('Enter an adjective: ')
    adjective4 = input('Enter an adjective: ')
    noun3 = input('Enter a noun: ')
    
    # Print the story
    print(f"\nOnce upon a time I went camping at {noun1} park, with my {adjective1} son. ", end='')
    print(f"We went down to the lake to {verb1}. Then my son was taken mysteriously. ", end='')
    print(f"The only piece of evidence left behind was a/an {noun2}. I leave the park. ", end='')
    print(f"{number1} years later, a/an {adjective2} man shows up to my door and we return to the park. ", end='')
    print(f"We go deep into the forest and a {animal1} kills the man and takes me to my son. ", end='')
    print(f"My son is now the leader of the {adjective3} people. My son did not recognize me, ", end='')
    print(f"kill the {adjective4} man with the {noun3}, and eat his remains he commanded. The End!\n")

def lunch_mad_lib():
    # Collect the blanks
    adjective1 = input('Enter an adjective: ')
    noun1 = input('Enter a noun: ')
    food1 = input('Enter a type of food: ')
    adjective2 = input('Enter an adjective: ')
    body_part1 = input('Enter a body part: ')
    adjective3 = input('Enter an adjective: ')
    noun2 = input('Enter a noun: ')
    adverb1 = input('Enter an adverb: ')
    adjective4 = input('Enter an adjective: ')
    
    # Print the story
    print(f"\nDanielle is on lunch duty. She hates {adjective1} {noun1}. But she loves the {food1} ", end='')
    print(f"that the lunch ladies serve. A/An {adjective2} student shows up in the lunch line ", end='')
    print(f"not wearing his mask correctly. He was wearing it on his {body_part1}. Danielle ", end='')
    print(f"is fed up with {adjective3} students not wearing it correctly so she picks up a/an {noun2} ", end='')
    print(f"and throws it at him. It kills him {adverb1} and Danielle is fired. By the ", end='')
    print(f"{adjective4} principle. Wear your mask correctly kids, the end.\n")

# check validity of user menu choice
def is_valid_choice(user_choice):
    if user_choice == '1':
        return True
    elif user_choice == '2':
        return True
    elif user_choice == '3':
        return True
    else:
        print('Invalid menu option')
        return False

def display_menu():
    print('1. Rock, Paper, Scissors\n2. Draw Shapes\n3. Currency Calculator')
    print('4. Guess the Number\n5. Mad Libs\n6. Exit')
    
def exit_game():
    print('\nThank you for playing! Come again!')
    
main()