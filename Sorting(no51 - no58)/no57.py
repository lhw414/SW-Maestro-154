# BJ 11652

import sys

n = int(sys.stdin.readline())
card_dic = {}

for i in range(n):
    card = int(input())
    if card in card_dic:
        card_dic[card] += 1
    else:
        card_dic[card] = 1

result = sorted(card_dic.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])
