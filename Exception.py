ItemsInCart =1

#if ItemsInCart != 0:
 #   raise("Items should be greater then 1")

#assert(ItemsInCart == 0)

try:
    with open('test.txt','r') as reader:
        reader.read()
except:
    print("Some error in the previous file")

try:
    with open('test1.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e)

