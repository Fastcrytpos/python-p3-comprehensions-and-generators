#!/usr/bin/env python3

def return_evens(num_list):
        list_of_evens=[n for n in num_list if n % 2==0 ]
        return list_of_evens if list_of_evens else []

    

def make_exclamation(sentence_list):
    result=[] if not sentence_list else [str(n)+"!" for n in sentence_list]
    return result
    pass