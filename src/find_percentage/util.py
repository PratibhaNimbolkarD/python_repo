def find_percentage(n):
    sum = 0
    for i in n:
        sum = sum + i

    return "%.02f" % (sum / 3)