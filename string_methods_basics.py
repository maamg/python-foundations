import random

user_card = []
computer_card = []
is_game_over = False


def deal_card(user):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user.extend(random.sample(cards, 1))


def calculate_score(cardList):
    if len(cardList) == 2 and sum(cardList) == 21:
        return 0
    else:
        return sum(cardList)


def compare(user, computer):
    if calculate_score(user) > calculate_score(computer):
        print(f" Your card: [{user} and your score: {sum(user)} ")
        print(f" Computer's card: [{computer}] and computer's score:{sum(computer)}")
        print("You won the game")
    elif calculate_score(user) < calculate_score(computer):
        print(f" Your card: [{user} and your score: {sum(user)} ")
        print(f" Computer's card: [{computer}] and computer's score:{sum(computer)}")
        print("You lost the game")
    else:
        print(f" Your card: [{user} and your score: {sum(user)} ")
        print(f" Computer's card: [{computer}] and computer's score:{sum(computer)}")
        print("It's Tie")


def play_game():
    global is_game_over
    if not is_game_over:
        first_agreement = input("Do you want to play Black-Jack.Type 'y' to play and type 'n' to exit\n")
        if first_agreement == 'y':
            deal_card(user_card)
            deal_card(computer_card)
            deal_card(user_card)
            deal_card(computer_card)
            if calculate_score(user_card) == 0 and calculate_score(computer_card) ==0:
                print(f"You have the Black-Jack [{user_card}] first! You win")
            elif calculate_score(user_card) == 0 and calculate_score(computer_card) != 0:
                print(f"You have the Black-Jacket{user_card}.Computer win")
            elif calculate_score(user_card) != 0 and calculate_score(computer_card) == 0:
                print(f'Computer has the Black Jacket {computer_card}. Computer won the game')
            else:
                print(f" Your card is {user_card} and computer's first card is [{computer_card[0]}]")
                while first_agreement == 'y':
                    agreement = input("Type 'y' to get another card, type 'n' to pass:\n")
                    if agreement == "y":
                        deal_card(user_card)
                        print(f"Your card is {user_card}, and your score is {calculate_score(user_card)} ")
                        if calculate_score(user_card) == 21:
                            print("Yes! You have got the Black-Jack")
                            is_game_over = True
                        elif calculate_score(user_card) < 21:
                            first_agreement = 'y'
                        else:
                            print("You have exceed 21!")
                            first_agreement = 'n'
                            is_game_over = True
                    else:
                        first_agreement = False
                        print("agreement = 'n'")

                while calculate_score(computer_card) < 17:
                    deal_card(computer_card)
                    is_game_over = False

                if calculate_score(computer_card) > 21:
                    print(f"Computer exceed score 21. Computer's card :{computer_card} and computer score is: [{calculate_score(computer_card)}]")
                    is_game_over = True

                else:
                    if calculate_score(user_card) > calculate_score(computer_card):
                        print(f"Your card is {user_card} and score: [{calculate_score(user_card)}]")
                        print(f"Computer card is {computer_card} and score: [{calculate_score(computer_card)}]")
                        print(" You won the game")
                        is_game_over = True

                    elif calculate_score(user_card) < calculate_score(computer_card):
                        print(f"Your card is {user_card} and score: [{calculate_score(user_card)}]")
                        print(f"Computer card is {computer_card} and score: [{calculate_score(computer_card)}]")
                        print(" You lost the game")
                        is_game_over = True

                    elif calculate_score(user_card) == calculate_score(computer_card):
                        print(f"Your card is {user_card} and score: [{calculate_score(user_card)}]")
                        print(f"Computer card is {computer_card} and score: [{calculate_score(computer_card)}]")
                        print(" It's a draw")
                        is_game_over = True


play_game()





