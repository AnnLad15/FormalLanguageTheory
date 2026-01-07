class NFA:
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def accepts_input(self, input_string):
        cur_states = {self.initial_state}
        for i in input_string:
            #print(i)
            next_states = set()
            for c in cur_states:
                if self.transitions[c] and i in self.transitions[c]:
                    next_states.update(self.transitions[c][i])

            if len(next_states) == 0:
                return False

            cur_states = next_states

        if len(cur_states & self.final_states) != 0:
            return True

        return False
