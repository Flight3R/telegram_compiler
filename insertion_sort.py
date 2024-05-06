import random
import time
import statistics
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def insertion_sort_opt(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

liczba_probek = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

execution_times = []
execution_times_opt = []

for sample in liczba_probek:
    sample_times = []
    sample_times_opt = []
    for attempt in range(10):
        arr = [random.randint(0, 1000) for _ in range(sample)]
        
        start_time = time.time()
        insertion_sort(arr)
        end_time = time.time()
        execution_time = end_time - start_time
        sample_times.append(execution_time)

        start_time = time.time()
        insertion_sort_opt(arr)
        end_time = time.time()
        execution_time_opt = end_time - start_time
        sample_times_opt.append(execution_time_opt)

        print(f'Próba {1 + attempt} dla próbki {sample}')

    execution_times.append(sample_times)
    execution_times_opt.append(sample_times_opt)

avg_execution_times = [statistics.mean(times) for times in execution_times]
std_dev_execution_times = [statistics.stdev(times) for times in execution_times]
avg_execution_times_opt = [statistics.mean(times) for times in execution_times_opt]
std_dev_execution_times_opt = [statistics.stdev(times) for times in execution_times_opt]

# Printing statistics in Polish in the command line
for i, sample in enumerate(liczba_probek):
    print(f'Średni czas wykonania dla próbki {sample}:')
    print(f'Sortowanie przez wstawianie: {avg_execution_times[i]:.6f} ± {std_dev_execution_times[i]:.6f} s')
    print(f'Optymalizowane sortowanie przez wstawianie: {avg_execution_times_opt[i]:.6f} ± {std_dev_execution_times_opt[i]:.6f} s')
    print()

# Plotting the graphs
plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, avg_execution_times, yerr=std_dev_execution_times, fmt='-o', label='Sortowanie przez wstawianie')
plt.errorbar(liczba_probek, avg_execution_times_opt, yerr=std_dev_execution_times_opt, fmt='-o', label='Optymalizowane sortowanie przez wstawianie')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, avg_execution_times, yerr=std_dev_execution_times, fmt='-o', label='Sortowanie przez wstawianie')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek - Sortowanie przez wstawianie')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(liczba_probek, avg_execution_times_opt, yerr=std_dev_execution_times_opt, fmt='-o', label='Optymalizowane sortowanie przez wstawianie', color='orange')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek - Optymalizowane sortowanie przez wstawianie')
plt.legend()
plt.grid(True)
plt.show()
