import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')
def no_idea():
    n_and_m = input().split()
    array = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    happiness = 0

    for i in array:
        if i in a:
            happiness += 1
        elif i in b:
            happiness -= 1
    logging.info(happiness)

    return happiness