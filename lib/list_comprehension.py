#!/usr/bin/env python3

def return_evens(num_list):
    pass
    evens = [num for num in num_list if num % 2 == 0]
    return evens





def make_exclamation(sentence_list):
    pass
    if not sentence_list:
        return []  # Return an empty list if sentence_list is empty
    else:
        return [sentence + '!' for sentence in sentence_list]