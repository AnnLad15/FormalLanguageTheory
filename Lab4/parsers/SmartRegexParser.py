import logging

logger = logging.getLogger(__name__)

class SmartRegexParser:
    """
    Проверяет строку на соответствие регулярному выражению ^( (a\2a+(?=a)|b)* )\1+$
    Сперва ищет повторяющиеся подстроки (G1)\1+ .
    Затем проверяет подстроки (G1) на соответствие (a\2a+(?=a)|b)* методом обхода в глубину
    """
    def __init__(self, text):
        self.text = text
        self.n = len(text)

    def parse(self):
        """
        Парсит ^( (a\2a+(?=a)|b)* )\1+$.
        Сперва проверяет строку на повторения.

        пример:
        # abaa abaa abaa -> abaa
        # aaaa aaaa aaaa -> a, aa, aaa, aaaa, aaaaaa
        # abaaa -> нет повторений
        """
        if self.n < 2:
            return False



        # Перебрираем lenghts от 1 до n/2 без остатка
        for length in range(1, self.n // 2 + 1):
             if self.n % length == 0:
                 unit = self.text[:length]
                 multiplier = self.n // length
                 
                 # Проверяем что слово состоит из повторений 'unit'
                 if unit * multiplier == self.text:
                     # Проверяем 'unit' на соответствие Group 1: (a\2a+(?=a) | b)*
                     if self._validate_group1(unit):
                         logger.debug(f"result = True")
                         return True
                 else:
                     logger.debug(f"No repetitions for unit {unit}")
        logger.debug(f"result = False")
        return False

    def _validate_group1(self, text):
        """
        Проверяем 'text' на соответствие (a\2a+(?=a) | b)*
        """
        logger.debug(f"Validating group: {text}")
        n = len(text)
        if n == 0:
            return True

        # Стек для DFS (pos, last_g2)
        stack = [(0, None)] # * может быть ноль повторений
        
        iter = 0
        while stack:
            iter += 1
            logger.debug(f"iteration {iter}. stack: {stack}")
            pos, last_g2 = stack.pop()
            if logger.isEnabledFor(logging.DEBUG):
                s = text[:pos] + "_" + text[pos:]
                logger.debug(f"processing {pos} {last_g2}, string: {s}")
            
            if pos == n:
                logger.debug(f"True")
                return True
                
            # Ветка: 'b'
            if pos < n and text[pos] == 'b':
                logger.debug(f"branch b")
                logger.debug(f"push {pos + 1} b")
                stack.append((pos + 1, "b"))
                
            # Ветка: 'a\2a+(?=a)'
            if last_g2 is not None and pos < n and text[pos] == 'a':
                logger.debug(f"branch a")
                check_pos = pos + 1
                if text.startswith(last_g2, check_pos):
                    check_pos += len(last_g2)
                    
                    # Проверяем a+ (жадный)
                    a_count = 0
                    while (check_pos + a_count < n) and text[check_pos + a_count] == 'a':
                        a_count += 1
                    logger.debug(f"a_count= {a_count}")
                        
                    # Пробуем возможные длины k для a+, начиная с большего, до 1
                    for k in range(a_count, 0, -1):
                        after_a_pos = check_pos + k


                        # Проверяем предпросмотр (?=a)
                        is_lookahead_valid = False
                        # Следующий символ находится в строке, проверяе его на 'a'

                        if after_a_pos < n:
                            if text[after_a_pos] == 'a':
                                is_lookahead_valid = True
                        else:
                            # Следующий символ находится за пределами строки.
                            # В этом случае проверяем первый символ, так как строка повторится (\1+)
                            logger.debug(f"text[0]= {text[0]}")
                            if n > 0 and text[0] == 'a':
                                is_lookahead_valid = True
                                
                        if is_lookahead_valid:
                            new_segment = 'a' + last_g2 + ('a' * k)
                            logger.debug(f"push {after_a_pos} {new_segment}")
                            stack.append((after_a_pos, new_segment))
        logger.debug(f"False")                    
        return False
