sentence=input()
length=len(sentence)

if length==0:
    print("no string")
elif length==1:
    print(sentence+str(length))

last=sentence[0]
count=1
i=1
r=""

while i<length:
    if sentence[i]==sentence[i-1]:
        count+=1
    else:
        r=r+sentence[i-1]+str(count)
        count=1
    i+=1

r=r+sentence[i-1]+str(count)

print(r)