'''
Hutchinson's Omaha Hi/Lo Point System (Starting Hand Strength)
High hand (play it as 20pt): 10+ lowest card AND
One of following: (Pair and suited)  or (2 pair) or (double suited)

Creator: Brian Ho (plush424)
'''

# A = 1, J = 11, Q=12, K=13, for the sake of this program

def main():
    starting_hand = input("Input hand: ")
    lst_hand = Convert(starting_hand)
    points = step_1(lst_hand)
    points = step_2(lst_hand, points)
    points = step_3(lst_hand, points)
    points = step_4(lst_hand, points)
    play = ""
    if points >= 30:
        play = ".. Consider raising this hand"
    elif points >= 20:
        play = ".. Play this hand"
    else:
        play = ".. Probably fold"
    print("Point total: " + str(points) + play)


def Convert(string):
    li = list(string.split(" "))
    return li

def step_1(list_of_cards): #list of strings As
    points = 0
    x = list_of_cards[0][0]
    y = list_of_cards[1][0]
    if x == y:
        y = list_of_cards[2][0]
    if x == y:
        y = list_of_cards[3][0]

    if x == "A":
        if y == "2":
            points +=20
        elif y == "3":
            points += 17
        elif y == "4":
            points += 13
        elif y == 5:
            points += 10

    elif x == "2":
        if y == "3":
            points += 15
        elif y == "4":
            points += 12

    elif x == "3":
        if y == "4":
            points += 11

    elif x == "4":
        if y == "5":
            points += 8
    return points

def step_2(list_of_cards, points):
    x = list_of_cards[0][0]
    y = list_of_cards[1][0]
    if x == y:
        y = list_of_cards[2][0]
    if x == y:
        y = list_of_cards[3][0]

    for i in range(len(list_of_cards)):
        if x != list_of_cards[i][0] and y != list_of_cards[i][0]:
            z = list_of_cards[i][0]
            if z == "3":
                points += 9
            if z == "4":
                points += 6
            if z == "5":
                points += 4
            if z == "J" or z == "Q" or z == "K":
                points += 2
            if z == "6" or z == "10":
                points += 1
    return points



def step_3(list_of_cards, points):
    x = list_of_cards[0][0]
    y = list_of_cards[1][0]
    z = list_of_cards[2][0]
    a = list_of_cards[3][0]
    lst_value_only = [x,y,z,a]
    step_3_points = 0
    if x == y:
        if x == "A":
            step_3_points += 8
        elif x == "K":
            step_3_points += 6
        elif x == "Q":
            step_3_points += 5
        elif x == "J":
            step_3_points += 2
        elif x == "10" or x == "4" or x == "3":
            step_3_points += 1
        elif x == "2":
            step_3_points += 3
        if y == z:
            step_3_points = (step_3_points)/2
        if y == a:
            step_3_points = (step_3_points)/2

    elif y == z:
        if y == "A":
            step_3_points += 8
        elif y == "K":
            step_3_points += 6
        elif y == "Q":
            step_3_points += 5
        elif y == "J":
            step_3_points += 2
        elif y == "10" or y == "4" or y == "3":
            step_3_points += 1
        elif y == "2":
            step_3_points += 3
        if  z == a:
            step_3_points = (step_3_points)/2

    if y != z and z == a:
        if z == "A":
            step_3_points += 8
        elif z == "K":
            step_3_points += 6
        elif z == "Q":
            step_3_points += 5
        elif z == "J":
            step_3_points += 2
        elif z == "10" or z == "4" or z == "3":
            step_3_points += 1
        elif z == "2":
            step_3_points += 3
    points += step_3_points
    return points

def step_4(list_of_cards, points):
    step_4_points = 0
    club = []
    diamond = []
    heart = []
    spade = []
    all_suits = [club, diamond, heart, spade]
    for card in list_of_cards:
        if card[1] == "c":
            club.append(card[0])
        elif card[1] == "d":
            diamond.append(card[0])
        elif card[1] == "h":
            heart.append(card[0])
        elif card[1] == "s":
            spade.append(card[0])

    for suit in all_suits:
        if len(suit) == 2 or len(suit) == 3:
            suit_points = 0
            card_value = 0
            for card in suit:
                if card == "A":
                    card_value = 4
                elif card == "K":
                    card_value = 3
                elif card == "Q" or card == "J":
                    card_value = 2
                elif card == "8" or card == "9" or card == "10":
                    card_value = 1
                if card_value > suit_points:
                    suit_points = card_value

            if len(suit) == 3:
                suit_points = suit_points/2
            step_4_points += suit_points
    points += step_4_points
    return points




main()

