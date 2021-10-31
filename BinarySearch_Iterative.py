def binary_Search_Iterative(arr,ele):
    first=0
    mid=0
    last=len(arr)-1
    found=False

    while first<=last and not found:
        mid=(first+last)//2

        if arr[mid]==ele:
            found=True
        else:
            if ele<arr[mid]:
                last=mid-1
            else:
                first=mid+1   
    return found

print(binary_Search_Iterative([1,2,3,4,5,6,7,8,9,10],5))