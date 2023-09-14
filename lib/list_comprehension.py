#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [x for x in num_list if x % 2 == 0]
    return even_numbers

def make_exclamation(sentence_list):
    if not sentence_list:
        return []
    return [sentence + '!' for sentence in sentence_list]

from list_comprehension import return_evens, make_exclamation
