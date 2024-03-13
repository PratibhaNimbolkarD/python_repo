import logging
logging.basicConfig(level= logging.INFO, format= '%(message)s')

def mutate_string():
    string = input("Enter the string : ")
    position, character = input("Enter the index and the letter : ").split()
    position = int(position)
    newString = string[:position]+character+string[position+1:]
    logging.info(newString)
    return newString