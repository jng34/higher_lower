from random import choice
from art import logo, vs
from game_data import data
from os import system, name

################################
def clear():
    """Function to clear console"""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')
################################

score = 0

def get_account_info(random_obj):
  """Destructures an object and returns a string of information."""
  n, _, d, c = random_obj 
  return f"{random_obj[n]}, a {random_obj[d]}, and from {random_obj[c]}."


def check_answer(guess, followers_A, followers_B):
  """Takes in user guess, followers count for A and B. Returns boolean."""
  if followers_A > followers_B:
    return guess == 'a'
  else:
    return guess == 'b'


def start_game(score, random_A = choice(data), random_B = choice(data)):
  """Code base for higher-lower game."""
  clear()
  print(logo)
  if score > 0:
    print(f"Correct. Your score: {score}\n")

  # Ensures random A and B are different
  while random_B == random_A:
    random_B = choice(data)

  # Compare A and B: 'Name', 'Description', and from 'Country'
  print(f"Compare A: {get_account_info(random_A)}.")
  print(vs)
  print(f"Against B: {get_account_info(random_B)}.\n")

  guess = input('Who has more followers? Type "A"  or "B"?: ').lower()

  followers_A = random_A['follower_count']
  followers_B = random_B['follower_count']

  is_correct = check_answer(guess, followers_A, followers_B)
  if is_correct:
    score += 1
    start_game(score, random_B, choice(data))
  else:
    clear()
    print(logo)
    print(f"Sorry that is incorrect. Game over. Final score: {score}")


start_game(score)
