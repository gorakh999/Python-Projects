<<<<<<< HEAD
import  random
import art
import replit

def deal_cards():
    '''This Function returns a random Card'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''This Function takes list of card as input and return the sum of cards'''
    # This means that it is a blackjack
    if (sum(cards) == 21 and len(cards) == 2):
        return 0
    
    # if there is an ACE and sum is over 21 then we count ACE as 1
    if (11 in cards and sum(cards) > 21):
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score, comp_score):
    
    if (user_score > 21 and comp_score > 21):
        return "You went over, You Loose"

    elif (user_score == comp_score):
        return "Draw"
    
    elif (comp_score == 0):
        return "You Loose, Opponent has BlackJack"

    elif (user_score == 0):
        return "You Win with BlackJack"

    elif (user_score > 21):
        return "You went over, You Loose"
    
    elif (comp_score > 21):
        return "Opponent went over, you Win"

    elif (user_score > comp_score):
        return "You Win"
    
    else:
        return "You Loose"

def play_game():
    print(art.logo)

    user_cards = []
    comp_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"Your Cards {user_cards}. Current Score : {user_score}")
        print(f"Computer First Card : {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True

        else:
            a = input("Type 'y' to get another card, 'n' to pass : ")
            if (a == 'y'):
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_cards())
        comp_score = calculate_score(comp_cards)

    print(f"Your Final Hand: {user_cards}. Final Score : {user_score}")
    print(f"Computers Final Score : {comp_cards}. Final Score : {comp_score}")
    print(compare_score(user_score, comp_score))
            

def main():
    
    while (True):
        print("Would You Like to Play BlackJack Game ? Type 'y' to Continue, 'n' to exit : ")
        opt = input()

        if (opt.lower() == 'y'):
            replit.clear()
            play_game()

        elif (opt.lower() == 'n'):
            break

        else:
            print("Input is Wrong, Try Again")

if __name__ == '__main__':
    main()
=======
import  random
import art
import replit

def deal_cards():
    '''This Function returns a random Card'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''This Function takes list of card as input and return the sum of cards'''
    # This means that it is a blackjack
    if (sum(cards) == 21 and len(cards) == 2):
        return 0
    
    # if there is an ACE and sum is over 21 then we count ACE as 1
    if (11 in cards and sum(cards) > 21):
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score, comp_score):
    
    if (user_score > 21 and comp_score > 21):
        return "You went over, You Loose"

    elif (user_score == comp_score):
        return "Draw"
    
    elif (comp_score == 0):
        return "You Loose, Opponent has BlackJack"

    elif (user_score == 0):
        return "You Win with BlackJack"

    elif (user_score > 21):
        return "You went over, You Loose"
    
    elif (comp_score > 21):
        return "Opponent went over, you Win"

    elif (user_score > comp_score):
        return "You Win"
    
    else:
        return "You Loose"

def play_game():
    print(art.logo)

    user_cards = []
    comp_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"Your Cards {user_cards}. Current Score : {user_score}")
        print(f"Computer First Card : {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True

        else:
            a = input("Type 'y' to get another card, 'n' to pass : ")
            if (a == 'y'):
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_cards())
        comp_score = calculate_score(comp_cards)

    print(f"Your Final Hand: {user_cards}. Final Score : {user_score}")
    print(f"Computers Final Score : {comp_cards}. Final Score : {comp_score}")
    print(compare_score(user_score, comp_score))
            

def main():
    
    while (True):
        print("Would You Like to Play BlackJack Game ? Type 'y' to Continue, 'n' to exit : ")
        opt = input()

        if (opt.lower() == 'y'):
            replit.clear()
            play_game()

        elif (opt.lower() == 'n'):
            break

        else:
            print("Input is Wrong, Try Again")

if __name__ == '__main__':
    main()
>>>>>>> 251004b38adf8cf83ca0859cbca8edd9e63482a0
    