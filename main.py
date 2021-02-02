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
  if sum(player_cards) <=21:
    continue
  else:
    print('YOU LOSE')
  while sum(computer_cards) < 21:
    computer_cards.append(new_card())
    print(computer_cards)
  if sum(computer_cards) <= 21:
    continue
  else: 
    print('Dealer busts, You win!')
  if sum(computer_cards) < sum(player_cards):
    print('You Win')
  else:
    print('Dealer wins, You lose')
  ask_repeat = input('Do you want to play again? Y/N: ')
  if ask_repeat == "Y" or ask_repeat == "y":
    continue
  else:
    print("Thanks for playing!")
    continue_playing = False