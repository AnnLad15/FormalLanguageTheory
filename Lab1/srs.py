import random

def apply_rule_once(word, rule, start_index):
    left = rule[0]
    right = rule[1]
    position = word.find(left, start_index)
    if position == -1:
        return None, position
    return word[:position] + right + word[position + len(left):], position


def test_apply_rule_once():
    assert apply_rule_once("aaccac", ("ac", "c"), 0) == ('accac', 1), "fail"
    assert apply_rule_once("aaccac", ("ac", "c"), 4) == ('aaccc', 4), "fail"
    assert apply_rule_once("ccccc", ("ac", "c"), 0) == (None, -1), "fail"


def apply_rule(word, rule):
    start_ind = -1
    words = []
    while True:
        word_new, start_ind = apply_rule_once(word, rule, start_ind + 1)
        if word_new == None:
            return words
        words.append(word_new)


def test_apply_rule():
    assert apply_rule("aaccac", ("ac", "c")) == ['accac', 'aaccc'], "fail"
    assert apply_rule("aaacaaabccac", ("ac", "c")) == ['aacaaabccac', 'aaacaaabccc'], "fail"
    assert apply_rule("bbbbccc", ("ac", "c")) == [], "fail"
    assert apply_rule("bbbbcacacac", ("ac", "c")) == ['bbbbccacac', 'bbbbcaccac', 'bbbbcacacc'], "fail"


def apply_rules(word, rules):
    words_all = set()
    for rule in rules:
        words = apply_rule(word, rule)
        words_all.update(words)
    return words_all


def test_apply_rules():
    assert apply_rules("accacb", [("ac", "c")]) == {'acccb', 'ccacb'}, "fail"
    assert apply_rules("accacb", [("ac", "c"), ("cb", "bc")]) == {'accabc', 'acccb', 'ccacb'}, "fail"
    assert apply_rules("accacb", [("ac", "c"), ("ac", "c")]) == {'acccb', 'ccacb'}, "fail"


def generate_random_word(alphabet, len_word):
    word = ""
    for i in range(len_word):
        word += alphabet[random.randint(0, len(alphabet) - 1)]
    return word


def test_generate_random_word():
    Alphabet = ['a', 'b', 'c']
    assert len(generate_random_word(Alphabet, 6)) == 6, "fail"
    assert len(generate_random_word(Alphabet, 20)) == 20, "fail"


def apply_n_times_random_rule(word, rules, iterations_count):
    new_word = word
    for i in range(iterations_count):
        words_all = list(apply_rules(new_word, rules))
        if len(words_all) == 0:
            break
        new_word = words_all[random.randint(0, len(words_all) - 1)]
    return new_word


def test_all():
    test_apply_rule_once()
    test_apply_rule()
    test_apply_rules()
    test_generate_random_word()


#test_all()