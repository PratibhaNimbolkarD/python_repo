import itertools
import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')
def iterable_iterators():
    lenght = int(input())
    list_of_letters = input().split()
    num_of_selections = int(input())

    posible_combinations = list(itertools.combinations(list_of_letters, num_of_selections))
    posible_combinations_lenght = len(posible_combinations)
    matches_lenght = len(['k' for i in posible_combinations if 'a' in i])

    logging.info(matches_lenght / posible_combinations_lenght)
    return matches_lenght / posible_combinations_lenght