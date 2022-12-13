from random import choice
from art import logo, vs
from game_data import data

print(logo)

# Compare A: 'Name', 'Description', and from 'Country'
random_A = choice(data)
# Destructuring
n, fc, d, c = random_A 
print(f"Compare A: {random_A[n]}, a {random_A[d]}, and from {random_A[c]}.")

print(vs)

# Compare B: 'Name', 'Description', and from 'Country'
random_B = choice(data)
# Ensures random A and B are different
while random_B == random_A:
  random_B = choice(data)


n, fc, d, c = random_B 
print(f"Compare B: {random_B[n]}, a {random_B[d]}, and from {random_B[c]}.")
# guess = input('Who has more followers? Type "A"  or "B"?: ')