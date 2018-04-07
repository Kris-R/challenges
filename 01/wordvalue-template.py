from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    dictAsList = [i.upper().rstrip() for i in open(DICTIONARY)]
    return dictAsList

print(load_words())

def calc_word_value(load=DICTIONARY):
    """Calculate the value of the words found in the data.py __dictionary.txt__, stores
    those values as key-value pairs to a new dict"""
    wordValues = {}
    for word in open(load):
        word = word.upper().rstrip()
        wordNum = 0
        for letter in word:
            wordNum += LETTER_SCORES[letter]
        wordValues[word] = wordNum
    return wordValues

print(calc_word_value())

def max_word_value(input=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if isinstance(input, list):
        print("Working with a list")
        max_value = 0
        max_word = 0
        for word in input:
            currentValue = 0
            for letter in word:
                currentValue += LETTER_SCORES[letter]
            if currentValue > max_value:
                max_value = currentValue
                max_word = word
        return max_word, max_value

    elif isinstance(input, str):
        print("Working with a string")
        max_value = 0
        max_word = 0
        for word in open(input):
            word = word.upper().rstrip()
            currentValue = 0
            for letter in word:
                currentValue += LETTER_SCORES[letter]
            if currentValue > max_value:
                max_value = currentValue
                max_word = word
        return max_word, max_value


print(max_word_value())
print(max_word_value(load_words()))

if __name__ == "__main__":
    pass # run unittests to validate
