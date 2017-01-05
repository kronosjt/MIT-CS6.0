# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
    'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # PSEUDOCODE:
    # 1. initialize score to 0
    # 2. if word is empty then score=0
    # 3. else: for each letter in word, use letter as key & extract value from  SCRABBLE_LETTER_VALUES
    # 4. if the lenth of word == n then add bonus 50

    score = 0 # Initialize score

    if len(word) != 0:
        for letter in word:
            score += SCRABBLE_LETTER_VALUES[letter]

    if len(word) == n:
        score += 50 # Bonus 50 for using all letters in the hand

    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # PSEUDOCODE
    # 1. for each letter in word decrement the letter.value in hand

    for letter in word:
        hand[letter] = hand.get(letter) - 1
    return hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # PSEUDOCODE
    # 1. Check if word exists in word_list, else return False
    # 2. For each letter in word check if it exists in hand, else return False
    # 3. If it exists check if the value is != 0 and matches the number of times the letter is used, else return False
    # 4. Account for same letter being used multiple times!! Use get_frequency_dict() to convert word into a dict

    word_in_hand = True
    word_in_wordlist = False

    for entry in word_list:  # For each string in word_list
        if word == entry:  # Check if word matches it
            word_in_wordlist = True

    word_2_dict = get_frequency_dict(word) # Convert word into a dict for ease

    for letter in word_2_dict.keys():  # For each letter in word
        if not word_2_dict.get(letter) <= hand.get(letter):  # Compare value of a key in word to hand
            word_in_hand = False  # This will execute if the count for a letter in word is greater than that in hand

    return word_in_hand and word_in_wordlist

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """

    # PSEUDOCODE
    # 0. Call load_words() to load the dictionary.
    # 1. Check if hand has ended - hand is empty or '.' was entered. If yes->print total score.
    # 2. Call display_hand() and ask user to input a word
    # 3. Call is_valid_word() to check if it is a legitimate play and word
    # 4. If invalid word then ask user to enter a word again
    # 5. If valid word, call update_hand()
    # 6. Call get_word_score() to calculate score
    # 7. Display total score.
    # 8. Back to # 2
    # VARIABLES NEEDED:
    # 1. Something to hold return from load_words() - word_list
    # 2. Something to check if hand has ended - hand_ended
    # 2. Something to hold the entered word - input_word
    # 3. Something to check for valid word - is_valid
    # 4. Something to hold the total score - score
    # 5. Something to check if the hand has ended - hand_ended

    print "-"*35
    print "Starting the Game!!"
    is_valid = False  # to check for valid word
    is_period = False  # to check for '.'
    hand_ended = False  # to check if hand ended
    total_score = 0  # counter for score

    while not hand_ended and not is_period: # Runs till hand is empty or '.' is entered
        print "Current hand is: ", display_hand(hand)

        while not is_valid and not is_period and not hand_ended: # Keeps executing until a valid word or '.' is entered
            input_word = raw_input("Enter word, or a . to indicate that you are finished:")
            if input_word == '.':
                is_period = True
                hand_ended = True
                break
            else:
                is_valid = is_valid_word(input_word,hand,word_list)
                if is_valid:  # If word is valid then calculate score and update hand
                    word_score = get_word_score(input_word, HAND_SIZE)
                    total_score += word_score
                    print "%s earned %d points. Total: %d " % (input_word, word_score, total_score)
                    hand_updated = update_hand(hand,input_word)  # Update the hand
                    print "Updated hand: ", hand_updated
                    hand_ended = empty_dict(hand_updated)  # check if hand has ended i.e. all letters are used up
                    is_valid = False  # reset is_valid to go through loop again for nex play

    print "Total Score: %d" % total_score


def empty_dict(input_dict):
    """
    Returns True if a dictionary is 'empty' i.e. all the values are zero
    :param input_dict:
    :return: True or False
    """
    print "inside emptydict func"
    for key in input_dict.keys():
        if input_dict.get(key) != 0:
            return False
            break
    return True


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
    #print "play_game not implemented."         # delete this once you've completed Problem #4
    #play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4

    play_hand({'h': 1, 'e': 1, 'l': 2, 'n': 1, 'o': 2}, word_list)  # debug
    
    ## uncomment the following block of code once you've completed Problem #4
#    hand = deal_hand(HAND_SIZE) # random init
#    while True:
#        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
#        if cmd == 'n':
#            hand = deal_hand(HAND_SIZE)
#            play_hand(hand.copy(), word_list)
#            print
#        elif cmd == 'r':
#            play_hand(hand.copy(), word_list)
#            print
#        elif cmd == 'e':
#            break
#        else:
#            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

