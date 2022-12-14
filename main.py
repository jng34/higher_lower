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

def start_game(score, random_A = choice(data), random_B = choice(data)):
  clear()
  print(logo)
  if score > 0:
    print(f"Correct. Your score: {score}")

  # Compare A: 'Name', 'Description', and from 'Country'
  # Destructuring
  n, fc, d, c = random_A 
  followers_A = random_A[fc]
  print(f"Compare A: {random_A[n]}, a {random_A[d]}, and from {random_A[c]}.")

  print(vs)

  # Compare B: 'Name', 'Description', and from 'Country'
  # Ensures random A and B are different
  while random_B == random_A:
    random_B = choice(data)

  n, fc, d, c = random_B 
  followers_B = random_B[fc]
  print(f"Compare B: {random_B[n]}, a {random_B[d]}, and from {random_B[c]}.\n")

  guess = input('Who has more followers? Type "A"  or "B"?: ').lower()

  is_A_greater_than_B = followers_A > followers_B
  if guess == 'a' and is_A_greater_than_B == True:
    score += 1
    start_game(score, random_B, choice(data))
  elif guess == 'b' and is_A_greater_than_B == False:
    score += 1
    start_game(score, random_B, choice(data))
  else:
    clear()
    print(logo)
    print(f"Sorry that is incorrect. Game over. Final score: {score}")


start_game(score)
