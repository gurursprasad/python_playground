s=input("Enter the Expression : ")
c=0
prev=s[0]
output=''
for ch in s:
    if ch==prev:
        c=c+1
    else:
        output=output+str(c)+prev
        c=1
        prev=ch
        output=output+str(c)+prev
print(output)

