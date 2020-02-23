#!/bin/python3


import collections
from collections import deque
from copy import copy, deepcopy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    
    if start_word == end_word: 
        final_ladder = [start_word]
        return final_ladder

    if len(start_word) != len(end_word):
        return False

    f = open(dictionary_file, 'r')
    full_5word_dict = f.read().split()


    ladder_stack =[]  # a stack = list
    ladder_stack.append(start_word)
    word_q = deque() # a deque = a queue
    word_q.append(ladder_stack)

    while len(word_q) > 0:
        #dequeue a stack from the queue
        wq = word_q.popleft()
        for x in full_5word_dict:
            if _adjacent(x, wq[-1]):
                if x == end_word:
                    wq.append(x)
                return wq
                break
            copied_wq = deepcopy(wq) #make a DEEPcopy of the stack
            copied_wq.append(x) # push the found word onto the copy
            word_q.append(copied_wq) # enqueue the copy
            full_5word_dict.remove(x) # delete word from the dictionary


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    for i in range (len(ladder)-1):
        if _adjacent(ladder[i], ladder[i+1]):
            return True
    return False
        

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
    if diff == 1: return True
    else: return False


