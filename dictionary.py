import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def definition(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data)) > 0:
        prompt = input( "Did you mean %s instead? Y to accept, N to ignore: " % get_close_matches(word, data)[0] )
        if prompt.upper() == 'Y':
            return definition(get_close_matches(word, data)[0])
        elif prompt.upper() != 'N':
            return "We didn't understand your response."
            
    return "%s not found, try another." % word

word = input('Enter word: ')
output = definition(word)
output = output if type(output) == list else [output]

for item in output:
    print(item)
