import logging
import time
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

logger = logging.getLogger(__name__)

class FuzzTester:
    def __init__(self, generator, parsers):
        """
        Args:
            generator: объект с методом generate(), возвращающим строку
            parsers: список классов парсеров,
                     которые можно инстанциировать так: Parser(text)
                     и у которых есть метод parse()
        """
        self.generator = generator
        self.parsers = parsers
        self.results = {}
        self.history = []



    def run_tests(self, num_samples=10):
        logger.debug(f"--- Starting Fuzz Test: {num_samples} samples ---")
        

        for i in range(num_samples):
            word = self.generator.generate()
            logger.debug(f"\n[Sample {i+1}] Word: '{word}'")

            iteration_times = {}

            
            # Запускаем каждый парсер
            for parser_cls in self.parsers:
                parser_name = parser_cls.__name__
                
                # Создаем экземпляр
                parser_instance = parser_cls(word)
                
                # Замеряем время
                start_time = time.perf_counter()
                result = parser_instance.parse()
                end_time = time.perf_counter()
                
                duration = end_time - start_time
                
                # Сохраняем результат
                record = {
                    "parser": parser_name,
                    "result": result,
                    "time": duration
                }
                if word not in self.results:
                    self.results[word] = []
                self.results[word].append(record)
                iteration_times[parser_name] = duration

                
                logger.debug(f"  {parser_name}: {result} ({duration:.6f}s)")
            
            self.history.append(iteration_times)
        logger.debug(f"history {self.history}, result {self.results}")

    def get_mismatches(self, expected_res):
        """
        Возвращает словарь {word: [record1, record2, ...]},
        для слов где парсеры дали ответ отличный от ожидаемого (expected_res)
        """
        mismatches = {}
        for word, records in self.results.items():
            if not records:
                continue

            # Проверяет, отличается ли какой-либо результат парсера для этого слова от первого.
            is_mismatch = any(rec["result"] != expected_res for rec in records)
            
            if is_mismatch:
                mismatches[word] = records
        return mismatches

    def plot_execution_time(self):
        """
        Строит график времени выполнения для каждого парсера для всех итераций
        (итерация - x , время выполнения - y)
        """
        if not HAS_MATPLOTLIB:
            logger.warning("[WARNING] matplotlib not found. Cannot plot execution times.")
            return

        if not self.history:
            logger.debug("No history to plot.")
            return
            
        # Подготавливаем данные по каждому парсеру
        parser_times = {p.__name__: [] for p in self.parsers}
        
        for run_data in self.history:
            for p_cls in self.parsers:
                p_name = p_cls.__name__
                parser_times[p_name].append(run_data.get(p_name, 0))

        # Строим график
        x_axis = range(1, len(self.history) + 1)

        
        plt.figure(figsize=(10, 6))
        
        for p_name, times in parser_times.items():
            plt.plot(x_axis, times, marker='o', label=p_name)
            
        plt.title("Время выполнения парсеров по итерции")
        plt.xlabel("Номер итерации")
        plt.ylabel("Время (сек.)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_average_execution_time(self):
        """
        Рисует диаграмму среднего время выполнения
        """
        if not HAS_MATPLOTLIB:
            logger.warning("[WARNING] matplotlib not found. Cannot plot average execution times.")
            return

        if not self.history:
            logger.debug("No history to plot.")
            return
            
        # Считаем среднее время по парсерам
        parser_data = []
        
        for p in self.parsers:
            p_name = p.__name__
            total_time = 0
            count = 0
            for run_data in self.history:
                if run_data[p_name]:
                    total_time += run_data[p_name]
                    count += 1
            
            avg = total_time / count if count > 0 else 0
            parser_data.append((p_name, avg))

        # Сортирует по avg
        parser_data.sort(key=lambda x: x[1])
        
        sorted_names = [x[0] for x in parser_data]
        sorted_times = [x[1] for x in parser_data]

        # Рисуем
        plt.figure(figsize=(10, 6))
        # Задаем цвета столбцов
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
        
        plt.bar(sorted_names, sorted_times, color=colors)
        
        plt.title("Среднее время выполнения каждого парсера")
        plt.xlabel("Парсер")
        plt.ylabel("Среднее время (сек)")
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
