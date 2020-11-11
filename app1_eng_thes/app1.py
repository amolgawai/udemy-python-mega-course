'''
English Thesaurus app
Asks for a word and prints out definition
'''
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

ERR_DOESNT_EXIST = "The word doesn't exist. Please check the same."
ERR_SPELL_MISTAKE = "Did you mean "
SEPARATOR = "=================="

def get_definition(word):
    word_noun = word.capitalize()
    word_acronym = word.upper()
    word = word.lower()
    if word in data:
        return data[word]
    elif word_noun in data:
        return data[word_noun]
    elif word_acronym in data:
        return data[word_acronym]
    else:
        matches = get_close_matches(word, data.keys())
        if matches:
            return ERR_SPELL_MISTAKE + matches[0]
        else:
            return ERR_DOESNT_EXIST

def print_output(str_or_lst):
        print(SEPARATOR)
        if type(str_or_lst) == list:
                for item in str_or_lst:
                        print(item)
        else:
            print(str_or_lst)

input_word = input("Enter word: ")
output = get_definition(input_word)
print_output(output)