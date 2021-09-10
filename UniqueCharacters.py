def split(a):
    return [char for char in a]

word=input()
flag=0
word_list=split(word)
word_list.sort()

for i in range(1,len(word)):
    if word_list[i]==word_list[i-1]:
        flag=1
        break
    else:
        flag=0

if flag==1:
    print("False")
else:
    print("True")