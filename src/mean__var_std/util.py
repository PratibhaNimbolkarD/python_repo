import numpy as np
import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')
def mean_var_std():
    n, m = list(map(int, input().split()))
    arr = np.array([input().split() for i in range(n)], dtype=int)
    logging.info(np.mean(arr, axis=1))
    logging.info(np.var(arr, axis=0))
    output = np.std(arr)
    logging.info(output.round(12))
    return output.round(12)