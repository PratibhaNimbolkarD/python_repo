import numpy as np
import logging

logging.basicConfig(level=logging.INFO , format= '%(message)s')
def min_max():



    n, _ = map(int, input().split())

    x = np.array([input().split() for _ in range(n)], int)
    logging.info(np.max(np.min(x, axis=1)))
    return (np.max(np.min(x, axis=1)))