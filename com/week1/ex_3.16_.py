L = [70, 100, 80, 60, 90]
nMin = nMax = L[0]
# nMin = min(L)
# nMax = max(L)
for n in L:
    if nMin > n:
        nMin = n
    if nMax < n:
        nMax = n
print("Min = %d,m nMax = %d" %(nMin, nMax))
