n = int(input('--->'))
oddSum = evenSum = 0
for i in range(1, n+1):
    if i%2:
        oddSum += i
    else:
        evenSum += i
print("n = %d: oddSum=%d, evenSum = %d" % (n, oddSum, evenSum))
