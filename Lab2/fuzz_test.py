import random
import re

from Lab2.AFA_test import create_afa
from Lab2.DFA_test import create_dfa
#from Lab2.NFA_test import create_nfa
from Lab2.NFA_min_test import create_nfa


def generate_random_word(alphabet, len_word):
    word = ""
    for i in range(len_word):
        word += alphabet[random.randint(0, len(alphabet) - 1)]
    return word


def generate_valid_random_word():
    """
    (aa*ab|bbabb|abb*abab)*baba(a|b)(a|b)((aa)*ab|babb*aabab)*
    """
    result = ''
    # (aa*ab|bbabb|abb*abab)*
    reps = random.randint(0, 10)
    for i in range(reps):
        variant = random.randint(0, 2)
        if variant == 0:
            word = 'a' + 'a' * random.randint(0, 10) + 'ab'
        elif variant == 1:
            word = 'bbabb'
        else:
            word = 'ab' + 'b' * random.randint(0, 10) + 'abab'
        result += word

        # baba
    result += 'baba'

    # (a|b)(a|b)
    if random.randint(0, 1) == 0:
        result += 'a'
    else:
        result += 'b'

    if random.randint(0, 1) == 0:
        result += 'a'
    else:
        result += 'b'

        # ((aa)*ab|babb*aabab)*
    reps2 = random.randint(0, 10)
    for i in range(reps2):
        variant = random.randint(0, 1)
        if variant == 0:
            word = 'aa' * random.randint(0, 10) + 'ab'
        else:
            word = 'bab' + 'b' * random.randint(0, 10) + 'aabab'
        result += word

    return result


# print(generate_valid_random_word())


def fuzztest(dfa, nfa, afa, regular, iterations=1000):
    success_nfa = 0
    success_dfa = 0
    success_afa = 0
    # success_random = 0
    success_regular = 0
    success_random_t = 0

    for i in range(iterations):
        word = generate_valid_random_word()
        # print(word)
        if nfa.accepts_input(word):
            success_nfa += 1
        if dfa.accepts_input(word):
            success_dfa += 1
        if afa.accepts_input(word):
            success_afa += 1
        if re.match(regular, word) is not None:
            success_regular += 1

    # for i in range(iterations):
    #     word = generate_random_word(['a', 'b'], 20)
    #     if nfa.accepts_input(word) == dfa.accepts_input(word):  # False == False or True == True
    #         success_random += 1

    for i in range(iterations):
        word = generate_random_word(['a', 'b'], 20)
        # print(word)
        t1 = nfa.accepts_input(word)
        t2 = dfa.accepts_input(word)
        t4 = afa.accepts_input(word)
        t3 = re.match(regular, word) is not None
        # print(word, t1, t2, t3)
        if t1 == t2 and t1 == t3 and t1==t4:
            success_random_t += 1

    return {"nfa": [success_nfa, iterations - success_nfa]}, \
           {"dfa": [success_dfa, iterations - success_dfa]}, \
           {"afa": [success_afa, iterations - success_afa]}, \
           {"regex": [success_regular, iterations - success_regular]}, \
           {"random word": [success_random_t, iterations - success_random_t]}
    # {"random word":[success_random, iterations - success_random]}, \


dfa = create_dfa()
nfa = create_nfa()
afa = create_afa()
regular = r"^(a+ab|bbabb|ab+abab)*baba..((aa)*ab|bab+aabab)*$"

print(fuzztest(dfa, nfa, afa, regular, 10000))
