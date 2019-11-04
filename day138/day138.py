#!/usr/bin/env python3


'''
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1c, 5c, 10c, and 25c.

For example, given n = 16, return 3 since we can make it with a 10c, a 5c, and a 1c.
'''

def get_min_coins(value):
    coins = [25, 10, 5, 1]
    res = []
    while value > 0:
        for coin in coins:
            if value >= coin:
                res.append(coin)
                value -= coin
                break
    return res

print(get_min_coins(16))
print(get_min_coins(37))
print(get_min_coins(0))
print(get_min_coins(-1))
print(get_min_coins(128))