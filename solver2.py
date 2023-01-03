import pandas as pd
import random
import sys
import numpy as np


def solve(word_list, word, valid_list):
    count = 1
    subset = subset_fun(word_list, "roate", word)
    #print("roate")
    while len(subset) > 0:
        guess = guess_word(subset, valid_list)
        #print(guess)
        subset = subset_fun(subset, guess, word)
        count += 1

    return count


def guess_word(subset, valid_list):
    min = sys.maxsize
    best_guess = ""

    for guess in valid_list:
        score = 0

        for word in subset:
            score += len(subset_fun(subset, guess, word))

        if score < min:
            min = score
            best_guess = guess

    return best_guess


def subset_fun(subset, guess, word):
    subset = [x for x in subset if guess not in x]

    for pos in range(0, 5):
        if guess[pos] == word[pos]:
            subset = [x for x in subset if guess[pos] == x[pos]]

        else:
            if len(word.replace(guess[pos], '')) != 3 and len(guess.replace(guess[pos], '')) == 3:
                subset = [x for x in subset if len(x.replace(guess[pos], '')) != 3]

            if guess[pos] in word:
                subset = [x for x in subset if guess[pos] in x]

            else:
                subset = [x for x in subset if guess[pos] not in x]

    return subset


if __name__ == '__main__':
    word_list = pd.read_csv("wordlist.csv", header=None).values.tolist()
    word_list = list(np.array(word_list).flatten())
    valid_list = pd.read_csv("valid-words.csv", header=None).values.tolist()
    valid_list = list(np.array(valid_list).flatten())
    rand_word = random.choice(word_list)

    #print("The random word is: " + rand_word)
    #print("Here are the guesses")
    #solve(word_list, rand_word, valid_list)


    count = 0

    for i in range(0, 100):
        rand_word = random.choice(word_list)
        count += solve(word_list, rand_word, valid_list)
        print(i)

    print(count/100)

