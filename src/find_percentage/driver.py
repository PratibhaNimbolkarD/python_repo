import logging
from util import find_percentage
logging.basicConfig(level=logging.INFO , format='%(message)s')

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    logging.info(find_percentage(student_marks[query_name]))