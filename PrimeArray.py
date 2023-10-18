
a = [10,7,34,12,21,2,11,54,41]
# a = [10,53,11,5,22,55,89,1,15,2,43,13]

for i in range(len(a)):
    if(a[i] > 1):
        for j in range(2,a[i]):
            if(a[i] % j ) == 0 :
                break
        else:
            print(a[i],end=' ')

