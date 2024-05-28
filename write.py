#read the file and store all the lines in list
#reverse the list
#write the list back to the file

with open('test.txt','r') as reader: # as reader is a obj
    content = reader.readlines()
    reversed(content)



with open('test.txt','r') as reader:
    content = reader.readlines()
    
