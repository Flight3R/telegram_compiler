import random
import time
import statistics
import matplotlib.pyplot as plt

def bubble_sort_opt(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

nof_samples = [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]

execution_times = []
execution_times_opt = []

for sample in nof_samples:
    sample_times = []
    sample_times_opt = []
    for attempt in range(10):
        arr = [random.randint(0, 1000) for _ in range(sample)]
        
        start_time = time.time()
        bubble_sort(arr)
        end_time = time.time()
        execution_time = end_time - start_time
        sample_times.append(execution_time)

        start_time = time.time()
        bubble_sort_opt(arr)
        end_time = time.time()
        execution_time_opt = end_time - start_time
        sample_times_opt.append(execution_time_opt)

        print(f'Attempt {1 + attempt} for sample {sample}')

    execution_times.append(sample_times)
    execution_times_opt.append(sample_times_opt)

avg_execution_times = [statistics.mean(times) for times in execution_times]
std_dev_execution_times = [statistics.stdev(times) for times in execution_times]
avg_execution_times_opt = [statistics.mean(times) for times in execution_times_opt]
std_dev_execution_times_opt = [statistics.stdev(times) for times in execution_times_opt]

# Printing statistics in Polish in the command line
for i, sample in enumerate(nof_samples):
    print(f'Średni czas wykonania dla próbki {sample}:')
    print(f'Sortowanie bąbelkowe: {avg_execution_times[i]:.6f} ± {std_dev_execution_times[i]:.6f} s')
    print(f'Optymalizowane sortowanie bąbelkowe: {avg_execution_times_opt[i]:.6f} ± {std_dev_execution_times_opt[i]:.6f} s')
    print()

# Plotting the graphs
plt.figure(figsize=(10, 6))
plt.errorbar(nof_samples, avg_execution_times, yerr=std_dev_execution_times, fmt='-o', label='Sortowanie bąbelkowe')
plt.errorbar(nof_samples, avg_execution_times_opt, yerr=std_dev_execution_times_opt, fmt='-o', label='Optymalizowane sortowanie bąbelkowe')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(nof_samples, avg_execution_times, yerr=std_dev_execution_times, fmt='-o', label='Sortowanie bąbelkowe')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek - Sortowanie bąbelkowe')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.errorbar(nof_samples, avg_execution_times_opt, yerr=std_dev_execution_times_opt, fmt='-o', label='Optymalizowane sortowanie bąbelkowe', color='orange')
plt.xlabel('Liczba próbek')
plt.ylabel('Czas wykonania (s)')
plt.title('Czas wykonania w zależności od liczby próbek - Sortowanie bąbelkowe')
plt.legend()
plt.grid(True)
plt.show()