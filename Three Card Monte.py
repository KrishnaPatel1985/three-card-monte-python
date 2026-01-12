import random
def main():
    money = 100
    print("-Three Card Monte-")
    print("Find the queen to double your bet!")
    while money>0:
        print(f"You have ${money}")

        while True:
            bet_input = input("How much you wanna bet?")
            try:
                bet = int(bet_input)
            except ValueError:
                print("Invalid input - should be an integer.")
                continue
            if bet < 1 or bet > money:
                print(f"Invalid input - should be within range 1-{money}.")
                continue
            break
        
        queen_location = random.randint(1,3)

        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  1  | |  2  | |  3  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")

        while True:
            user_input = input("Find the queen: ")
            try:
                user = int(user_input)
            except ValueError:
                print("Invalid input - should be an integer.")
                continue
            if user < 1 or user > 3:
                print("Invalid input - should be within range 1-3")
                continue
            break
        card1 = 'Q' if queen_location == 1 else 'K'
        card2 = 'Q' if queen_location == 2 else 'K'
        card3 = 'Q' if queen_location == 3 else 'K'

        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print(f"|  {card1}  | |  {card2}  | |  {card3}  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")

        if user == queen_location:
            money+=bet
            print("You got lucky this time...")
        else:
            money-=bet
            print("Sorry... you lose.")

        if money<=0:
            print("You're out of money. Beat it loser!")
            break
        while True:
            play_again = input("Play again? (Y/N) : ").strip().lower()
            if play_again not in ['y','n']:
                print("Invalid input must be - Y or N. ")
                continue
            break
        if play_again == 'n':
            break

    print("Thanks for playing")
if __name__ == "__main__":
    main()
