import numpy as np
import time
import random



def _fill_list(iterations=10**7):
    return np.random.randint(1, 101, size=iterations).tolist()

def python_time():
    addiction, multiplication = [], []
    for _ in range(100):
        arr1 = _fill_list()
        
        start = time.perf_counter()
        result1 = [x + x for x in arr1]
        end = time.perf_counter()
        add = end-start
        addiction.append(add)

        start = time.perf_counter()
        result1 = [x*5 for x in arr1]
        end = time.perf_counter()
        mult = end-start
        multiplication.append(mult)

        
    return addiction, multiplication

def numpy_time():
    addiction, multiplication = [], []
    for _ in range(100):
        arr1 = np.array(_fill_list())
        
        start = time.perf_counter()
        result1 = arr1 + arr1
        end = time.perf_counter()
        add = end-start

        addiction.append(add)

        start = time.perf_counter()
        result1 = arr1*5
        end = time.perf_counter()
        mult = end-start

        multiplication.append(mult)

        
    return addiction, multiplication

if __name__ == "__main__":
    add, mult = python_time()
    python_mean_add = round(np.mean(add), 7)
    python_mean_mult = round(np.mean(mult), 7)
    print(f"Python addition time: {python_mean_add}")
    print(f"Python multiplication time: {python_mean_mult}")
    add, mult = numpy_time()
    numpy_add = round(np.mean(add), 7)
    numpy_mult = round(np.mean(mult), 7)
    print(f"Numpy addition time: {numpy_add}")
    print(f"Numpy multiplication time: {numpy_mult}")

    print(f"Addition differential:{python_mean_add/numpy_add}")
    print(f"Multiplication differential:{python_mean_mult/numpy_mult}")