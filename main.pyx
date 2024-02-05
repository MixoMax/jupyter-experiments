#Cython test
#path: main.pyx


def LevensteinDistance(str1, str2):
    cdef int m = len(str1)
    cdef int n = len(str2)
    cdef int i, j
    cdef int cost
    cdef int D[m+1, n+1]

    for i in range(m+1):
        D[i, 0] = i
    for j in range(n+1):
        D[0, j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1
            D[i, j] = min(D[i-1, j]+1, D[i, j-1]+1, D[i-1, j-1]+cost)

    return D[m, n]