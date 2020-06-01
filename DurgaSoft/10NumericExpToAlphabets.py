s=input("Enter the Expression : ")
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        output=output+(d*x)
print(output)
