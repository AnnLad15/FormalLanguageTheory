import logging

logger = logging.getLogger(__name__)

class NaiveRegexParser:
    """
    Наивный парсер регулярного выражения ^( (a\2a+(?=a)|b)* )\1+$
    с использованием рекурсивного разбора с возвратом
    """
    def __init__(self, text):
        self.text = text
        self.n = len(text)

    def parse(self):
        """
        Получает список совпадений с (a\2a+(?=a)|b)*
        и каждое проверяет на повторение в хвосте (\1+)
        """
        # Получить все возможные варианты группы 1
        # формат (pos, g1_content)
        all_g1_matches = self._parse_group_1_loop(0, "", None)

        for pos, g1_content in all_g1_matches:
            if not g1_content:
                continue

            if self._check_tail(pos, g1_content):
                return True

        return False

    def _parse_group_1_loop(self, pos, current_g1, last_g2):
        """
        Рекурсивного разбора с возвратом.
        Возвращает список всех результатов вида (pos, current_g1), соответствующих группе G1,
        где pos - позиция в строке после найденной группы,
        current_g1 - найденная группа G1.
        """
        logger.debug(f"_parse_group_1_loop({pos}, {current_g1}, {last_g2})")
        results = []
        
        # Добавляем результат
        results.append((pos, current_g1))

        # Продолжаем цикл
        # --- Ветка: 'b' ---
        if pos < self.n and self.text[pos] == 'b':
            sub_results = self._parse_group_1_loop(
                pos + 1,
                current_g1 + "b",
                "b"
            )
            results.extend(sub_results)

        # --- Ветка: a\2a+(?=a) ---
        if last_g2 is not None and pos < self.n and self.text[pos] == 'a':
            check_pos = pos + 1
            if self.text.startswith(last_g2, check_pos):
                check_pos += len(last_g2)

                # Проверяем a+ (жадный)
                a_count = 0
                while (check_pos + a_count < self.n) and self.text[check_pos + a_count] == 'a':
                    a_count += 1

                for k in range(a_count, 0, -1):
                    after_a_pos = check_pos + k

                    # опережающая проверка
                    if after_a_pos < self.n and self.text[after_a_pos] == 'a':
                        segment = 'a' + last_g2 + ('a' * k)
                        
                        sub_results = self._parse_group_1_loop(
                            after_a_pos,
                            current_g1 + segment,
                            segment
                        )
                        results.extend(sub_results)
        logger.debug(f"result = {results}")
        return results


    def _check_tail(self, pos, pattern):
        """
        Проверка хвоста.
        Хвост должен состоять из повторений pattern одного или более раз.
        """
        logger.debug(f"_check_tail {pos}, {pattern}")
        if pos == self.n:
            return False

        current_pos = pos
        while current_pos < self.n:
            if self.text.startswith(pattern, current_pos):
                current_pos += len(pattern)
            else:
                return False
        return True
