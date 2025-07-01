from multiprocessing import Pool

# Pool: Manages a pool of worker processes for parallel task execution,
# ideal for distributing work across multiple processes.

def square(n):
    """Function to square a number."""
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    with Pool(processes=10) as pool:
        results = pool.map(square, numbers)

    print(f"Squared results: {results}")