from Lab2.AFA_test import create_afa
from itertools import product


def reachable_table_filtered_afa(states, alphabet, transitions, initial_state, final_states, max_depth=3):
    words = [""]
    for d in range(1, max_depth + 1):
        for w in product(alphabet, repeat=d):
            words.append("".join(w))

    def delta_star(state_set, word):
        current = set(state_set)
        for symbol in word:
            next_states = set()
            for state in current:
                if state in transitions and symbol in transitions[state]:
                    for transition_set in transitions[state][symbol]:
                        next_states.update(transition_set)
            current = next_states
            if not current:
                break
        return current

    def is_accepting_from_state(state, word):
        end_states = delta_star({state}, word)
        return bool(end_states & final_states)

    table = {}
    for w in words:
        row = {}
        for s in states:
            accepts = is_accepting_from_state(s, w)
            row[s] = "+" if accepts else ""
        table[w] = row

    filtered_table = {
        w: row for w, row in table.items()
        if any(v == "+" for v in row.values())
    }

    return filtered_table


def print_table(table, states, max_depth=10):
    states = sorted(states)
    word_width = max_depth + 1
    state_width = 3

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

    all_unique = True

    for sign, group in groups.items():
        if len(group) > 1:
            all_unique = False
            print(f"Одинаковые столбцы у состояний: {group}")

    if all_unique:
        print("Все столбцы различны")
    else:
        print("Есть одинаковые столбцы")

    return all_unique


afa = create_afa()
states = afa.states
alphabet = afa.input_symbols
transitions = afa.transitions
initial_state = afa.initial_state
final_states = afa.final_states

print("Анализ AFA:")
print(f"Состояния: {sorted(states)}")
print(f"Алфавит: {alphabet}")
print(f"Начальное состояние: {initial_state}")
print(f"Конечные состояния: {final_states}")

table_afa = reachable_table_filtered_afa(states, alphabet, transitions, initial_state, final_states, max_depth=6)
print("\nТаблица достижимости для AFA:")
print_table(table_afa, states, max_depth=5)

print("\nПроверка наличия '+' в столбцах:")
check_columns_have_plus(table_afa, states)

print("\nПроверка уникальности столбцов:")
check_no_identical_columns(table_afa, states)
