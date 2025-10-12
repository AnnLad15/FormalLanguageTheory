from collections import Counter

import srs
import test_rules


def invariant_test_iteration(word, T, rules_iterations=10):
    source_word = word
    words_chain = [source_word]
    for i in range(rules_iterations):
        source_word = srs.apply_n_times_random_rule(source_word, T, 1)
        words_chain.append(source_word)
    result = calculate_and_test_chain(words_chain)
    for index, value in enumerate(result):
        if not value["result"]:
            print(word)
            print(result[index - 1])
            print(value)


def calculate_and_test_chain(words_chain):
    invs = get_inv_funcs()
    calcs = []
    for w in words_chain:
        calcs_for_word = {"word": w}
        for inv, funcs in invs.items():
            calc = funcs[0]
            calcs_for_word[inv] = calc(w)
        calcs.append(calcs_for_word)

    prev_calc = calcs[0]
    prev_calc["result"] = True
    for c in calcs[1:]:
        c["result"] = True
        for inv, funcs in invs.items():
            test_func = funcs[1]
            res = test_func(prev_calc[inv], c[inv])
            c["result_" + inv] = res
            c["result"] = c["result"] & res
        prev_calc = c
    return calcs


def get_inv_funcs():
    return {
        "len": [inv_len, inv_test_gte],
        "count_c": [inv_count_c, inv_test_gte],
        "count_a+c": [inv_count_a_plus_c, inv_test_gte]
    }


def inv_len(word):
    return len(word)


def inv_test_gte(v1, v2):
    return v1 >= v2


def inv_count_c(word):
    c = Counter(word)
    return c.get('c', 0)


def inv_count_a_plus_c(word):
    c = Counter(word)
    return c.get('a', 0) + c.get('c', 0)


def invariant_test(iteration_count=3000):
    T = test_rules.get_initials_rules()
    T_new = test_rules.get_new_rules()
    alphabet = test_rules.get_alphabet()
    success = 0
    fail = 0
    for i in range(iteration_count):
        word = srs.generate_random_word(alphabet, 10)
        if i % 10 == 0:
            print(i, "/ 3000", success, fail)
        invariant_test_iteration(word, T, 10)
        invariant_test_iteration(word, T_new, 10)

    #     if result:
    #         success += 1
    #     else:
    #         fail += 1
    #         print("fuzzing", i, result, source_word, target_word)
    # return success, fail


invariant_test()

# print(
#     invariant_test_iteration(test_rules.get_initials_rules(), test_rules.get_new_rules(), test_rules.get_alphabet(), 20,
#                              10))
