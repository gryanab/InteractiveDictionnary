import json
from difflib import get_close_matches

dictionary = json.load(open('data.json'))


def definition(word: str) -> str:
    word_to_lower_case = word.lower()
    try:
        if word_to_lower_case in dictionary:
            return str(dictionary[word_to_lower_case])
        elif len(get_close_matches(word_to_lower_case, dictionary.keys(), cutoff=0.8)) > 0:
            return 'Did you mean {} instead?'.format(get_close_matches(word_to_lower_case, dictionary.keys())[0])
    except KeyError:
        return 'The definition you asked for seems to not exists in our database. Please double check the spelling.'


asked_word = input('Please enter the word you want to get the definition of: ')

print(definition(asked_word))

