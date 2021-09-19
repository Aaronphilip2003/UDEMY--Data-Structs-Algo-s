def Rec_Sum(n):
    if n==0:
        return 0
    else:
        return n+Rec_Sum(n-1)


print(Rec_Sum(4))