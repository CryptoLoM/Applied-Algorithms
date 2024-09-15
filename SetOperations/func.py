from main import SetOperations
import time
import random


def generate_random_set(t, num_elements):
    my_set = SetOperations(t)
    for _ in range(num_elements):
        my_set.insert(random.randint(0, 64 * t - 1))  # Вставляємо випадковий елемент
    return my_set

def measure_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    return time.perf_counter() - start_time

def run_experiment(set_size, num_trials, num_elements):
    results = {"insert": [], "search": [], "union": [], "search_non_existing": []}

    for _ in range(num_trials):
        A = generate_random_set(set_size, num_elements)
        B = generate_random_set(set_size, num_elements)

        # Вимірюємо час вставки елементу
        element = random.randint(0, 64 * set_size - 1)
        insert_time = measure_time(A.insert, element)
        results["insert"].append(insert_time)

        # Вимірюємо час пошуку елементу
        search_time = measure_time(A.search, element)
        results["search"].append(search_time)

        # Вимірюємо час об'єднання множин
        union_time = measure_time(A.union, B)
        results["union"].append(union_time)

        # Вимірюємо час пошуку елементу, якого немає у множині
        non_existing_element = 64 * set_size  # Це точно не існуючий елемент
        search_non_existing_time = measure_time(A.search, non_existing_element)
        results["search_non_existing"].append(search_non_existing_time)

    return results
