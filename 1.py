def bubble_sort(A):
    for i in range(len(A)):
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
        print(A)
    return A


a = []
for k in range(0, 10):
    k = int(input())
    a.append(k)
bubble_sort(a)