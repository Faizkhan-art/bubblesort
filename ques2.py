arr = [10, 4, 7, 2, 15, 6]
n=len(arr)
swaps=0

for i in range(n):
    for j in range(0, n-i -1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swaps+=swaps+1
print(arr)   
print("largest element",arr[-1]) 
print("smallest element",arr[0])    
print(swaps)    