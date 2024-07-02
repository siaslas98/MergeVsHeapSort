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
    plt.pause(0.001)

def init_plot(title):
    fig, ax = plt.subplots()
    ax.set_title(title)
    return fig, ax

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

        update_bars(arr, ax, fig, "Merge Sort")
    
    return arr

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

    # Use a smaller subset for visualization purposes
    stocks = stocks[:100]

    # Menu to choose sorting algorithm
    while True:
        print("Choose a sorting algorithm:")
        print("1. Merge Sort")
        print("2. Heap Sort")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            title = "Merge Sort"
            sort_function = merge_sort
            break
        elif choice == '2':
            title = "Heap Sort"
            sort_function = heap_sort
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    # Initialize the plot and show the initial graph
    fig, ax = init_plot(title)
    update_bars(stocks, ax, fig, f"{title} - Initial")

    # Prompt to start sorting
    start = input("Do you want to start sorting? (yes/no): ")
    if start.lower() == 'yes':
        start_time = time.time()
        sorted_stocks = sort_function(stocks.copy(), ax, fig)
        sort_time = time.time() - start_time
        print(f"{title} Time: {sort_time:.4f} seconds")
        plt.show()
    else:
        print("Sorting aborted.")
        plt.close()

if __name__ == "__main__":
    main()
