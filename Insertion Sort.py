def insertion_sort(arr):
    for i in range(1,len(arr)):
        start=arr[i]
        j=i-1
        while j>=0 and start<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=start
arr=[6,8,3,0,6,2,5]
insertion_sort(arr)
print("Sorted array:",arr)