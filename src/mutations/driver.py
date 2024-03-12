from util import mutate_string
if __name__ == '__main__':
    s = input("Enter the string : ")
    i, c = input("Enter the index and the letter : ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)