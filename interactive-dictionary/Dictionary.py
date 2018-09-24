# A command line dictionary
import os, json
from difflib import get_close_matches

# Program assumes that we have the dictionary database in the same folder 
# os.chdir('/Users/admin/Desktop/Python/Dictionary')

# change working dictionary to our Dictionary folder
data = json.load(open("data.json"))


def dictionary(word):
    if word in data:
        return data[word][0]
    elif word.capitalize() in data:
        return data[word.capitalize()][0]
    elif len(get_close_matches(word, data.keys()))>0:
        query = input("Did you mean %s instead? \nEnter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0]).lower()

        if query == 'y':
            answer = ''
            for i in data[get_close_matches(word, data.keys())[0]]:
                    answer += i + '\n'
            return answer
        elif query == 'n':

            return 'This word doesn\'t exists. Please double check it.'
        else:
            return 'Sorry. I didn\'t understand your input'
    else:
        return 'This word doesn\'t exists. Please double check it.'

word = 'papa' # Make word a non empty string
while word!='':
    word = input('Enter a word: ').lower()# Take user input
    print(dictionary(word))
