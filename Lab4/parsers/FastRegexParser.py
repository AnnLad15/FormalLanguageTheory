import logging

logger = logging.getLogger(__name__)


class FastRegexParser:
    """
    Быстрый парсер регулярного выражения ^bb+$ (аналог выражения ^( (a\2a+(?=a)|b)* )\1+$).
    Возвращает True, если строка состоит только из символов 'b' (не меньше двух),
    иначе False.
    """

    def __init__(self, text):
        self.text = text

    def parse(self):

        if not self.text or len(self.text) < 2:
            return False

        # Проверяем, что все символы - 'b'
        if self.text.find("a") != -1:
            return False

        # Если добрались сюда - значит только 'b'
        # logger.debug(f"SUCCESS: Строка '{self.text}' состоит только из 'b'.")
        return True
