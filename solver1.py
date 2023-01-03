import pandas as pd
import random
import string
import numpy as np


def solve(word_list, word):
    subset = word_list
    count = 0
    while len(subset) > 0 and count < 15:
        guess = guess_word(subset)[0]
        count += 1
        print(guess)

        subset = [x for x in subset if guess not in x[0]]

        for pos in range(0,5):
            if guess[pos] == word[pos]:
                subset = [x for x in subset if guess[pos] == x[0][pos]]

            else:
                if len(word.replace(guess[pos], '')) != 3 and len(guess.replace(guess[pos], '')) == 3:
                    subset = [x for x in subset if len(x[0].replace(guess[pos], '')) != 3]

                if guess[pos] in word:
                    subset = [x for x in subset if guess[pos] in x[0]]

                else:
                    subset = [x for x in subset if guess[pos] not in x[0]]


def guess_word(subset):
    frequency_list = frequency_table(subset)

    for word in subset:
        score = 0
        max = 0

        for pos in range(0,5):
            char = word[0][pos]
            score = score + frequency_list[pos][ord(char) - 97]

        if score > max:
            max = score
            max_word = word

    return max_word

def frequency_table(subset):
    letters = string.ascii_lowercase
    list1 = []
    for i in letters:
        list1.append(i)

    frequency_list = np.zeros(5*26).reshape(5, 26)

    for pos in range(0,5):
        for word in subset:
            char = word[0][pos]
            frequency_list[pos][ord(char) - 97] = frequency_list[pos][ord(char) - 97] + 1

    return frequency_list


if __name__ == '__main__':
    word_list = pd.read_csv("wordlist.csv", header=None).values.tolist()
    rand_word = random.choice(word_list)[0]

    print("The random word is: " + rand_word)
    print("Here are the guesses")

    solve(word_list, rand_word)
