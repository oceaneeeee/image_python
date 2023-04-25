from random import randint

def generate_random_list(n):
    arr = []
    for i in range(n):
        arr.append(randint(0, 9))
    return arr

print(__name__)
import sys
if __name__ == '__main__':
    print(generate_random_list(int(sys.argv[1])))
