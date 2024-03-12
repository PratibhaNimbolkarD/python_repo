import  logging
from util import mutate_string
logging.basicConfig(level=logging.INFO , format= '%(message)s')
if __name__ == '__main__':
    s = input("Enter the string : ")
    i, c = input("Enter the index and the letter : ").split()
    s_new = mutate_string(s, int(i), c)
    logging.info(s_new)