def bubble_sort(arr):
    for i in range(0,len(arr)):
        print(arr[i] ,end=" ")
    print("\n")
    for n in range(len(arr)-1,0,-1):
        for k in range (0,n):
            if arr[k]>arr[k+1]:
                temp=arr[k]
                arr[k]=arr[k+1]
                arr[k+1]=temp
    
    for i in range (0,len(arr)):
        print(arr[i],end=" ")


bubble_sort([10,9,8,7,6,5,4,3,2,1])
