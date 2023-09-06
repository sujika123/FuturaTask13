# Print prime numbers in an array

a = [10,53,11,5,22,55,89,1,15,2,43,13]
print('\nPrime Numbers')
for i in range(len(a)):
    c=0
    for j in range(1,a[i]+1):
        if a[i]%j==0:
            c=c+1

    if c==2:
        print(a[i],end=' ')