def Rec_Sum(n):
    if len(str(n))==1:
        return n
    else:
        return n%10+Rec_Sum(n//10)

print(Rec_Sum(4321))