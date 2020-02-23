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
    with open(dictionary_file) as f:
        xs = f.readlines()
    full_word_dict = open(dictionary_file).read().split("\n")
    

    if len(start_word) != len(end_word):
        return False

    word_stack =[]  # a stack = list
    word_stack.append(start_word)
    word_q = queue() # a deque = a queue
    word_q.append(word_stack)

    while len(word_q) != 0:
        #dequeue a stack from the queue
        wq = word_q.pop()
        for x in full_word_dict:
            if _adjacent(x, wq[-1]):
                if x == end_word:
                    wq.append(x)
                    return verify_word_stack(word_stack)
               copied_stack = deepcopy(wq) #make a DEEPcopy of the stack
               copied_stack.append(x) # push the found word onto the copy
               wq.appendleft(copied_stack) # enqueue the copy
               full_word_dict.remove(word) # delete word from the dictionary


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if len(ladder) == 0:
        return False
    else:
        for i in range (len(ladder)-1):
            if not _adjacent(ladder[i], ladder[i+1]):
                return False
        return True
        

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    diff = 0 
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff +=1
    if diff > 1: return False
    return True

