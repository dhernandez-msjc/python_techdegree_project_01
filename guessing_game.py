"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

# base game settings -----------
MIN = 1
MAX = 10
current_high_score = []


def display_intro() -> None:
    print("Welcome to the Number Guessing Game!")
    if current_high_score:
        print(f"Current top score {min(current_high_score)}")
    print()


def validate_user_guess(user_guess):
    try:
        user_guess = int(user_guess)
    except ValueError:
        pass
    else:
        if MIN <= user_guess <= MAX:
            return True
    print(f"You must enter a number between {MIN} and {MAX}.\n")
    return False


def display_hint(guess: int, solution: int) -> None:
    if guess > solution:
        hint = "Lower"
    elif guess < solution:
        hint = "Higher"
    print(f"It's {hint}.\n")


def display_results(number_of_attempts):
    print("You guessed the number!")
    if number_of_attempts == 1:
        print(f"You guessed in {number_of_attempts} attempt.")
    else:
        print(f"You guessed in {number_of_attempts} attempts.")
    print()


def display_game_over() -> None:
    print("Thank you for playing the Number Guessing Game.")


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    continue_playing = True

    while continue_playing:
        display_intro()
        solution = random.randint(MIN, MAX)
        number_of_attempts = 0
        still_guessing = True

        while still_guessing:
            player_input = input(f"Guess a number between {MIN} and {MAX}:  ")
            is_valid_guess = validate_user_guess(player_input)
            if is_valid_guess:
                number_of_attempts += 1
                players_guess = int(player_input)
                if players_guess == solution:
                    still_guessing = False
                    current_high_score.append(number_of_attempts)
                else:
                    display_hint(players_guess, solution)
        display_results(number_of_attempts)

        player_response = input("Would you like to play again <y/n>: ")
        continue_playing = player_response == 'y'
        print()

    # end the game if the player chooses not to continue
    display_game_over()

# Kick off the program by calling the start_game function.
start_game()