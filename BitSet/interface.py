from func import run_experiment
import matplotlib.pyplot as plt
# Функція для побудови графіків
def plot_results(results, set_sizes):
    for operation in results.keys():
        times = [sum(results[operation][size]) / len(results[operation][size]) for size in set_sizes]
        plt.plot(set_sizes, times, label=operation)

    plt.xlabel('Розмір множини')
    plt.ylabel('Час виконання (сек)')
    plt.title('Оцінка часу операцій над множинами')
    plt.legend()
    plt.grid(True)
    plt.show()

# Налаштування параметрів експерименту
set_sizes = [1000, 5000, 10000, 50000, 100000]  # Розміри множин
num_trials = 1000  # Кількість спроб для кожної операції
num_elements = 1000  # Кількість елементів у випадковій множині

# Збір результатів
experiment_results = { "insert": {}, "search": {}, "union": {} }
for size in set_sizes:
    results = run_experiment(size, num_trials, num_elements)
    for operation in results:
        experiment_results[operation][size] = results[operation]

# Побудова графіків
plot_results(experiment_results, set_sizes)
