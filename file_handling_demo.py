#to open existing file from python
#"r" is to read
#"a" is to append

f = open("text_file.txt","r")

if f.mode=="r":
    contents=f.read()
    print(contents)

#to append the file(adding)
f = open("text_file.txt","a+")
f.write("I love myself")
f=open("C:/Users/neha/Desktop/Python files/text_file.txt","r")
add=f.read()       
print(add)
f.close()

#to make a correction in the file
f=open("text_file.txt","w")
if f.mode=="w":
    f.write("Hello world!")
f.close()

