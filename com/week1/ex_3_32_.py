nPrime = int(input('소수의 개수--->'))

k = 0
n = 2
L = []
while k != nPrime:
    for i in range(2, n):
        if not n % i: break
        else:
            L.append(n)
            k += 1
        n += 1

print("{0}개의 소수, L = {1}".format(k, L))
