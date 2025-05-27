from random import choice
import art

def coin():
    """ask the player if they want to play again."""
    answer = input("play again? y/n: ")
    if answer == "y":
        return True
    else:
        return False

def ace_rule(hand):
    """cheks if there's 11 in the hand, and if the score > 21, changes it to 1."""
    if 11 in hand:
        if sum(hand) > 21:
            location_in_hand = hand.index(11)
            hand[location_in_hand] = 1
    return hand

def state (ph, ps, dh, ds):
    """returns a string describing the current hands and scores of players."""
    message = f"Your hand: {ph} score: {ps}.\nDealer's hand: {dh} score: {ds}."
    return message

def draw_sequence (hand, score):
    """3 actions: add card, check ACE rule, update the score, returns the updated score."""
    hand.append(choice(cards))
    hand = ace_rule(hand)
    score = sum(hand)
    return score

def win_check (ps,ds):
    """takes the scores as input and return an int representing who wins."""
    player_wins = 1
    draw = 0
    dealer_wins = -1

    if ps == 21:
        print("You WIN!")
        return player_wins

    p_diff = 21 - ps
    d_diff = 21 - ds

    if d_diff == p_diff:
        print ("Draw!")
        return draw

    elif p_diff < d_diff or d_diff < 0:
        print ("You WIN!")
        return player_wins

    else:
        print ("You LOSE!")
        return dealer_wins

def blackjack(ph, dh):
    if dh == [11, 10] or dh == [10, 11]:
        print(f"The dealer has BLACK JACK!\n{dh}\nYou LOSE.")
        return True

    if ph == [11, 10] or ph == [10, 11]:
        print(f"You have BLACK JACK!\n{ph}\nYou WIN.")
        return True
    else:
        return False


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
keep_playing = True

while keep_playing:

    print (art.logo)
    print ("welcome, let the game begin.")

    # set all hands and scores to 0.
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0

    #deal cards 1st round
    for time in range(2):
        player_hand.append(choice(cards))
        dealer_hand.append(choice(cards))

    #calc current score
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)

    if blackjack(player_hand, dealer_hand):
        print(state(player_hand, player_score, dealer_hand, dealer_score))
        keep_playing = coin()

    #print current scores and ask if cont
    print (state(player_hand, player_score, dealer_hand[0], dealer_score - dealer_hand[1]))
    hit = input ("hit me? Y or N: \n").lower()

    # if the user continue
    while hit == "y":
        print ("you hit y")
        player_score = draw_sequence(player_hand, player_score)
        print(state(player_hand, player_score, dealer_hand[0], dealer_score - dealer_hand[1]))

        if player_score == 21:
            print ("You WIN! Lucky")
            keep_playing = coin()
            break
        elif player_score > 21:
            print("You LOSE! Too greedy.")
            keep_playing = coin()
            break
        else:
            hit = input("hit me? Y or N: \n").lower()

    # if the user won't continue
    if hit == "n":
        print ("you hit n.\nThe dealer's hand is:")
        print(state(player_hand, player_score, dealer_hand, dealer_score))

        if dealer_score < 17:
            print ("dealer got a score lesser than 17, so he draws a card:")
            dealer_score = draw_sequence(dealer_hand, dealer_score)
            print(state(player_hand, player_score, dealer_hand, dealer_score))

        win_check (player_score, dealer_score)
        keep_playing = coin()

    # in case of bad input
    elif hit != "y" and hit != "n":
        print ("invalid input.")

print ("Game ended.")
