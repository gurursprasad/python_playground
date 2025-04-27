s=input("Enter the String: ")
alpha=''
digits=''
for ch in s:
    if ch.isalpha():
        alpha=alpha+ch
    else:
        digits=digits+ch
output=''.join(sorted(alpha)+sorted(digits))
print(output)
