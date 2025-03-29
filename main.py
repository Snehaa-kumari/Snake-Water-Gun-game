import random

def game_win(comp, you):
    if comp == you:
        return None
    elif (comp == 's' and you == 'w') or (comp == 'w' and you == 'g') or (comp == 'g' and you == 's'):
        return False  
    else:
        return True  

choices = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}

while True:  
    print("\nComputer Turn: Snake (s), Water (w), or Gun (g)..?")

    comp = random.choice(['s', 'w', 'g'])

    while True:
        you = input("\nYour Turn: Snake (s), Water (w), or Gun (g)?\n\tEnter Your Choice: ")
        if you in ['s', 'w', 'g']:
            break
        print(" Invalid input! Please enter 's', 'w', or 'g'.")

    result = game_win(comp, you)

    print(f"\n Computer chose: {choices[comp]}")
    print(f" You chose: {choices[you]}")

    if result is None:
        print("\n It's a Tie!")
    elif result:
        print("\n Congratulations, You Won! ")
    else:
        print("\n You Lost! Better Luck Next Time...")

    while True:
        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again in ['y', 'n']:
            break
        print("Invalid input! Please enter 'y' to play again or 'n' to exit.")

    if play_again != 'y':
        print("\nThanks for playing! See you next time! ")
        break
