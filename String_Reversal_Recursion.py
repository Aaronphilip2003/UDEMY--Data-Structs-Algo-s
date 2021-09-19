def Rev(s):
    # Base Case
    if len(s) <=1:
        return s
    else:
        return Rev(s[1:])+s[0]

print(Rev("abc"))

# abc
# pass 1: bc + a
# pass 2: c + ba
# pass 3: cba
