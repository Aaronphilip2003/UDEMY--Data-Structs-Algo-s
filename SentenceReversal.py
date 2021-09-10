def rev(s):
    words=[]
    length=len(sentence)
    spaces=[' ']
    i=0
    while i<length:
        if sentence[i] not in spaces:
            word_start=i

            while i<length and sentence[i] not in spaces:
                i+=1
            
            words.append(sentence[word_start:i])
        i+=1
    return " ".join(reversed(words))

sentence=input()
print(rev(sentence))

