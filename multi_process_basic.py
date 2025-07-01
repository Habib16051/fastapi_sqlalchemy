import multiprocessing
import time

# A simple example of using multiprocessing.Process to run a function in parallel:
# Process: Represents a single process. You can create and manage individual processes.
def worker(number):
    print(f"Worker {number} started!")
    time.sleep(1)
    print(f"Worker {number} finished!")


if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes done!")