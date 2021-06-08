import mysql.connector
import json
from difflib import get_close_matches

def initialise():
    try:
        con=mysql.connector.connect(
            user="ardit700_student",
            password="ardit700_student",
            host="108.167.140.122",
            database="ardit700_pm1database"
        )
        cursor = con.cursor()
        cursor.execute("SELECT DISTINCT Expression FROM Dictionary")
        results = cursor.fetchall()
        contents = list(w[0] for w in results)
        connected=True
        data = None
    except:
        connected=False
        cursor = None
        data = json.load(open('data.json'))
        contents = data.keys()
    return connected, contents, data, con

def get_match(word, contents):
    if word in contents:
        return word
    elif word.title() in contents:
        return word.title()
    elif word.upper() in contents:
        return word.upper()
    elif len(get_close_matches(word, contents)) > 0:
        prompt = input( "That word isn't in this dictionary, did you mean '%s' instead? Y/N: " % get_close_matches(word, contents)[0])
        print()
        if prompt.upper() == 'Y':
            return get_close_matches(word, contents)[0]
        elif prompt.upper() != 'N':
            print("We didn't understand your response.\n")
            return None     
    print("%s not found, try another.\n" % word)
    return None

def definition_output(key,con,data):
    if connected:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % key)
        results = cursor.fetchall()
        output = [r[1] for r in results]
    else:
        output = data[key]
        output = output if type(output) == list else [output]

    for item in output:
        print(f" - {item}")
    print()

connected, contents, data, con = initialise()
active = True
while active:
    word = input("Enter a word to get its definition: ").lower()
    print()
    key = get_match(word, contents)
    if key:
        definition_output(key, con, data)
    prompt = input("Would you like to define another word? Y/N: ")
    while prompt.upper() not in ['Y', 'N']:
        prompt = input("Sorry I didnt understand that. \nWould you like to define another word? Y/N: ")
    print()
    if prompt.upper() == "N":
        print("Thank you for using this dictionary.")
        active = False
