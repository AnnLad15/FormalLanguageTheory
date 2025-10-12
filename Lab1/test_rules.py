def get_initials_rules():
    return [
        ("ac", "c"),
        ("aa", "ba"),
        ("bc", "c"),
        ("ca", "aa"),
        ("cb", "bc"),
        ("ccc", "c"),
        ("aaa", "aa"),
        ("aab", "ba"),
        #("abb", "aba"),
        #("bbb", "bba"),
        ("aba", "abb"),
        ("bba", "bbb"),
    ]

def get_new_rules():
    return [
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
        ("cc", "c"),
        ("abb", "bbb"),
        ("bbb", "ba"),
        ("bab", "ba"),
        ("ba", "c"),
    ]

def get_alphabet():
    return ['a', 'b', 'c']
