# Create a text file and by using python handling:
# (1)count the number of characters
# (2)find the repeated word
# (3)count number of repeated words
# (4)count number of lines and words

'''#(1) counting the number of characters
f=open("text.txt","r")
data = f.read()
total_charac = len(data)
print(total_charac)'''

'''#(2)finding the repeated words
f=open("text.txt","r")
data = f.read()
d = dict() #creating an empty dictionary
data = data.lower()
for line in data:
    line = line.strip() #seperating lines
    #words = line.split(" ") #spliting words
    print(line)
    #print(words)
    for word in line:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
print(d)
for key in list(d.keys()):
    print(key, ":", d[key])'''
    
#(4)counting number of lines and words
f=open("text.txt","r")
data = f.read()
data_split = data.split()
print(data_split)
number_of_words = len(data_split)
print(number_of_words)
number_of_lines = data.split("\n")
print(len(number_of_lines))

