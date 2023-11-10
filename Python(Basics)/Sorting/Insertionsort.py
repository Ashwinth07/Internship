n=int(input("Enter the Total number :"))
l=[]
for i in range(n):
    l.append(int(input()))
for i in range(1, len(l)):
    key = l[i]
    j = i - 1
    while j >= 0 and key < l[j]:
        l[j + 1] = l[j]
        j -= 1
    l[j + 1] = key
print(f"Ascending Order {l}")
for i in range(1, len(l)):
    key = l[i]
    j = i - 1
    while j >= 0 and key > l[j]:
        l[j + 1] = l[j]
        j -= 1
    l[j + 1] = key
print(f"descending Order {l}")