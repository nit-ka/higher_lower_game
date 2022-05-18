# Higher lower game

from art import logo, vs
from game_data import data
import random
from replit import clear

def pick_random_person(list_name):
  '''Picks a random person from a list, returns a "message" with name and descripion, and also a "follower_count". Removes the record from the list.'''
  no_of_records = len(list_name)
  random_number = random.randint(1, no_of_records)
  choice = list_name.pop(random_number - 1)
  name = choice['name']
  follower_count = choice['follower_count']
  proffession = choice['description']
  country = choice['country']
  message = f"{name}, {proffession} from {country}."
  return message, follower_count

def compare_number(number_a, number_b):
  '''Returns "A" if number_a is bigger than number_b. Returns "B" if the opposite.'''
  if number_a > number_b:
    return "A"
  else:
    return "B"

def game_higher_lower():
  person_a = pick_random_person(data)
  person_b = pick_random_person(data)
  score = 0 
  game_on = True
  
  while game_on and len(data) > 0:
    print(logo)
    if score > 0:
      print(f"Correct answer. Your score: {score}")
    print(person_a[0])
    print(vs)
    print(person_b[0])
    users_choice = input("Who has more followers? Type 'A' or 'B': ")
    if users_choice != compare_number(person_a[1], person_b[1]):
      clear()
      print(logo)
      print(f"Wrong answer. Game over. Final score: {score}")
      game_on = False
    else:
      score += 1
      person_a = person_b
      person_b = pick_random_person(data)
      clear()
  if len(data) == 0:
    print("Congratulations! You win!")
    
game_higher_lower()

next_game = True
while next_game:
  ask_user_next_game = input("Do you want to play again? Type 'yes' or 'no'\n")
  if ask_user_next_game == "yes":
    clear()
    game_higher_lower()
  else:
    next_game = False