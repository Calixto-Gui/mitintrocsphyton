# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:03:56 2023

@author: GUILH
"""
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    x=0
    

    if len(my_word) == len(other_word):
        for e in range(len(my_word)) :
            if my_word[e] == other_word[e] :
                x = x + 1
            else:
                x = x + 0
        if x > 0:
            return True
        else:
            return False
    else:
        return False
    
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    lst=[]
    
    for word in wordlist:
        other_word = word
        if match_with_gaps(my_word, other_word):
            lst.append(word)
    if len(lst) == 0:
        print('No matches found')
    else:
        print(lst)

wordlist = ["ball","bill","bull","house","cat"]

my_word = "b____"

show_possible_matches(my_word)
