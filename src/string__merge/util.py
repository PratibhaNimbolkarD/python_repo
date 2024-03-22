import logging
logging.basicConfig(level= logging.INFO, format= '%(message)s')
def merge_the_tools():
    string = input("Enter the string: ").strip()
    k = int(input("Enter the length of each substring: "))
    c = 0
    s = ''
    str = ""

    for i in string:
        if i not in s:
            s = s + i
        c += 1
        if (c == k):
            # logging.info(s)
            str += s + "\n"
            s = ''
            c = 0

    logging.info(str)
    return str
