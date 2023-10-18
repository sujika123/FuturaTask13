# Print prime numbers in an array

a = [10,53,11,5,22,55,89,1,15,2,43,13]
# a = [10,7,34,12,21,2,11,54,41]
print('\nPrime Numbers')
for i in range(len(a)):
    c=0
    for j in range(1,a[i]+1):
        if a[i]%j == 0:
            c = c+1

    if c == 2:
        print(a[i],end=' ')

print()
print("__________________________________")

a=[]
n=int(input("Number of elements in array:"))
print("Elements of array")
for i in range(0,n):
   l=int(input())
   a.append(l)
print("Array is ",a)

# a = [10,53,11,5,22,55,89,1,15,2,43,13]
print('\nPrime Numbers')
for i in range(len(a)):
    c=0
    for j in range(1,a[i]+1):
        if a[i]%j==0:
            c=c+1

    if c==2:
        print(a[i],end=' ')


print("\n_____________________________")

num=[10,53,11,5,22,55,89,1,15,2,43,13]
prime_numbers=[]
for i in num:
    k=0
    for j in range(1,i):
        if i%j==0:
            k+=1
    if k==1:
        prime_numbers.append(i)
print(prime_numbers)