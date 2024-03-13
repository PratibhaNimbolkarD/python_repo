import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')

def find_percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = 0
    for key , value in student_marks.items():
        if key == query_name:
            avg = sum(value) / 3
            break
    logging.info("{:.02f}".format(avg))
    return avg






