import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  """Deals new randomly chosen card"""
  new_card = random.choice(cards)
  return new_card

def calculate_score(cards_delt):
  """"Checks for blackjack, calculates score, converts ace to one if over 21"""
  if cards_delt == [10, 11] or cards_delt == [11, 10]:
    return 0
  if 11 in cards_delt and sum(cards_delt) > 21:
      cards_delt.remove(11)
      cards_delt.append(1)
  return sum(cards_delt)
    
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw"
  elif computer_score == 0:
    return "Computer has blackjack, You lose!"
  elif user_score == 0:
    return "BlackJack, You win!"
  elif user_score > 21:
    return f"Bust, you lose with a score of {user_score}" 
  elif computer_score > 21:
    return f"Computer busts with a score of {computer_score}, You Win!"
  elif user_score < computer_score:
    return f"Computer has {computer_score}, you have {user_score}, computer wins"  
  else:
    return f"You have {user_score}, computer has {computer_score}, YOU WIN"
  

continue_playing = True

while continue_playing:
  user_cards = []
  computer_cards = []
  for i in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)  
  print(f'You have {user_cards} with a total score of {user_score}')
  print(f'The computer has [{computer_cards[0]}]')
  
  while user_score <= 21 and user_score != 0:
    hit = input('Do you want another card? Y/N: ')
    if hit == "Y" or hit == "y":
      user_cards.append(deal_card())
      user_score = calculate_score(user_cards)
      print(f"You have {user_cards} with a total score of {user_score}")
    else:
      break
  
  while computer_score < 17 and user_score <= 21:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    print(f'Computer draws a card, computer has {computer_cards} totalling {computer_score}')
  
  print(compare(user_score, computer_score))
  
  fortsette = input('Do you want to play again? Y/N: ')
  if fortsette == "y" or fortsette == "Y":
    continue_playing = True
  else:
    print('Thank you for playing!')
    break
  

  

      






