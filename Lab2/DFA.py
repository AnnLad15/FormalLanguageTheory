class DFA:
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def accepts_input(self, input_string):
        cur_state = self.initial_state
        for i in input_string:
            #print(i)
            if self.transitions[cur_state] and i in self.transitions[cur_state]:
                cur_state = self.transitions[cur_state][i]
                #print(cur_state)
            else:
                return False

        if cur_state in self.final_states:
            return True

        return False
