import random

def get_choices():
    player_choice = input('Choose rock, paper or scissors by typing R, P or S.')
    p_choice = player_choice.lower()
    if p_choice == 'r':
        player_choice = 'rock'
    elif p_choice == 'p':
        player_choice = 'paper'
    elif p_choice == 's':
        player_choice = 'scissors'
    else:
        return "Invalid Choice"
    choice_list = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choice_list)
    choices = {'player_choice': player_choice, 'computer_choice': computer_choice}
    
    return choices

choice = get_choices()

def get_winner(listy):
    player_value = 0
    computer_value = 0
    choice_list = ['rock', 'paper', 'scissors']
    for i in range(len(choice_list)):
        if listy[0] == choice_list[i]:
            player_value = i
        if listy[1] == choice_list[i]:
            computer_value = i
    difference = player_value - computer_value
    if player_value == computer_value:
        return 'It\'s a tie.'
    elif abs(difference) == 2:
        if difference < 0:
            return "Player wins!"
        else:
            return "Computer wins!"
    elif abs(difference) == 1:
        if difference < 0:
            return "Computer wins!"
        else:
            return "Player wins!"
        
conclusion = get_winner(list(choice.values()))


print(choice)
print(conclusion)
