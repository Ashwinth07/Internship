word=""
n=int(input())
#adding
for i in range(n):
    q=input()
    word=word+q
    word=word+" "
print(word)
#removing from string
n1=int(input("Enter the starting index"))
n2=int(input("Enter the ending index"))
print(word[:n1]+word[n2:])
#update
word=word.upper()
print(word)
#repetation
result = word * 3
print(result)
#replace
old=input("Enter the word want to replace")
new=input("Enter new word")
newsen= word.replace(old,new)
print(newsen)