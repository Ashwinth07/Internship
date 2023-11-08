n=int(input("Enter the Total number :"))
l=[]
for i in range(n):
    l.append(int(input()))
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if l[j] < l[min_idx]:
            min_idx = j
    l[i], l[min_idx] = l[min_idx], l[i]
print(f"After Sorting in ascending Order {l}")
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if l[j] > l[min_idx]:
            min_idx = j
    l[i], l[min_idx] = l[min_idx], l[i]
print(f"After Sorting in descending Order {l}")