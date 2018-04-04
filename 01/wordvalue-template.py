from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    dictAsList = [i.upper().rstrip() for i in open(DICTIONARY)]
    return dictAsList

print(load_words())

def calc_word_value(load):
    """Calculate the value of the words fund in the data.py dictionary.txt, stores
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
    of words as arg, if none provided uses default DICTIONARY

    Notes 4.4.2018: so it *can* accept any list, but I have set the default as
    the dictionary from data.py
    Will test whether it's there or not, then run the calculations on word value
    See test_wordvalue.py"""

    if input == type(list)

    else:
        # use the dictionary in a calculating function/



if __name__ == "__main__":
    pass # run unittests to validate
