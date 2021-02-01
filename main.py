import random

def new_card():
  card = random.randint(1, 14)
  if card > 10:
    card = 10
  return card


continue_playing = True

while continue_playing:
  computer_cards = []
  player_cards = []
  for i in range(2):
    player_cards.append(new_card())
  computer_cards.append(new_card())
  print(f"You have {player_cards}, totalling {sum(player_cards)}")
  print(f"The computer has {computer_cards}")
  hitting = True
  while hitting == True:
    hit = input('Would you like another card? Y/N: ')
    if hit == "Y" or hit == "y":
      player_cards.append(new_card())
      print(f"You have {player_cards} totalling {sum(player_cards)}")
    else:
      hitting = False