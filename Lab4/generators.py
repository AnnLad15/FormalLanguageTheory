import random
import logging

logger = logging.getLogger(__name__)

class RandomABGenerator:
    """
    Генерируем случайную строку из 'a' и 'b'
    """
    def __init__(self, min_len=1, max_len=10):
        self.min_len = min_len
        self.max_len = max_len

    def generate(self):
        while True:
            length = random.randint(self.min_len, self.max_len)
            # Генерируем случайную строку из 'a' и 'b'
            s = "".join(random.choice("ab") for _ in range(length))
            # Условие: кроме слов состоящих только из 'b'
            if "a" in s:
                return s

class DeepRecursiveGenerator:
    """
    Генерирует строку соответствующую группе 1, с заданным кол-вом повторений
    """
    def __init__(self, min_depth=1, max_depth=10, repeats=1):
        self.min_depth = min_depth
        self.max_depth = max_depth
        self.repeats = repeats

    def generate(self):
        s = "b"
        g2 = "b"  
        depth = random.randint(self.min_depth, self.max_depth)
 
        for _ in range(depth):
            a_length = random.randint(1, 10)
            g2 = "a" + g2 + "a" * a_length
            s = s + g2

        return s * self.repeats

class AllBGenerator:
    """
    Генирируем строку вида bb+ (аналог выражения ( (a\2a+(?=a)|b)* )\1+)
    """
    def __init__(self, min_len=1, max_len=10):
        self.min_len = min_len
        self.max_len = max_len

    def generate(self):
        length = random.randint(self.min_len, self.max_len)
        return "b" * length
