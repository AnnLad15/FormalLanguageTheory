import random

T = [
    ("ac", "c"),
    ("aa", "ba"),
    ("bc", "c"),
    ("ca", "aa"),
    ("cb", "bc"),
    ("ccc", "c"),
    ("aaa", "aa"),
    ("aab", "ba"),
    ("aba", "abb"),
    ("bba", "bbb"),
]

T_dif = [
    ("cc", "c"),
    ("abb", "bbb"),
    ("bbb", "ba"),
    ("bab", "ba"),
    ("ba", "c"),
]
T_new = T + T_dif

Alphabet = ['a', 'b', 'c']


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
    assert len(generate_random_word(Alphabet, 6)) == 6, "fail"
    assert len(generate_random_word(Alphabet, 20)) == 20, "fail"


def apply_n_times_random_rule(word, rules, iterations_count):
    new_word = word
    for i in range(iterations_count):
        words_all = list(apply_rules(new_word, rules))
        if len(words_all) == 0:
            print("новые правила не применились", new_word)
            break
        new_word = words_all[random.randint(0, len(words_all) - 1)]
    return new_word


def apply_rules_until_found_target(source_word, target_word, rules, max_iteration):
    iteration = 0
    new_words_iterations = set()
    source_words = {source_word}
    new_words_all = {source_word}
    while iteration <= max_iteration:
        print(iteration)
        for w in source_words:
            new_words = apply_rules(w, rules)
            if target_word in new_words:
                return True
            new_words_iterations.update(new_words)
        source_words = new_words_iterations - new_words_all
        new_words_all.update(source_words)
        iteration += 1





def fuzz():
    source_word = generate_random_word(Alphabet, 20)
    target_word = apply_n_times_random_rule(source_word, T, 10)
    success = apply_rules_until_found_target(source_word,target_word,T_new,1000)
    return source_word, target_word, success


print(fuzz())

#print(apply_rules_until_found_target('aaabcbccac', 'bbcccc', T_new, 1000))


def test_all():
    test_apply_rule_once()
    test_apply_rule()
    test_apply_rules()
    test_generate_random_word()


test_all()
