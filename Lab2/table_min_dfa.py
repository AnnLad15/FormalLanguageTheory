from itertools import product
from Lab2.DFA_test import create_dfa


def reachable_table_filtered(states, alphabet, transitions, final_states, max_depth=3):
    words = [""]
    for d in range(1, max_depth + 1):
        for w in product(alphabet, repeat=d):
            words.append("".join(w))

    def delta_star(state, word):
        for symbol in word:
            if symbol not in transitions[state]:
                return None
            state = transitions[state][symbol]
        return state

    table = {}
    for w in words:
        row = {}
        for s in states:
            end = delta_star(s, w)
            row[s] = "+" if end in final_states else ""
        table[w] = row

    filtered_table = {
        w: row for w, row in table.items()
        if any(v == "+" for v in row.values())
    }

    return filtered_table


def print_table(table, states, max_depth=10):
    states = sorted(states)
    word_width = max_depth + 1
    state_width = 2

    header = ["path".ljust(word_width)] + [s.center(state_width) for s in states]
    print(" | ".join(header))
    print("-" * (word_width + len(states) * (state_width + 3)))

    for w, row in table.items():
        word = (w if w else "ε").ljust(word_width)
        cells = [row[s].center(state_width) for s in states]
        print(" | ".join([word] + cells))


def check_columns_have_plus(table, states):
    state_has_plus = {s: False for s in states}

    for row in table.values():
        for s, val in row.items():
            if val == "+":
                state_has_plus[s] = True

    missing = [s for s in states if not state_has_plus[s]]

    if not missing:
        print("\nВсе состояния имеют +")
    else:
        print("\nСостояния без +:", ", ".join(sorted(missing, key=lambda x: int(x))))

    return missing


def check_no_identical_columns(table, states):
    states = sorted(states)

    signatures = {s: [] for s in states}
    for w, row in table.items():
        for s in states:
            signatures[s].append(row[s])

    groups = {}
    for s, sign in signatures.items():
        key = tuple(sign)
        groups.setdefault(key, []).append(s)

    print("\nПроверка одинаковых столбцов:")
    all_unique = True

    for sign, group in groups.items():
        if len(group) > 1:
            all_unique = False
            print(f"Одинаковые столбцы у состояний: {group}")

    if all_unique:
        print("Все столбцы различны ")
    else:
        print("Есть одинаковые столбцы")

    return all_unique


dfa = create_dfa()
states = dfa.states
alphabet = dfa.input_symbols
transitions = dfa.transitions
final_states = dfa.final_states

# строим таблицу
table = reachable_table_filtered(states, alphabet, transitions, final_states, max_depth=10)
print_table(table, states, max_depth=10)

# проверка столбцов на наличие хотя бы одного +
check_columns_have_plus(table, states)

# проверка уникальности столбцов
check_no_identical_columns(table, states)
