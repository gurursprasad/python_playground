file_obj = open('testleaf.txt', mode='w')
# file_obj.write('Leaf_test')
# file_obj.close()
for i in range(10):
    file_obj.write(f'index number is {i} \n')
file_obj.close()