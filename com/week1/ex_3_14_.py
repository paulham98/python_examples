year = int(input('년도--->'))
nDays = 0
for y in range(1, year):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        bLeapYear = True
    else:
        bLeapYear = False
        if bLeapYear:
            nDays += 366
        else:
            nDays += 365
print("year = %d : nDays=%d" % (year, nDays))