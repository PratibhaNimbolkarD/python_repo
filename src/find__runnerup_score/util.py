import logging

logging.basicConfig(level=logging.INFO , format='%(message)s')
def runner_up():
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    arr.remove(max(arr))
    logging.info(max(arr))
    return max(arr)