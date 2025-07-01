from multiprocessing import Process, Queue

# A simple example of using multiprocessing.Queue to share data between processes:
# Queue: A thread- and process-safe way to share data between processes.

def producer(queue):
    """Function to produce data and put it in the queue."""
    for i in range(5):
        queue.put(i)
        print(f"Producing {i}")

def consumer(queue):
    while True:
        item = queue.get()
        print(f"Consuming {item}")
        if item == 4:  # Assuming 4 is the sentinel value to stop
            break

if __name__ == "__main__":
    queue = Queue()
    producer_process = Process(target=producer, args=(queue,))
    consumer_process = Process(target=consumer, args=(queue,))
    # Start the producer and consumer processes
    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()
