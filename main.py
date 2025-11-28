import numpy as np
import time
import random



def _fill_list(iterations=10**7):
    data = []
    for _ in range(round(iterations)):
        data.append(random.randint(1, 10**4))
    return data


if __name__ == "__main__":
    arr1 = _fill_list()

    # python
    start = time.time()
    result1 = [x + x for x in arr1]
    end = time.time()
    print(f"Standard python addiction time: {end-start}") 
    
    start = time.time()
    result1 = [x*5 for x in arr1]
    end = time.time()
    print(f"Standard python multiplication time: {end-start}") 
    
    # Numpy
    np_arr1 = np.array(arr1)

    start = time.time()
    result2 = np_arr1 + np_arr1
    end = time.time()
    print(f"Numpy addiction time: {end-start}") 
    
    start = time.time()
    result = arr1 * 5
    end = time.time()
    print(f"Numpy multiplication time: {end-start}") 