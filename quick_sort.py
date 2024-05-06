import random
import time
import statistics
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quicksort_opt(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_opt(arr, low, pi)
        quicksort_opt(arr, pi + 1, high)

liczba_probek  = list(range(10000, 60000 + 1, 1000))

czasy_wykonania = []
czasy_wykonania_opt = []

for probka in liczba_probek:
    czasy_probki = []
    czasy_probki_opt = []
    for proba in range(10):
        arr = [random.randint(0, 1000) for _ in range(probka)]
        
        start_time = time.time()
        quicksort_opt(arr, 0, len(arr) - 1)
        end_time = time.time()
        czas_wykonania = end_time - start_time
        czasy_probki.append(czas_wykonania)

        start_time = time.time()
        quicksort(arr)
        end_time = time.time()
        czas_wykonania_opt = end_time - start_time
        czasy_probki_opt.append(czas_wykonania_opt)

        print(f'Próba {1 + proba} dla próbki {probka}')

    czasy_wykonania.append(czasy_probki)
    czasy_wykonania_opt.append(czasy_probki_opt)

avg_czasy_wykonania_merge = [statistics.mean(czasy) for czasy in czasy_wykonania]
odchylenie_std_czasow_wykonania_merge = [statistics.stdev(czasy) for czasy in czasy_wykonania]
avg_czasy_wykonania_quick_opt = [statistics.mean(czasy) for czasy in czasy_wykonania_opt]
odchylenie_std_czasow_wykonania_quick_opt = [statistics.stdev(czasy) for czasy in czasy_wykonania_opt]

# Wyświetlanie statystyk w konsoli
for i, probka in enumerate(liczba_probek):
    print(f'Średni czas wykonania dla próbki {probka}:')
    print(f'Sortowanie szybkie: {avg_czasy_wykonania_merge[i]:.6f} ± {odchylenie_std_czasow_wykonania_merge[i]:.6f} s')
    print(f'Optymalizowane sortowanie szybkie: {avg_czasy_wykonania_quick_opt[i]:.6f} ± {odchylenie_std_czasow_wykonania_quick_opt[i]:.6f} s')
    print()

# Rysowanie wykresów
plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, avg_czasy_wykonania_merge, yerr=odchylenie_std_czasow_wykonania_merge, fmt='-o', label='Quicksort')
plt.errorbar(liczba_probek, avg_czasy_wykonania_quick_opt, yerr=odchylenie_std_czasow_wykonania_quick_opt, fmt='-o', label='Optymalizowane quicksort')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, avg_czasy_wykonania_merge, yerr=odchylenie_std_czasow_wykonania_merge, fmt='-o', label='Quicksort')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek - Quicksort')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, avg_czasy_wykonania_quick_opt, yerr=odchylenie_std_czasow_wykonania_quick_opt, fmt='-o', label='Optymalizowane quicksort', color='orange')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek - Optymalizowane quicksort')
plt.legend()
plt.grid(True)
plt.show()
