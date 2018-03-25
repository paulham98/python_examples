sID = input("주민번호 입력 :")
W = (2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5)
nSum = 0
for i in range(len(sID)-1):
    nSum += W[i]* int(sID[i])
    nCheckDigit = (11 - nSum % 11) % 10

    if int(sID[-1]) == nCheckDigit:
        print("{0}은 올바른 주민번호".format(sID))
    else:
        print("{0}은 잘못된 주민번호".format(sID))
