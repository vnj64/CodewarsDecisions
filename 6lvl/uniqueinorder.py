from dis import code_info
from enum import unique


def unique_in_order(iterable):
    array_uniq = []
    for symbol in range(len(iterable) - 1):
        if iterable[symbol] != iterable[symbol + 1]:
            array_uniq.append(iterable[symbol])
    array_uniq.append(iterable[-1])
    return array_uniq


print(unique_in_order("AAAABBBCCDAABBB"))
