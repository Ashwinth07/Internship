n=int(input("Enter the Total number :"))
l=[]
for i in range(n):
    l.append(int(input()))
for i in range(n):
    for j in range(n-1-i):
        if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

print(f"After Sorting in ascending Order {l}")

for i in range(n):
    for j in range(n-1-i):
        if l[j] < l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

print(f"After Sorting in descending Order {l}")
