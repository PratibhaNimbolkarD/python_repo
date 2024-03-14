import logging
logging.basicConfig(level=logging.INFO , format='%(message)s')

def string_formatting():
    number = int(input("Enter the number : "))
    length = len("{0:b}".format(number))
    result=""
    for i in range(1, number + 1):
         logging.info("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=length))
         a = "{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=length)
         result += a+'\n'
    return (result)