#for loops
#use of break and continue
even = [2,4,6,8,10]
print(type(even))
for i in even:
    if i>6:
        break
    print(i)

#except 10 to print all the numbers
for j in even:    
    if j == 6:
        continue
    print(j)

#for only printing one number
    for i in even:
        if i!=10:
            continue
        print(i)
    
    

