n=input()
arr=input()
l=arr.split()
print(l)
i=0
pospro=0
negpro=0
zeropro=0
a=0
b=0
c=0
while i>=len(l):
    if i<0:
        b+=1
    if i>0:
        a+=1
    if i==0:
        c+=1
pospro=a/n
negpro=b/n
zeropro=c/n
print(pospro)
print(negpro)
print(zeropro)
