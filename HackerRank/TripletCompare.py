import sys
a0,a1,a2=input().strip().split(' ')
A=[int(a0),int(a1),int(a2)]
b0,b1,b2=input().strip().split(' ')
B=[int(b0),int(b1),int(b2)]
alice=0
bob=0
for i in range(3):
    if A[i]>B[i]:
        alice+=1
    if A[i]<B[i]:
        bob+=1
    if A[i]==B[i]:
        pass
print(alice,bob)
