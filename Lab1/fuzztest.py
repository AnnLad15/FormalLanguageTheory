import srs
import test_rules


def apply_rules_until_target_found(source_word, target_word, rules, max_iteration):
    iteration = 0
    new_words_iterations = set()
    source_words = {source_word}
    new_words_all = {source_word}
    while iteration <= max_iteration:
        # print(iteration)
        for w in source_words:
            new_words = srs.apply_rules(w, rules)
            if target_word in new_words:
                print("iteration", iteration, len(new_words_all))
                return True
            new_words_iterations.update(new_words)
        source_words = new_words_iterations - new_words_all
        if len(source_words) == 0:
            return False
        new_words_all.update(source_words)
        iteration += 1
        # print(source_words)
    return False


def fuzz_iteration(T, T_new, alphabet, word_len=10, rules_iterations=10, max_depth=1000):
    source_word = srs.generate_random_word(alphabet, word_len)
    target_word = srs.apply_n_times_random_rule(source_word, T, rules_iterations)
    success = apply_rules_until_target_found(source_word, target_word, T_new, max_depth)
    return source_word, target_word, success


def fuzz_test(iteration_count=3000):
    T = test_rules.get_initials_rules()
    T_new = test_rules.get_new_rules()
    alphabet = test_rules.get_alphabet()
    success = 0
    fail = 0
    for i in range(iteration_count):
        if i % 10 == 0:
            print(i,"/",iteration_count , success, fail)
        source_word, target_word, result = fuzz_iteration(T, T_new, alphabet, 20, 10, 100)
        if result:
            success += 1
        else:
            fail += 1
            print("fuzzing", i, result, source_word, target_word)
    return success, fail


print(fuzz_test(500))
# print(apply_rules_until_found_target('aaabcbccac', 'bbcccc', T_new, 1000))
# print(apply_rules_until_target_found("cabbabbbbb", "bbaababab", T_new, 200))
# print(apply_rules('aaacc', T_new))
