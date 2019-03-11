import json
from difflib import get_close_matches

dictionary = json.load(open('data.json'))


def definition(word: str):
    """
    Returns definition of a single based on the data.json file.
    Input: word as a string.
    Output: Definition(s) as list.
    """

    word_to_lower_case = word.lower()
    try:
        if word in dictionary:
            return dictionary[word]
        elif word_to_lower_case in dictionary:
            return dictionary[word_to_lower_case]
        elif word.title() in dictionary:  # if user entered "texas" this will check for "Texas" as well.
            return dictionary[word.title()]
        # returning several items in list
        elif len(get_close_matches(word_to_lower_case, dictionary.keys(), cutoff=0.8)) > 0:
            # proposing item with the greatest probability to match query. Hence, the first one on the list.
            yn = str(input('Did you mean {} instead? yes/no : '.format(get_close_matches(word_to_lower_case, dictionary.keys())[0]))).lower()
            while not(yn == 'y' or yn == 'yes' or yn == 'n' or yn == 'no'):
                    # taking into account empty answer.
                    if len(yn) == 0:
                         print('Please enter yes/y or no/n')
                    else:
                        print('Please enter yes/y or no/n.')
                    yn = str(input('Did you mean {} instead? yes/no : '.format(get_close_matches(word_to_lower_case, dictionary.keys())[0]))).lower().strip()
            if yn == 'y' or yn == 'yes':
                return dictionary[get_close_matches(word_to_lower_case, dictionary.keys())[0]]
            elif yn == 'n' or yn == 'no':
                return 'The definition you asked for seems to not exists in our database. Please double check the spelling.'
        elif len(word) == 0:
            return 'Please enter something.'
    except KeyError:
        return 'The definition you asked for seems to not exists in our database. Please double check the spelling.'


asked_word = input('Please enter the word you want to get the definition of: ')

output = definition(asked_word)

if type(output) == list:
    i = 1
    for item in output:
        print('Definition(s) of the word: ', asked_word)
        print('Definition ', i, ' ', item)
        i += 1
else:
    print(output)

