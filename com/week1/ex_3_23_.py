n = int(input('양의 정수--->'))

bPrime = True
for i in range(2, n):
    if not n % i:
        bPrime = False
if bPrime:
    print("{0}은 소수이다.".format(n))
else:
    print("{0}은 소수가 아니다.".format(n))
    