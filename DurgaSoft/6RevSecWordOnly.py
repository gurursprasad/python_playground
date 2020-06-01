s=input("Enter the String to reverse every seconf word: ")
l=s.split()
l1=[]
i=0
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
output=' '.join(l1)
print(output)
