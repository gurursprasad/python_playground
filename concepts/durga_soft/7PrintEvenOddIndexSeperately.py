s=input("Enter the string: ")
i=0
Even=''
Odd=''
while i<len(s):
    if i%2==0:
        Odd = Odd+s[i]
    else:
        Even = Even+s[i]
    i=i+1
OddOutput=''.join(Odd)
EvenOutput=''.join(Even)
print(OddOutput)
print(EvenOutput)
