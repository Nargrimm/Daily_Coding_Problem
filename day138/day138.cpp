#include <iostream>
#include <vector>

/*
 * Find the minimum number of coins required to make n cents.
 *
 * You can use standard American denominations, that is, 1c, 5c, 10c, and 25c.
 *
 * For example, given n = 16, return 3 since we can make it with a 10c, a 5c, and a 1c.
 */

std::vector<int> get_min_coins(int value)
{
    std::vector<int> res = {};
    std::vector<int> coins = {25, 10, 5, 1};
    while (value > 0)
    {
        for (auto const coin : coins)
        {
            if (value >= coin)
            {
                value -= coin;
                res.push_back(coin);
                break;
            }
        }
    }
    return res;
}

void print_results(std::vector<int> res)
{
    if (!res.size() > 0)
        return;
    std::cout << "[" << *(res.begin());
    for (auto it = res.begin() + 1; it != res.end(); it++)
    {
        std::cout << ", " << *it;
    }
    std::cout << "]" << std::endl;
    return;
}

int main(void)
{
    print_results(get_min_coins(16));
    print_results(get_min_coins(37));
    print_results(get_min_coins(0));
    print_results(get_min_coins(-1));
    print_results(get_min_coins(128));
    return 0;
}