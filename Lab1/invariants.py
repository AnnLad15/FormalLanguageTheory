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

    #вывод строчек в которых инварианты False
    #for index, value in enumerate(result):
        #if not value["result"]:
            #print(word)
            #print(result[index - 1])
            #print(value)

    for r in result:
        if not r["result"]:
            return result
    return None


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
        "count_a+b+2c": [inv_count_a_plus_b_plus_2c, inv_test_gte],

        #   #"count_c": [inv_count_c, inv_test_gte],
        #   #"count_a+c": [inv_count_a_plus_c, inv_test_gte]
        #   #"parity_blocks": [inv_odd_len_block_x_parity, inv_test_eq],
        #   #"inv_min_pos_a": [inv_min_pos_a, inv_test_gte],
        #   #"ac+ccc": [inv_count_ac_plus_ccc,inv_test_gte],
        #   #"a_plus_b_mod2":[inv_count_a_plus_b_mod2,inv_test_eq]
    }



def inv_test_gte(v1, v2):
    return v1 >= v2


def inv_test_eq(v1, v2):
    return v1 == v2


def inv_len(word):
    """
        Инвариант: длина слова
    """
    return len(word)

def inv_count_c(word):
    """
        Инвариант: количество букв c
    """
    c = Counter(word)
    return c.get('c', 0)


def inv_count_a_plus_c(word):
    """
        Инвариант: количество букв a+c
    """
    c = Counter(word)
    return c.get('a', 0) + c.get('c', 0)


def inv_count_a_plus_b_plus_2c(word):
    """
        Инвариант: I(w)= a + b + 2 * c
    """
    c = Counter(word)
    return c.get('a', 0) + c.get('b', 0) + 2 * c.get('c', 0)


def inv_odd_len_block_x_parity(word: str):
    """
        Инвариант: чётность (mod 2) количества X-блоков нечётной длины
    """
    word_blocks = word.replace("a", "x")
    word_blocks = word_blocks.replace("b", "x")
    _, block_count_odd, _ = count_blocks_by_leter(word_blocks, "x")
    return block_count_odd % 2


def count_blocks_by_leter(word: str, leter='x'):
    """
    Функция подсчета общее количество блоков, количество блоков нечетной и четной длины
    """
    if not word:
        return 0, 0, 0  # пустое слово → 0 блоков, чётность 0

    block_count = 0  # первый блок уже есть
    block_len = 0
    prev = word[0]
    block_count_odd = 0
    if prev == leter:
        block_len = 1

    for ch in word[1:]+".":
        if ch == leter:
            if ch != prev:
                block_len = 1
            else:
                block_len += 1
        else:
            if prev == leter:
                block_count_odd += block_len % 2
                block_count += 1
                block_len = 0
        prev = ch

    return block_count, block_count_odd, block_count - block_count_odd


def inv_min_pos_a(word: str):
    """
    Инвариант: минимальная позиция символа 'a' в слове.
    Если 'a' нет в слове, возвращает длину слова (т.е. максимальное значение).
    """
    try:
        return word.index('a')
    except ValueError:
        return len(word)

def inv_count_ac_plus_ccc(word: str):
    """
    Инвариант ac+ccc
    """
    return word.count("ac") + word.count("ccc")


def inv_count_a_plus_b_mod2(word: str):
    """
    Инвариант: (#a + #b) mod 2 для данного слова.
    """
    c = Counter(word)
    return (c.get('a', 0) + c.get('b', 0)) % 2

def invariant_test(iteration_count=3000):
    T = test_rules.get_initials_rules()
    T_new = test_rules.get_new_rules()
    alphabet = test_rules.get_alphabet()
    ok_old = fail_old = 0
    ok_new = fail_new = 0

    for i in range(1, iteration_count + 1):
        word = srs.generate_random_word(alphabet, 10)

        # T
        result_old = invariant_test_iteration(word, T, 10)
        if result_old is None:
            ok_old += 1
        else:
            fail_old += 1

        # T_new
        result_new = invariant_test_iteration(word, T_new, 10)
        if result_new is None:
            ok_new += 1
        else:
            fail_new += 1

        if i % 10 == 0:
            print(f"{i}/{iteration_count}  T: success:{ok_old}, fail:{fail_old}  T_new: success:{ok_new}, fail:{fail_new}")

    print("\n==== Results ====")
    print(f"T: success:{ok_old}  fail:{fail_old}")
    print(f"T_new: success:{ok_new}  fail:{fail_new}")

invariant_test()
