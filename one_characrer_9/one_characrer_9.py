# coding: utf-8
import sys

# 入力のリスト
lines = sys.stdin.readlines()
# 検索条件を格納
kw = lines[0].rstrip()
# 被検索の文字列を格納
string = lines[1]
#print(lines)
#print(string.count(kw))

# ヒット回数初期化
count_n = 0

for s in string:
    # 検索
    if s == kw:
        count_n += 1
        
# 検索ヒット回数
print(count_n)