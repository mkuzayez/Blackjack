import random


def blackjack():

    print('''
                                                                                   
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  
    
''')

    start = input('Type "S" to start playing Blackjack, or any other key to abort\n').lower()
    if not start == 's':
        return print('Aborted')


    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    computers_cards = [random.choice(cards), random.choice(cards)]
    users_cards = [random.choice(cards), random.choice(cards)]


    if sum(users_cards) == 21:
        return print('You have a Blackjack. You Won.')
    elif sum(computers_cards) == 21:
        return print('Computer has a Blackjack. You lost.')
# no Blackjack:

    if sum(users_cards) > 21 and (1 not in users_cards or 11 not in users_cards):
        return print('You lost.')
    if sum(users_cards) > 21 and 11 in users_cards:
        temp = users_cards.index(11)
        users_cards[temp] = 1
        if sum(users_cards) > 21:
            return print('You lost.')


    print(f'''
Computer's cards are: {computers_cards[0]}, X.
Your cards are: {users_cards[0]}, {users_cards[1]}. with a sum of {sum(users_cards)}
''')



    while input('Type "h" for hit, or any other key for Stand\n').lower() == 'h':

        users_cards.append(random.choice(cards))
        if sum(users_cards) == 21:
            return print('Your cards now are: ' + ', '.join(str(i) for i in users_cards) + f' with a sum of {sum(users_cards)}. Blackjack.\nYou won.')

        elif sum(users_cards) < 21:
            print('Your cards now are: ' + ', '.join(str(i) for i in users_cards) + f'. with a sum of {sum(users_cards)}')

        elif sum(users_cards) > 21:
            return print('Your cards now are: ' + ', '.join(str(i) for i in users_cards) + f'. with a sum of {sum(users_cards)}, which is over 21.\nYou lost.')


    while sum(computers_cards) < 17:
        print('Computer\'s cards are: ' + ', '.join(str(i) for i in computers_cards) + f'. with a sum of {sum(computers_cards)}' + '.\nComputer will hit.')
        computers_cards.append(random.choice(cards))

    if sum(computers_cards) > 21:
        return print('Computer\'s cards are: ' + ', '.join(str(i) for i in computers_cards) + f'. with a sum of {sum(computers_cards)}.\n\nIt\'s a bust. You won')


    if sum(users_cards) > sum(computers_cards):
        return print('Computer\'s cards are: ' + ', '.join(str(i) for i in computers_cards) + f'. with a sum of {sum(computers_cards)}.\n\nYou won.')

    elif sum(users_cards) == sum(computers_cards):
        return print('Computer\'s cards are: ' + ', '.join(str(i) for i in computers_cards) + f'. with a sum of {sum(computers_cards)}.\n\nIt\'s a draw.')

    elif sum(users_cards) < sum(computers_cards):
        return print('Computer\'s cards are: ' + ', '.join(str(i) for i in computers_cards) + f'. with a sum of {sum(computers_cards)}.\n\nYou lost.')




blackjack()

while input('Do you want to play again? type "s" to start again, or any other key to cancel.\n').lower() == 's':
    blackjack()
