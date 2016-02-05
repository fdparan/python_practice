import random

lst = list(range(1,600))


def binary_search(array, target):
    print array
    l = 0
    u = len(array) - 1

    while u >= l:
        guess = (l + u) // 2
        if array[guess] == target:
            print 'found target {} at index {}'.format(array[guess], guess)
            return guess

        if array[guess] < target:
            l = guess + 1
        else:
            u = guess - 1

    return -1


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print len(primes)

assert binary_search(primes, 73) == 20

print lst
print binary_search(lst, 53)