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
    print(len(result1))
    print(f"Standard python: {end-start}") 

    # Numpy
    np_arr1 = np.array(arr1)


    start = time.time()

    result2 = np_arr1 + np_arr1
    end = time.time()
    print(f"Numpy time: {end-start}") 
    print(result1 == result2)