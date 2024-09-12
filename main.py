prices = [7, 4, 1]

curr = 0
for i in range(len(prices)):
    for j in range(i+1, len(prices)):

        sub = prices[j] - prices[i]
        # print(prices[i], prices[j], " = ", sub)
        if sub > curr:
            curr = sub
            buy = i
            sell = j

    print(curr, buy, sell)






