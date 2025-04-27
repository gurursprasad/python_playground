# print("This is module1")
# print("This is module1 added a new line")

# x = 10
# y = 20

# def fi():
# 	pass

# def f2():
# 	pass

def f1():
    if __name__ == '__main__':
        print("The module is executed directly")
        print("The value of __name__:", __name__)
    else:
        print("The module is executed indirectly from another method/program")
        print("The value of __name__:", __name__)