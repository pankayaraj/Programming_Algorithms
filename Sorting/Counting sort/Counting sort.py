def counting_sort(list,k):
    counter = []
    for _ in xrange(k):
        counter.append(0)
    for i in list:
        counter[i] += 1
    A = []
    for j in xrange(len(counter)):
        while counter[j] != 0:
            A.append(j)
            counter[j] -= 1
    return (A)


