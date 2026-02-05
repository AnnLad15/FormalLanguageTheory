# AFA.py
class AFA:
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def accepts_input(self, input_string: str) -> bool:
        memo = {}
        return self._accepts_state(self.initial_state, input_string, 0, memo)

    def _accepts_state(self, state, input_string, position, memo) -> bool:
        is_epsilon = False

        if state in self.transitions and 'epsilon' in self.transitions[state]:
            epsilon_clauses = self.transitions[state]['epsilon']
            is_epsilon = True

        key = (state, position)
        if key in memo:
            return memo[key]

        if position == len(input_string):
            result = state in self.final_states
            memo[key] = result
            return result

        if not is_epsilon:
            symbol = input_string[position]
            if symbol not in self.input_symbols:
                memo[key] = False
                return False

            if state not in self.transitions or symbol not in self.transitions[state]:
                memo[key] = False
                return False
            clauses = self.transitions[state][symbol]

        else:
            clauses = epsilon_clauses



        for clause in clauses:
            all_accept = True
            for next_state in clause:
                shift = 1
                if is_epsilon:
                    shift = 0
                if not self._accepts_state(next_state, input_string, position + shift, memo):
                    all_accept = False
                    break
            if all_accept:
                memo[key] = True
                return True

        memo[key] = False
        return False
