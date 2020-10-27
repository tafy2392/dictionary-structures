import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return(data[word])
    elif get_close_matches(word, data.keys()):
        return "Did you mean {}".format(get_close_matches(word, data.keys())[0])
    else:
        return "Word does not exist"

word=input("Enter a word to translate: \n")
print(translate(word.lower()))
