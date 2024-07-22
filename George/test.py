import csv
import time
import matplotlib.pyplot as plt
import numpy as np

def read_csv(filename):
    stocks = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stocks.append((row['Stock Name'], float(row['Price'])))
    return stocks

def update_bars(arr, ax, fig, title):
    ax.clear()
    ax.bar(np.arange(len(arr)), [x[1] for x in arr], color='blue')
    ax.set_title(title)
    plt.pause(0.0000000001)

def init_plot(title):
    fig, ax = plt.subplots()
    ax.set_title(title)
    return fig, ax

# algorithm for merge sort
# Below is stolen code (CHANGE IT)
def merge_sort(arr, ax, fig):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, ax, fig)
        merge_sort(R, ax, fig)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][1] < R[j][1]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        # update the graph
        update_bars(arr, ax, fig, "Merge Sort")
    
    return arr

# algorithm to heapify
# Below is stolen code (CHANGE IT)
def heapify(arr, n, i, ax, fig):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i][1] < arr[left][1]:
        largest = left

    if right < n and arr[largest][1] < arr[right][1]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, ax, fig)

# algorithm to for heap sort
# Below is stolen code (CHANGE IT)
def heap_sort(arr, ax, fig):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, ax, fig)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, ax, fig)
        update_bars(arr, ax, fig, "Heap Sort")
    
    return arr

def main():
    # Read the CSV file
    stocks = read_csv('stocks_100k.csv')

    # Uses a smaller subset for visualization purposes
    # change the number of stocks to be sorted
    stocks = stocks[:1000]

    # Menu to choose sorting algorithm
    while True:
        print("Choose a sorting algorithm:")
        print("1. Merge Sort")
        print("2. Heap Sort")
        print("3. Show Both (Merge Sort and Heap Sort)")
        choice = input("Enter 1, 2, or 3: ")

        if choice == '1':
            title = "Merge Sort"
            sort_functions = [merge_sort]
            break
        elif choice == '2':
            title = "Heap Sort"
            sort_functions = [heap_sort]
            break
        elif choice == '3':
            title = "Merge Sort and Heap Sort"
            sort_functions = [merge_sort, heap_sort]
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Initialize the plots
    figs = []
    axs = []
    for sort_function in sort_functions:
        fig, ax = init_plot(f"{sort_function.__name__}")
        figs.append(fig)
        axs.append(ax)
        update_bars(stocks, ax, fig, f"{sort_function.__name__} - Initial")

    # Prompt to start sorting
    start = input("Do you want to start sorting? (yes/no): ")
    if start.lower() == 'yes':
        start_time = time.time()
        for i, sort_function in enumerate(sort_functions):
            sorted_stocks = sort_function(stocks.copy(), axs[i], figs[i])
            sort_time = time.time() - start_time
            # printing the time difference
            print(f"{sort_function.__name__} Time: {sort_time:.4f} seconds")

        plt.show()
    else:
        print("Sorting aborted.")
        plt.close()

if __name__ == "__main__":
    main()
