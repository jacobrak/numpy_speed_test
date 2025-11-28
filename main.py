import numpy as np
import time
import random



def _fill_list():
    data = []
    for _ in range(1000):
        data.append(random.randint(1, 2**8))
    return data
