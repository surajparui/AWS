arr=[2,7,11,15]
arr.sort()
target=9
i=0
j=len(arr)
while i>j:
    if arr[i]+arr[j]<target:
        i=i+1
    elif arr[i]+arr[j]>target:
        j=j-1
    else:
        print(i,j)
        break