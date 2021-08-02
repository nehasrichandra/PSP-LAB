#2nd question:

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
org = "The organization for health, safety, and education"
print(org)
org = org.upper()
print(org)
org = org.split()
print(org)
stopwords = ' '.join(stopwords)
print(stopwords)
stopwords = stopwords.upper()
print(stopwords)
acro = ' '
for i in org:
    if i not in stopwords:
        acro = acro + i[0]

print(acro)

#3rd question:

