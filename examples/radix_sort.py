import random


def radixsort(aList):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in xrange(RADIX)]

        # split aList between lists
        for i in aList:
            tmp = i//placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 1:
                maxLength = False

        a = 0

        # empty lists into aList array
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1

        # move to next digit
        placement *= 10

# samp = [33, 25, 8]

samp = [random.randint(1, 1000) for x in range(100)]

print 'Before:'
print samp

radixsort(samp)

print 'After:'
print samp

