from deck_of_cards import deck_of_cards

human_cards = [] #human will get 2 cards afterwards
comp_cards = [] #comp will get 2 cards afterwards
flop = [] #will get a card if both players check
river = [] #will get another card

deck_obj = deck_of_cards.DeckOfCards()
deck_obj.shuffle_deck()

##.name is a function used to print card's name as a string##
print("Player 1 cards: ")
for i in range(2): #giving cards to human
    human_cards.append(deck_obj.give_random_card())
    print(human_cards[i].name)

print("\nPlayer 2 cards: ")
for j in range(2): #giving cards to computer
    comp_cards.append((deck_obj.give_random_card()))
    print(comp_cards[j].name)

print("\nPLAYER 1:")
check1 = input("Check(c) or Fold(f): ")
if check1 == 'c':
    flop.append(deck_obj.give_first_card())
    print("Flop: ", flop[0].name)

print("\nPLAYER 2:")
check2 = input("Check(c) or Fold(f): ")
if check2 == 'c':
    flop.append(deck_obj.give_first_card())
    print("River: ",  flop[1].name)

# print(human_card[0].suit)
# print(human_card[1].rank)
