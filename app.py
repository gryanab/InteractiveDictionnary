import json

dictionary = json.load(open('data.json'))


def definition(word):
    word_to_lower_case = word.lower()
    try:
        return dictionary[word_to_lower_case]
    except KeyError:
        return 'The definition you asked for seems to not exists in our database. Please double check the spelling.'


asked_word = input('Please enter the word you want to get the definition of: ')

print(definition(asked_word))

