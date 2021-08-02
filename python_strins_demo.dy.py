name = "neha"
print(name)
print(type(name))

#another example(concatenation)
subject1="problem"
subject2="solving"
subject3="and"
subject4="programming"
subject = subject1 + subject2 + subject3 + subject4
print(subject)



#slicing or slice operator
print(subject[0:7])
print(subject[7:14])
print(subject[14:17])
print(subject[17:28])



#in operator(gives membership)
print("solving" in subject)    
#checking whether the given string is present in subject or not
print("semester" not in subject)



#Raw string operator (print the string as it is) (r or R)
print("\n prints \n") #only print 'prints'
print(r"\n prints \n") #print whole inside inverted comas
print(R"\n prints \n")
#Because anything after '\' slash will not get printed\
#to escape sequence r is introduced



# %s string format
sub='Maths'
part=1
print("%s %d"%(sub,part))
print("We have part %d of %s in first semester"%(part,sub))



# repeat (*) operator
print(subject1*3, subject2 * 2, subject3 * 4)



#to change either upper or lower case
print(subject1.upper())
print(subject2.lower())



#split
sentence="i love my self"
print(sentence.split())



#join
words = ["i","am","the","best"]
print('\/'.join(words))

