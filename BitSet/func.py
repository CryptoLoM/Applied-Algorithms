from main import BitSet
import time
import random

def generate_random_set(size, num_elements):
    bitset = BitSet(size)
    for _ in range(num_elements):
        bitset.insert(random.randint(0, size - 1))
    return bitset

# Функція для вимірювання часу виконання операцій
def measure_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    return time.perf_counter() - start_time

# Експериментальна оцінка часу роботи операцій
def run_experiment(set_size, num_trials, num_elements):
    results = {"insert": [], "search": [], "union": []}

    for _ in range(num_trials):
        A = generate_random_set(set_size, num_elements)
        B = generate_random_set(set_size, num_elements)

        # Вимірюємо час вставки елементу
        element = random.randint(0, set_size - 1)
        insert_time = measure_time(A.insert, element)
        results["insert"].append(insert_time)

        # Вимірюємо час пошуку елементу
        search_time = measure_time(A.search, element)
        results["search"].append(search_time)

        # Вимірюємо час об'єднання множин
        union_time = measure_time(A.union, B)
        results["union"].append(union_time)

    return results

    # Перевірка для елементу, який точно не може бути у множин
    non_existing_element = set_size + 1
    search_time_non_existing = measure_time(A.search, non_existing_element)
    results["search_non_existing"].append(search_time_non_existing)
