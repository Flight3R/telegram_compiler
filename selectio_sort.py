import random
import time
import statistics
import matplotlib.pyplot as plt

def sortowanie_przez_wybieranie(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def sortowanie_przez_wybieranie_optymalne(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

liczba_probek = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

czasy_wykonania = []
czasy_wykonania_optymalne = []

for probka in liczba_probek:
    czasy_probki = []
    czasy_probki_optymalne = []
    for proba in range(10):
        arr = [random.randint(0, 1000) for _ in range(probka)]
        
        start_time = time.time()
        sortowanie_przez_wybieranie(arr)
        end_time = time.time()
        czas_wykonania = end_time - start_time
        czasy_probki.append(czas_wykonania)

        start_time = time.time()
        sortowanie_przez_wybieranie_optymalne(arr)
        end_time = time.time()
        czas_wykonania_optymalne = end_time - start_time
        czasy_probki_optymalne.append(czas_wykonania_optymalne)

        print(f'Próba {1 + proba} dla próbki {probka}')

    czasy_wykonania.append(czasy_probki)
    czasy_wykonania_optymalne.append(czasy_probki_optymalne)

srednie_czasy_wykonania = [statistics.mean(czasy) for czasy in czasy_wykonania]
odchylenia_standardowe_czasow = [statistics.stdev(czasy) for czasy in czasy_wykonania]
srednie_czasy_wykonania_optymalne = [statistics.mean(czasy) for czasy in czasy_wykonania_optymalne]
odchylenia_standardowe_czasow_optymalne = [statistics.stdev(czasy) for czasy in czasy_wykonania_optymalne]

# Wyświetlanie statystyk
for i, probka in enumerate(liczba_probek):
    print(f'Średni czas wykonania dla próbki {probka}:')
    print(f'Sortowanie przez wybieranie: {srednie_czasy_wykonania[i]:.6f} ± {odchylenia_standardowe_czasow[i]:.6f} s')
    print(f'Optymalizowane sortowanie przez wybieranie: {srednie_czasy_wykonania_optymalne[i]:.6f} ± {odchylenia_standardowe_czasow_optymalne[i]:.6f} s')
    print()

# Tworzenie wykresów
plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, srednie_czasy_wykonania, yerr=odchylenia_standardowe_czasow, fmt='-o', label='Sortowanie przez wybieranie')
plt.errorbar(liczba_probek, srednie_czasy_wykonania_optymalne, yerr=odchylenia_standardowe_czasow_optymalne, fmt='-o', label='Optymalizowane sortowanie przez wybieranie')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, srednie_czasy_wykonania, yerr=odchylenia_standardowe_czasow, fmt='-o', label='Sortowanie przez wybieranie')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek - Sortowanie przez wybieranie')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, srednie_czasy_wykonania_optymalne, yerr=odchylenia_standardowe_czasow_optymalne, fmt='-o', label='Optymalizowane sortowanie przez wybieranie' , color='orange')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek - Optymalizowane sortowanie przez wybieranie')
plt.legend()
plt.grid(True)
plt.show()
