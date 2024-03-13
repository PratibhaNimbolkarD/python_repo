import logging

def string_formatting():
    number = int(input("Enter the number : "))
    length = len("{0:b}".format(number))
    for i in range(1, number + 1):
         print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=length))