import random
<<<<<<< d824eb13145d3c147d18e7c02ec13fd57b2f7b25

def print_player(player, player_card):

    print ("player card: %s"%(player))
    print ("player card total: %s"%(player_card))
    print (" ")

def print_dealer(dealer, dealer_card):

    print ("dealer card: %s"%(dealer)).upper()
    print ("dealer card total: %s"%(dealer_card)).upper()
    print (" ")

def print_winner(player, dealer, player_card, dealer_card):

    if player_card == 21:
        print_dealer(dealer, dealer_card)
        print ("Player Wins")
        return True
    elif dealer_card == 21:
        print_dealer(dealer, dealer_card)
        print ("Dealer Wins")
        return True
    elif player_card > 21:
        print_dealer(dealer, dealer_card)
        print ("Dealer Wins")
        return True
    elif dealer_card > 21:
        print_dealer(dealer, dealer_card)
        print ("Player Wins")
        return True
    return False



def card_deck():

    deck = {"clubs": range(1,14), "diamonds": range(1,14), "hearts": range(1,14), "spades": range(1,14)}
    player_card = 0
    player = []
    dealer_card = 0
    dealer = []


    s = set()

    player.append(generate(deck, s))
    player_card += card
    player.append(generate(deck, s))
    player_card += card

    dealer.append(generate(deck, s))
    dealer_card += card
    print_dealer(dealer, dealer_card)
    dealer.append(generate(deck, s))
    dealer_card += card

    print_player(player, player_card)
    print_winner(player, dealer, player_card, dealer_card)

    while True:
        if print_winner(player, dealer, player_card, dealer_card):
            return
        askplayer = raw_input("Do you want to hit or stay?(h/s): ").lower()
        print(" ")
        if askplayer.startswith("h"):
            player.append(generate(deck, s))
            player_card += card
            print_player(player, player_card)

        else:
            break

    while dealer_card < 17 or dealer_card < player_card:
        dealer.append(generate(deck, s))
        dealer_card += card
        if print_winner(player, dealer, player_card, dealer_card):
            return

    print_player(player, player_card)
    p = 21 - player_card
    d = 21 - dealer_card
    if p<d:
        print_dealer(dealer, dealer_card)
        print ("Player Wins")
    elif d<p:
        print_dealer(dealer, dealer_card)
        print ("Dealer Wins")
    else:
        print_dealer(dealer, dealer_card)
        print ("Push")
    return

count = 0
def generate(deck, s):
    global card
    global count
    while True:
        count += 1
        suits = random.choice(deck.keys())
        card = random.choice(deck[suits])
        a = suits + str(card)

        if a not in s:
            s.add(a)
            if card>= 10:
                card = 10
            if card == 1:
                if count == 1 or count == 2:
                    ace = int(raw_input("Player: 1 or 11? "))
                    print(" ")
                    card = ace
                elif count == 3 or count == 4:
                    ace = int(raw_input("Dealer: 1 or 11? "))
                    print (" ")
                    card = ace
                else:
                    ace = int(raw_input("1 or 11? "))
                    print (" ")
                    card = ace

            return a


card_deck()

#corrections
# duplication of cod
# OOP implementation
# bid amount through OOP  concept
# ace for dealer it ll be automatic because of this player could assume dealer's card and concept of shouldn't reveal dealer's card
#    got false
# ace for player could able to change if total goes up 21
# done Dealer card shouldn't reveal
# done if player stay then dealer should take card as per necessary


# 1 deck
# 2 player 2 card and dealer 2 ( and dealer's one card ll be hidden)
=======
def card_deck():
    global deck
    deck = {"clubs": range(1,14), "diamonds": range(1,14), "hearts": range(1,14), "spades": range(1,14)}
    player = []
    computer = []
    count = 0
    player_card = 0
    computer_card = 0
    global s
    global card
    s = set()
    for i in range(1,5):
        generate()
        count += 1
        if count < 3:
            if card == 11 or card == 12 or card == 13:
                card = 10
                player_card += card
            elif card == 1:
                print ("player card: %s"%(player))
                print ("player card total: %s"%(player_card))
                print ("computer card total: %s"%(computer_card))
                ace = int(raw_input("Do you want ace as 1 or 11?"))
                player_card += ace
            else:
                player_card += card
            player.append(a)
        else:
            if card == 11 or card == 12 or card == 13:
                card = 10
                computer_card += card
            elif card == 1:
                print ("computer card: %s"%(computer))
                print ("player card total: %s"%(player_card))
                print ("computer card total: %s"%(computer_card))
                ace = int(raw_input("Do you want ace as 1 or 11?"))
                computer_card += ace
            else:
                computer_card += card
            computer.append(a)
    print ("player card: %s"%(player))
    print ("computer card: %s"%(computer))
    print ("player card total: %s"%(player_card))
    print ("computer card total: %s"%(computer_card))
    if player_card == 21:
        print ("player card: %s"%(player))
        print ("computer card: %s"%(computer))
        print ("player card total: %s"%(player_card))
        print ("computer card total: %s"%(computer_card))
        print ("Player win")
        return
    elif computer_card == 21:
        print ("player card: %s"%(player))
        print ("computer card: %s"%(computer))
        print ("player card total: %s"%(player_card))
        print ("computer card total: %s"%(computer_card))
        print ("Computer win")
        return
    else:
        # askplayer = raw_input("Do you want to hit or stay?(h/s): ").lower()
        show_cards = 0
        while True:
            if show_cards >= 1:
                print ("player card: %s"%(player))
                print ("computer card: %s"%(computer))
                print ("player card total: %s"%(player_card))
                print ("computer card total: %s"%(computer_card))
            askplayer = raw_input("Do you want to hit or stay?(h/s): ").lower()
            if askplayer.startswith("h"):
                generate()
                if card == 11 or card == 12 or card == 13:
                    card = 10
                    player_card += card
                elif card == 1:
                    print ("player card: %s"%(player))
                    print ("player card total: %s"%(player_card))
                    print ("computer card total: %s"%(computer_card))
                    ace = int(raw_input("Do you want ace as 1 or 11?"))
                    player_card += ace
                else:
                    player_card += card
                player.append(a)
                if player_card == 21:
                    print ("player card: %s"%(player))
                    print ("computer card: %s"%(computer))
                    print ("player card total: %s"%(player_card))
                    print ("computer card total: %s"%(computer_card))
                    print ("Player wins")
                    return
                elif player_card > 21:
                    print ("player card: %s"%(player))
                    print ("computer card: %s"%(computer))
                    print ("player card total: %s"%(player_card))
                    print ("computer card total: %s"%(computer_card))
                    print ("Dealer wins")
                    return
                show_cards += 1
            else:
                break
        else:
            while computer_card < 17:
                generate()
                if card == 11 or card == 12 or card == 13:
                    card = 10
                    computer_card += card
                elif card == 1:
                    print ("computer card: %s"%(computer))
                    print ("player card total: %s"%(player_card))
                    print ("computer card total: %s"%(computer_card))
                    ace = int(raw_input("Do you want ace as 1 or 11?"))
                    computer_card += ace
                else:
                    computer_card += card
                computer.append(a)
            if computer_card == 21:
                print ("player card: %s"%(player))
                print ("computer card: %s"%(computer))
                print ("player card total: %s"%(player_card))
                print ("computer card total: %s"%(computer_card))
                print ("Dealer wins")
                return
            elif computer_card > 21:
                print ("player card: %s"%(player))
                print ("computer card: %s"%(computer))
                print ("player card total: %s"%(player_card))
                print ("computer card total: %s"%(computer_card))
                print ("Player wins")
                return

        d1 = 21 - player_card
        d2 = 21 - computer_card
        if d1<d2:
            print ("player card: %s"%(player))
            print ("computer card: %s"%(computer))
            print ("player card total: %s"%(player_card))
            print ("computer card total: %s"%(computer_card))
            print ("Player wins")
            return
        elif d2<d1:
            print ("player card: %s"%(player))
            print ("computer card: %s"%(computer))
            print ("player card total: %s"%(player_card))
            print ("computer card total: %s"%(computer_card))
            print ("Dealer wins")
            return
        else:
            print ("player card: %s"%(player))
            print ("computer card: %s"%(computer))
            print ("player card total: %s"%(player_card))
            print ("computer card total: %s"%(computer_card))
            print ("push")
            return

def generate():
    global card
    while True:
        suits = random.choice(deck.keys())
        card = random.choice(deck[suits])
        global a
        a = suits + str(card)
        if a not in s:
            s.add(a)
            break

card_deck()

# 1 deck
# 2 player 2 card and computer 2 ( and computer's one card ll be hidden)
>>>>>>> blackjack
# 3 that cards ll be store in one set,s o it won't be repeat
# 4 add total of that two cards
# 5 considering total of two cards ask player he wants to hit or stay
# 6 if stay decide win loose or burst
# 7 if hit continue process of total and then check win loose and burst
# 8 and then check amount bet with class
