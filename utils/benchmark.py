import time

def benchmark(func, *args, **kwargs):
    """
    Benchmark the execution time of a function.
    """

    start_time = time.time()
    result = func(*args, **kwargs)
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
    return result