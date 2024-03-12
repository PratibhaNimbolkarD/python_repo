import logging

logging.basicConfig(level=logging.INFO , format='%(message)s')
def runner_up(arr):
    arr = set(arr)
    arr.remove(max(arr))
    logging.info(max(arr))