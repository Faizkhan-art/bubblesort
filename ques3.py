arr=[25,78,1,2,3,4,56,96]
n=len(arr)
swap=0

for i in range(n):
    for j in range(0, n- i -1):
        if arr[j] >arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swap += 1
print(arr)
print("largest element",arr[-1])
print("smallest",arr[0])  
print(swap)      