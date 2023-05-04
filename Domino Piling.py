m,n = input().split()
m = int(m)
n = int(n)

if 1<=m and m<=16 and 1<=n and n<=16 and m<=n:
    if (m*n)%2 == 1:
        maxAmount = ((m*n)-1)/2
    else:
        maxAmount = (m*n)/2
    print(int(maxAmount))
