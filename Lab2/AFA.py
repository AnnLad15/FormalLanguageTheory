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
        key = (state, position)
        if key in memo:
            return memo[key]

        if position == len(input_string):
            result = state in self.final_states
            memo[key] = result
            return result

        symbol = input_string[position]
        if symbol not in self.input_symbols:
            memo[key] = False
            return False

        if state not in self.transitions or symbol not in self.transitions[state]:
            memo[key] = False
            return False

        clauses = self.transitions[state][symbol]

        for clause in clauses:
            all_accept = True
            for next_state in clause:
                if not self._accepts_state(next_state, input_string, position + 1, memo):
                    all_accept = False
                    break
            if all_accept:
                memo[key] = True
                return True

        memo[key] = False
        return False
