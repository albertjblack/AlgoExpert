def nonConstructbleChange(coins):
    upperChange = 0
    coins.sort()

    for coin in coins:
        if coin > upperChange + 1:
            return upperChange + 1
        else:
            upperChange += coin
    return upperChange + 1


if __name__ == "__main__":
    coins1 = [5, 1, 2, 1]
    coins2 = [1, 9, 1, 4, 2]

    print(nonConstructbleChange(coins1))
    print(nonConstructbleChange(coins2))
