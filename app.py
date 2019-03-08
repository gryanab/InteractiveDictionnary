import json

dictionary = json.load(open('data.json'))

def definition(word):
    return dictionary[word]


word = input('Please enter the word you want to get the definition of: ')

print(definition(word))

