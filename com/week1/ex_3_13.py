n = int(input('--->'))
nFact =1
for i in range(n, 0, -1):
    nFact *= i
    print("n= %d : nFact=%d" % (n,nFact))
