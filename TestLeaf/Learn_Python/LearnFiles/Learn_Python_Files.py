# with open('test01.txt', 'w') as file_obj:
#     for i in range(11):
#         file_obj.write(f'5 * {i} = {5*i} \n')

def split(word):
    return [char for char in word]

with open('test01.txt' , 'r') as r:
    data = r.read()
    l=data.split()
    l1=[]
    l2=[]
    s=''
    for word in l:
        # print(f'word = {word}')
        # l1 = split(word)
        # print(f'l1 = {l1}')
        for ch in word:
            if ch.isnumeric():
                l2.append(ch)
    print(l2)
    # print(l1)