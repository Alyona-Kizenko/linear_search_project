import random
import time
import matplotlib.pyplot as plt

def linear_search(lst, target):
    """
    Линейный поиск элемента target в списке lst.
    Возвращает индекс элемента или -1, если элемент не найден.
    """
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

def test_search_on_100_elements():
    random_list = random.sample(range(1000), 100)
    test_values = [random_list[0], random_list[50], 1001] 
    print("Тесты поиска в списке из 100 элементов:")
    for val in test_values:
        idx = linear_search(random_list, val)
        print(f"Значение {val} найдено на индексе: {idx}")

def measure_time(n, target):
    lst = random.sample(range(n * 10), n)
    start = time.time()
    linear_search(lst, target)
    end = time.time()
    return end - start

def plot_performance():
    sizes = [10, 100, 1000, 5000, 10000]
    times = []
    for size in sizes:
      
        t = measure_time(size, -1)
        times.append(t)
        print(f"Размер: {size}, время поиска: {t:.6f} сек")
    plt.plot(sizes, times, marker='o')
    plt.title("Время выполнения линейного поиска")
    plt.xlabel("Размер списка")
    plt.ylabel("Время (сек)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    test_search_on_100_elements()
    plot_performance()
