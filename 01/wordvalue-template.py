from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    dictAsList = [i.upper().rstrip() for i in open(DICTIONARY)]
    return dictAsList

print(load_words())

def calc_word_value(load):
    """Calculate the value of the words found in the data.py dictionary.txt, stores
    those values as key-value pairs to a new dict"""
    wordValues = {}
    for word in load:
        wordNum = 0
        for letter in word:
            wordNum += LETTER_SCORES[letter]
        wordValues[word] = wordNum
    return wordValues

print(calc_word_value(load_words()))

def max_word_value(input=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if isinstance(input, list):
        print("it's a list")
    elif isinstance(input, str):
        print("it's a string")

    print("max word value called", input)
        # create a re-usable function to calculate word values

max_word_value()
print(type(DICTIONARY))

if __name__ == "__main__":
    pass # run unittests to validate
