s=input("Enter the String to Internally reveerse: ")
l=s.split()
print(l)
l1=[]
for x in l:
    l1.append(x[::-1])
print(l1)
output=' '.join(l1)
print(output)
