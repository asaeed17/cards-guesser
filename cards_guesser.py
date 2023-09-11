import sqlite3
from random import randint
from time import time

conn = sqlite3.connect("computer_cards.db")

def insert_picked(name):
    insert_sql = "INSERT INTO picked(name, time) VALUES ('{}', {})".format(name, time())
    conn.execute(insert_sql)
    conn.commit()

def read_last_picked():
    result = conn.execute("SELECT * FROM picked ORDER BY time DESC")
    return result.fetchone()

def read_all_cards():
    result = conn.execute("SELECT * FROM computer")
    return result.fetchall()

def pick_card():
    cards = read_all_cards()
    last_picked_card = read_last_picked()
    # print("lp tuple: ", last_picked_card)
    # print("lp card name string : ", last_picked_card[0])

    random_card = cards[randint(0, len(cards) - 1)]
    # print("rc tuple: ", random_card)

    #keep shuffling until the random card isn't the last picked card
    while random_card[0] == last_picked_card[0]:
        random_card = cards[randint(0, len(cards) - 1)]

    insert_picked(random_card[0])
    return random_card


player = input("Are you player (1) or (2) > ")
choosing_player = "1"

player1_score = player2_score = 0

for round in range(5):
    input("Press enter to pick a card when both players are ready > ")

    card = pick_card()
    card_text = f"{card[0]}, cores={card[1]}, speed={card[2]}GHz, RAM={card[3]}MB, cost={card[4]}$"
    print(card_text)

    print("Player " + choosing_player + " picks.")

    winner = input(f"Did you (player {player}) win? (Y)es, (N)o, (D)raw >").lower()

    if winner == "y" or winner == "n":
        if winner == "y":
            choosing_player = player
        elif winner == "n":
            choosing_player = "2" if player == "1" else "1"

        #update score
        if choosing_player == "1" :
            player1_score += 1
        elif choosing_player == "2":
            player2_score += 1

if player1_score > player2_score:
    print(f"Player 1 won with {player1_score} score!")
    print(f"Player 2's score: {player2_score}")
else:
    print(f"Player 2 won with {player2_score} score!")
    print(f"Player 1's score: {player1_score}")

conn.close()
