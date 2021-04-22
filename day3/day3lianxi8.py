jin = 20
day = 0

while True:
    jin = jin - 3
    if jin >= 0:
        jin = jin + 2
        day = day + 1
    else:
        break
print(day)