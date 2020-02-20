#!/bin/python3



from collections import deque
from copy import copy, deepcopy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    
    if len(start_word) != len(end_word):
        return False

    word_stack =[]
    word_stack.append(start_word)
    word_q = ([])
    word_q.append(word_stack)

    while len(word_q) != 0:
        #dequeue a stack from the queue

        for x in dictionary_file:
            if _adjacent(x, word_stack[0]):
                if x == end_word:
                    word_stack.append(x)
                    return verify_word_stack(word_stack)
               # make a copy of the stack
               # push the found word onto the copy
               # enqueue the copy
               # delete word from the dictionary


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
