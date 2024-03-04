import random

def user_choice():
 
  while True:
    user_input = input("Choose rock, paper, or scissors: ").lower()
    if user_input in ["rock", "paper", "scissors"]:
      return user_input
    else:
      print("Invalid choice. Please choose rock, paper, or scissors.")

def computer_choice():


  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)

def determine_winner(user_choice, computer_choice):
 

  if user_choice == computer_choice:
    return "tie"
  elif user_choice == "rock":
    if computer_choice == "scissors":
      return "user"
    else:
      return "computer"
  elif user_choice == "paper":
    if computer_choice == "rock":
      return "user"
    else:
      return "computer"
  elif user_choice == "scissors":
    if computer_choice == "paper":
      return "user"
    else:
      return "computer"

def play_game():
  """Runs a single round of the rock-paper-scissors game."""

  user_score = 0
  computer_score = 0

  while True:
    user_choices = user_choice()
    computer_choices = computer_choice()

    print(f"\nYou chose: {user_choices.upper()}")
    print(f"Computer chose: {computer_choices.upper()}")

    winner = determine_winner(user_choices, computer_choices)

    if winner == "user":
      user_score += 1
      print("You win!")
    elif winner == "computer":
      computer_score += 1
      print("Computer wins!")
    else:
      print("It's a tie!")

    print(f"Score: You - {user_score}, Computer - {computer_score}")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
      break

# Start the game
play_game()
print("Thanks for playing!")

