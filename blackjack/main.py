import random

cards = [("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10), ("Jack", 10), ("Queen", 10), ("King", 10), ("Ace", 11)]
cards = cards * 4

deck_player = []
chips_player = 100
deck_dealer = []

check = None
def deal_cards():
    for h in range(2):
        h = random.choice(cards)
        cards.remove(h)
        deck_player.append(h)
    for g in range(2):
        g = random.choice(cards)
        cards.remove(g)
        deck_dealer.append(g)
    print(f'Deck Player {deck_player} --> {player_calculate(deck_player)}')
    print(f'Karten des Dielers: {deck_dealer[0]}')
first_run = True
def player_calculate(list):

    total = 0
    for card, value in list:
        if value == 11 and card == "Ace" and not first_run:
            inp = int(input("11 oder 1?"))
            index = deck_player.index(("Ace", 11))
            deck_player[index] = ("ace", inp)
            value = inp
        total += value
    first_run = False
    return total
def dealer_calculate(list):
    total = 0
    for card, value in list:
        total += value
    return total

def play():
    print(chips_player)
    #stake = input("Wie viele chips?:")
    deal_cards()

    while player_calculate(deck_player) <= 21 or dealer_calculate(deck_dealer) <= 16:
        anwser = input("noch eine Karte austeilen? y/n")
        if anwser == "y":
            card = random.choice(cards)
            cards.remove(card)
            deck_player.append(card)
            print(f'Deck Player {deck_player}')
            if player_calculate(deck_player) > 21:
                print("Der Dealer hat gewonnen!")
                break
        else:
            while player_calculate(deck_player) <= 21 or dealer_calculate(deck_dealer) <= 16:
                if dealer_calculate(deck_dealer) < 16:
                    card = random.choice(cards)
                    cards.remove(card)
                    deck_dealer.append(card)
                    print(f'Deck Dealer: {deck_dealer} --> {dealer_calculate(deck_dealer)}')
                    if dealer_calculate(deck_dealer) > 21:
                        print("Du hast gewonnen!")
                        print(f'Deck Player {deck_player} --> {player_calculate(deck_player)}')
                        print(f'Deck Dealer {deck_dealer} --> {dealer_calculate(deck_dealer)}')
                        break
                else:
                    if dealer_calculate(deck_dealer) > player_calculate(deck_player):
                        print("Der Dealer hat Gewonnen!")
                        print(f'Deck Player {deck_player} --> {player_calculate(deck_player)}')
                        print(f'Deck Dealer {deck_dealer} --> {dealer_calculate(deck_dealer)}')
                        break
                    elif dealer_calculate(deck_dealer) == player_calculate(deck_player):
                        print("Gleichstand")
                        print(f'Deck Player {deck_player} --> {player_calculate(deck_player)}')
                        print(f'Deck Dealer {deck_dealer} --> {dealer_calculate(deck_dealer)}')
                        break
                    else:
                        print("Du hast gewonnen!")
                        print(f'Deck Player {deck_player} --> {player_calculate(deck_player)}')
                        print(f'Deck Dealer {deck_dealer} --> {dealer_calculate(deck_dealer)}')
                        break
            break

def new_Game():
    for i in deck_dealer.copy():
        cards.append(i)
        deck_dealer.remove(i)
    for i in deck_player.copy():
        cards.append(i)
        deck_player.remove(i)

def main():
    while input("Spielen?y/n") != "n":
        global check
        check = 0
        play()
        new_Game()



if __name__ == "__main__":
    main()
