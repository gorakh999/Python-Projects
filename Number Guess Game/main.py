import art
import random
import replit

def generate_number():
    '''Reutrns a Randomly Generated Number'''
    number = random.randint(1, 101)
    return number

def play_game():
    replit.clear()
    print(art.logo)
    print("I am thinking of a Number between 1 and 100.")
    generated_number = generate_number()
    difficulty = input("Choose a Difficulty. Type 'easy' or 'hard' Default is 'Easy' : ")
    if difficulty.lower() == 'hard':
        no_of_attempts = 5
    else:
        no_of_attempts = 10

    while(1):

        if (no_of_attempts == 0):
            print("You do not have Any Attempts Remaining")
            print("Thank You for Playing.")
            break

        print(f"You have {no_of_attempts} attempts remaining to guess the number.")
        number = int(input("Make a Guess : "))
        
        no_of_attempts -= 1
        if (number > generated_number):
            print("Too High")
        elif (number < generated_number):
            print("Too Low")
        else:
            print(f"You got it. The Answer is {generated_number}")
            break
    
    a = input("Do you want to Play Again ? : Type 'y' for yes, 'n' for No : ")
    if (a == 'y'):
        replit.clear()
        play_game()
    else:
        print("Thank You")
        return

if __name__ == '__main__':
    play_game()

