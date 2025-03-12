import time
import concurrent.futures


def task(n):
    """Simulates a time-consuming task."""
    count = 0
    for i in range(n):
        count += 1
    return count


def sequential_run(func, iterations, n):
    """Executes a function sequentially and measures the time."""
    start_time = time.time()
    for _ in range(iterations):
        func(n)
    end_time = time.time()
    return end_time - start_time


def parallel_run(func, iterations, n):
    """Executes a function in parallel using ThreadPoolExecutor and measures the time."""
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(func, n) for _ in range(iterations)]
        concurrent.futures.wait(futures)
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    iterations = 1000
    n = 10000

    sequential_time = sequential_run(task, iterations, n)
    parallel_time = parallel_run(task, iterations, n)

    print(f"Sequential execution time: {sequential_time:.4f} seconds")
    print(f"Parallel execution time: {parallel_time:.4f} seconds")




