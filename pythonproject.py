import random

   

while True:
  player_choice = input ( 'ENTER AN ACTION (rock, paper, scissors)')
  possible_choices = ['rock', 'paper' , 'scissors']
  system_choice = random.choice(possible_choices)
  print(f'You chose {player_choice}  ,  and the computer chose {system_choice}')

  if player_choice == system_choice:
    print(f'You both selected {system_choice} Then it is a tie')

  elif player_choice == 'rock' and system_choice == 'paper':
     print('You loose!!!!')

  elif player_choice == 'rock' and system_choice == 'scissors':
    print('You win!!!!')

  elif player_choice == 'paper' and system_choice == 'rock':
    print('You win!!!!')

  elif player_choice == 'paper' and system_choice == 'scissors':
    print('You loose!!!!')

  elif player_choice == 'scissors' and system_choice == 'rock':
    print('You Loose!!!!')

  elif player_choice == 'scissors' and system_choice == 'paper':
    print('You win!!!!')

  play_again = input ('Do you want to play again? (yes/no)')
  if play_again.lower() != 'yes':
   break


    
     