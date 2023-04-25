from random import randint
import sys
def generait_random_list(n):
    arr = []
    for i in range(n):
        arr.append(randint(-9, 9))
    return arr
def get_max(arr):
    max = arr[0]
    for i in arr:
        if max < i:
            max = i
    return max
def abs_arr(arr):
    x = []
    for i in arr:
        x.append(abs(i))
    return x
def shift_arr(arr, s):
    l = []
    for i in range(s):
        l.append(arr[i])
    for i in range(len(arr)-s):
        arr[i] = arr[i+s]
    for i in range(s):
        arr[len(arr)-s+i] = l[i]
    return arr
if __name__ == '__main__':
    arr = generait_random_list(int(sys.argv[1]))
    print(arr)
    print(get_max(arr))
    print(abs_arr(arr))
    print(shift_arr(arr, 2))
