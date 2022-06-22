############### Blackjack Project #####################

import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack_score = 21

print(logo)
wanna_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")


def ace_check(cards_list):
    score = 0
    for card in cards_list:
        if card == 11:
            if score + card > 21:
                score += 1
            else:
                score += 11
        else:
            score += card
    return score


while wanna_play == 'y':
    computer_cards = random.sample(cards, 2)
    user_cards = random.sample(cards, 2)

    computer_score = ace_check(computer_cards)
    user_score = ace_check(user_cards)

    print(f"your cards: {user_cards}, current score: {user_score}")
    print(f"Computers first card: {computer_cards[0]}")

    if computer_score == blackjack_score:
        print("computer wins!")
        wanna_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
        continue
    elif user_score == blackjack_score:
        print("You win!")
        wanna_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
        continue

    next_draw = input("Type 'y' to get another card, type 'n' to pass:")

    while next_draw == 'y':
        user_cards.append(random.choice(cards))
        user_score = ace_check(user_cards)
        print(f"your cards: {user_cards}, current score: {user_score}")
        print(f"Computers first card: {computer_cards[0]}")

        if user_score > blackjack_score:
            print("computer wins!")
            break
        elif user_score == blackjack_score:
            print("You win!")
            break

        wanna_next_draw = input("Type 'y' to get another card, type 'n' to pass:")

        while wanna_next_draw == 'n':
            if user_score > 16:
                next_draw = 'n'
                break
            print("You have to take cards till your score is above 16")
            wanna_next_draw = input("Type 'y' to get another card, type 'n' to pass:")

    while computer_score < blackjack_score and (user_score < blackjack_score or next_draw == 'n'):
        computer_cards.append(random.choice(cards))
        computer_score = ace_check(computer_cards)

        if blackjack_score >= computer_score > user_score:
            print("computer wins!")
            break
        elif computer_score > blackjack_score:
            print("You win!")
            break

    print(f"your cards: {user_cards}, current score: {user_score}")
    print(f"Computers  card: {computer_cards}, computer score: {computer_score}")

    wanna_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    if wanna_play == "y":
        os.system('clear')
        print(logo)

print("Good bye! see you soon")