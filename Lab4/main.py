import logging
from parsers.FastRegexParser import FastRegexParser
from parsers.SmartRegexParser import SmartRegexParser
from parsers.NaiveRegexParser import NaiveRegexParser
from FuzzTester import FuzzTester

from generators import RandomABGenerator, AllBGenerator, DeepRecursiveGenerator

logger = logging.getLogger(__name__)


def run_execution(parsers, generator, expected_res, num_samples, title):
    logger.info(f"--- {title} ---")
    fuzz = FuzzTester(generator, parsers)
    fuzz.run_tests(num_samples=num_samples)
    fuzz.plot_execution_time()
    fuzz.plot_average_execution_time()

    # Проверка mismatches (различий в тестах)
    mismatches = fuzz.get_mismatches(expected_res)
    if mismatches:
        logger.error(f"Found {len(mismatches)} mismatches in {title}:")
        for w, res in list(mismatches.items())[:5]:
            logger.error(f"Word: {w}, Expected result: {expected_res}, Results: {res}")
    else:
        logger.info(f"No mismatches in {title}.")


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #logging.getLogger(FuzzTester.__module__).setLevel(logging.DEBUG)

    parsers = [
        NaiveRegexParser,
        SmartRegexParser,
        FastRegexParser,
    ]

    # 1. Рандомные (неверные) тесты
    run_execution(parsers, RandomABGenerator(min_len=100, max_len=2000), False, 50, "Random Invalid Fuzzing")

    # 2. Генерится строка типа (b aba+ aaba+a+ ...)*n
    run_execution(parsers, DeepRecursiveGenerator(repeats=3), False, 50, "Deep recursion (invalid) fuzzing - 3 repeats")
    run_execution(parsers, DeepRecursiveGenerator(repeats=1), False, 50, "Deep recursion (invalid) fuzzing - no repeats")

    # 3. Рандомные (верные) тесты, где строка соответствует регулярному выражению bb+
    run_execution(parsers, AllBGenerator(min_len=2, max_len=100), True, 50, "Random Valid Generator Fuzzing")


if __name__ == "__main__":
    main()
