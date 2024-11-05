from wsgiref.validate import validator

import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
# def index_smallest_from(values:list[int], start:int) -> Optional[int]:
#     if start >= len(values) or start < 0:
#         return None
#
#     mindex = start
#     for idx in range(start + 1, len(values)):
#         if values[idx] < values[mindex]:
#             mindex = idx
#
#     return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>

def index_smallest_from_str(values:list[data.Book], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx].title < values[mindex].title: #checks if  the value for books[i] is lower in the alphabet
            mindex = idx
    return mindex

# def selection_sort(values:list[data.Book]) -> None:
#     for idx in range(len(values) - 1):
#         mindex = index_smallest_from_str(values, idx)
#         tmp = values[mindex]
#         values[mindex] = values[idx]
#         values[idx] = tmp


# Part 1
def selection_sort_books(books:list[data.Book])->list[data.Book]:
    for i in range(len(books)-1):
        mindex = index_smallest_from_str(books, i)
        tmp = books[mindex]
        books[mindex] = books[i]
        books[i] = tmp
    return books



# Part 2
def swap_case(words:str)->str:
    results = ''
    for char in words:
        if char.islower():
            results = results +char.upper()
        else:
            results = results +char.lower()
    return results


# Part 3
def str_translate(phrase:str,old_let:str,new_let:str):
    translate_dict = {old_let:new_let}
    result = ''
    for char in phrase:
        if char in old_let:
            result += translate_dict[char]
        else:
            result += char
    return result


# Part 4
def histogram_letters(para:str):
    letter_dictionary = {}
    for i in para:
        if i not in letter_dictionary:
            letter_dictionary[i] = 1
        else:
            letter_dictionary[i] +=1
    return letter_dictionary