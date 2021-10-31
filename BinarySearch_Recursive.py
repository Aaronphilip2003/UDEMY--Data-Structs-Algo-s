def rec_Binary_Search(arr,ele):
    if len(arr)==0:
        return False
    
    else:
        mid=len(arr)//2
        if arr[mid]==ele:
            return True
        else:
            if ele<arr[mid]:
                return rec_Binary_Search(arr[:mid],ele)
            else:
                return rec_Binary_Search(arr[mid+1:],ele)

print(rec_Binary_Search([1,2,3,4,5,6,7,8,9,10],100))