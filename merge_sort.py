import random
import time
import statistics
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    
    while len(left) > 0:
        result.append(left[0])
        left = left[1:]
    
    while len(right) > 0:
        result.append(right[0])
        right = right[1:]
    
    return result

def merge_sort_opt(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort_opt(left_half)
    right_half = merge_sort_opt(right_half)
    
    return merge_opt(left_half, right_half)

def merge_opt(left, right):
    result = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

liczba_probek = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]

czasy_wykonania = []
czasy_wykonania_opt = []

for probka in liczba_probek:
    czasy_probki = []
    czasy_probki_opt = []
    for proba in range(10):
        arr = [random.randint(0, 1000) for _ in range(probka)]
        
        start_time = time.time()
        merge_sort(arr)
        end_time = time.time()
        czas_wykonania = end_time - start_time
        czasy_probki.append(czas_wykonania)

        start_time = time.time()
        merge_sort_opt(arr)
        end_time = time.time()
        czas_wykonania_opt = end_time - start_time
        czasy_probki_opt.append(czas_wykonania_opt)

        print(f'Próba {1 + proba} dla próbki {probka}')

    czasy_wykonania.append(czasy_probki)
    czasy_wykonania_opt.append(czasy_probki_opt)

avg_czasy_wykonania = [statistics.mean(czasy) for czasy in czasy_wykonania]
odchylenie_std_czasow_wykonania = [statistics.stdev(czasy) for czasy in czasy_wykonania]
avg_czasy_wykonania_opt = [statistics.mean(czasy) for czasy in czasy_wykonania_opt]
odchylenie_std_czasow_wykonania_opt = [statistics.stdev(czasy) for czasy in czasy_wykonania_opt]

# Wyświetlanie statystyk w konsoli
for i, probka in enumerate(liczba_probek):
    print(f'Średni czas wykonania dla próbki {probka}:')
    print(f'Sortowanie przez scalanie: {avg_czasy_wykonania[i]:.6f} ± {odchylenie_std_czasow_wykonania[i]:.6f} s')
    print(f'Optymalizowane sortowanie przez scalanie: {avg_czasy_wykonania_opt[i]:.6f} ± {odchylenie_std_czasow_wykonania_opt[i]:.6f} s')
    print()

# Rysowanie wykresów
plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, avg_czasy_wykonania, yerr=odchylenie_std_czasow_wykonania, fmt='-o', label='Sortowanie przez scalanie')
plt.errorbar(liczba_probek, avg_czasy_wykonania_opt, yerr=odchylenie_std_czasow_wykonania_opt, fmt='-o', label='Optymalizowane sortowanie przez scalanie')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, avg_czasy_wykonania, yerr=odchylenie_std_czasow_wykonania, fmt='-o', label='Sortowanie przez scalanie')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek - Sortowanie przez scalanie')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, avg_czasy_wykonania_opt, yerr=odchylenie_std_czasow_wykonania_opt, fmt='-o', label='Optymalizowane sortowanie przez scalanie', color='orange')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek - Optymalizowane sortowanie przez scalanie')
plt.legend()
plt.grid(True)
plt.show()
