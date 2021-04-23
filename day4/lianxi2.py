a = [1,5,21,30,15,9,30,24]
c=0
d=0
while True:

    if a[c]%5 == 0:
        d=d+a[c]
    c=c+1
    if c==7:
       print("5的倍数的和:",d)
       break

