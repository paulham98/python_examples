nTH = int(input('--->'))

i = 1
nSum = 0
while True:
    nSum += i
    if nSum >= nTH:
        break
    i += 1
    print("i = %d: nSum = %d" % (i, nSum))
    