'''
English Thesaurus app
Asks for a word and prints out definition
'''
import json
from difflib import get_close_matches

def get_definition(word, data):
    """Get the definition of word from the data dictionary
    Keyword Arguments:
    word -- for which definition is requested
    data -- the data dictionary in json object
    Return Argument:
    string -- the result which is
    the definition if found or
    the closest word match in case pf spell mistake
    "doesn't exist" error message
    """
    err_doesnt_exist = "The word doesn't exist. Please check the same."
    err_spell_mistake = "Did you mean "
    word = word.lower()
    # noun, acronym and normal word forms
    word_forms = [word, word.capitalize(), word.upper()]
    for wrd_form in word_forms:
        if wrd_form in data:
            return data[wrd_form]
   # check for spell mistake
    matches = get_close_matches(word, data.keys(), cutoff=0.8)
    if matches:
        return err_spell_mistake + matches[0]

    return err_doesnt_exist


def print_output(i_word, str_or_lst):
    """ Print the string or list output
    Keyword Arguments:
    str_or_lst -- object to be printed
    """
    sep_str = "=================="
    print(sep_str)
    print(i_word + " means\n")
    if isinstance(str_or_lst, list):
        for item in str_or_lst:
            print(item)
    else:
        print(str_or_lst)

    print(sep_str)


def ask_word_reply_def(data):
    """Ask user for a word and print the definition
    Keyword Arguments:
    data -- The dictionary data json object
    """
    input_word = input("Enter word, 'qq' to quit: ")
    if input_word == 'qq':
        return False

    output = get_definition(input_word, data)
    print_output(input_word, output)
    return True


def main():
    """ Main function of the app
    """
    data = json.load(open("data.json"))
    while ask_word_reply_def(data):
        pass


if __name__ == '__main__':
    main()
