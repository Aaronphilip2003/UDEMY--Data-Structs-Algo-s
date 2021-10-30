def seq_Search_Sorted(arr,ele):
    pos=0
    found=False
    stopped=False
    while arr[pos]<len(arr) and not found and not stopped:
        if arr[pos]==ele:
            found=True
        else:
            if arr[pos]>ele:
                stopped=True
            else:
                pos=pos+1
    return found

print(seq_Search_Sorted([1,2,3,4,5],7))