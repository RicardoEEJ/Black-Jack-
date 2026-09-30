"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """
    card_value = 0
    face_cards = ['J','Q','K']
    ace = ['A']
    numbers =  ['2','3','4','5','6','7','8','9','10']
    
    if card in face_cards:
        card_value = 10
        return card_value
    if card in ace:
        card_value = 1
        return card_value
    if card in numbers:
        return int(card)
    return None



def higher_card(
                card_one:str, 
                card_two: str) -> str | tuple:
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    if (value_of_card(card_one) 
        > 
        value_of_card(card_two)): 
        return card_one
    
    if (value_of_card(card_two) 
        > 
        value_of_card(card_one)):
        return card_two
    
    return (card_one, card_two)
#print (higher_card('J','10'))


def value_of_ace(
                 card_one: str, 
                 card_two: str)-> int:
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """    
    ace = ['A']
    if card_one in ace or card_two in ace:
        return 1
    if  value_of_card(card_one) + value_of_card(card_two) < 11  :
        return 11
    return 1
   


def is_blackjack(
                 card_one, 
                 card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """
    blackjack = False
    ace = 'A'

    if card_one == 'A' and card_two == 'A':
        return blackjack
    if card_one in ace or card_two in ace:
        if card_one == 'A':
            card_one = 11
            if card_one + value_of_card(card_two) == 21:
                blackjack = True
                return blackjack
        if card_two == 'A':
            card_two = 11
            if card_two + value_of_card(card_one) == 21:
                blackjack = True
                return blackjack

    return blackjack

print (is_blackjack('A', 'A'))

def can_split_pairs(
        card_one: str, 
        card_two:str)->bool:
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    split = False
    if (
        value_of_card(card_one) 
        == 
        value_of_card(card_two) 
        or         
        value_of_card(card_two) 
        ==
        value_of_card(card_one)
        ): 
        split = True
        return split
    
    return split

print (can_split_pairs('A','A'))   


def can_double_down(
        card_one: str, 
        card_two: str)-> bool:
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    double_down = [9,10,11]
    if value_of_card(card_one) + value_of_card(card_two) in double_down:
        return True
    return False
print (can_double_down('4','5'))
    
