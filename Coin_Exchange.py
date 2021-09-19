def Rec_Coin(target,coins):
    min_coins=target

    if target in coins:
        return 1
    
    else:
        for i in [c for c in coins if c<=target]:
            num_coins=1+Rec_Coin(target-i,coins)
            if num_coins < min_coins:
                min_coins=num_coins
    return min_coins

print(Rec_Coin(23,[1,5,10]))