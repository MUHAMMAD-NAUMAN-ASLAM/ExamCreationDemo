#classes in Python

class calculator:
    num=100 # class variable

    def getData(self):
        print("i am now executing as a method in class")

    def __init__(self):
        print("I am calling a constructor")

obj = calculator()
obj.getData()
print(obj.num)