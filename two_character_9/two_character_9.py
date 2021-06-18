# coding: utf-8
import sys
import re

# 入力リスト
lines = sys.stdin.readlines()
#print(lines)

# 検索条件
kw = lines[0].rstrip()
# 検索範囲の設定
kw_len = len(kw)
# 被検索文字列
string = lines[1].rstrip()
#print(string)

#print(len([m.span() for m in re.finditer(kw, string)]))

# ヒット回数初期化
match_c = 0

for i in range(0,len(string)):
    # 検索範囲内の文字列を格納
    w_size = string[i:i+kw_len]
    #print(w_size)
    # 検索範囲内の文字列と検索条件を比較
    if w_size == kw:
        #print(w_size)
        # ヒット回数をカウント
        match_c += 1

# ヒット回数の合計を出力
print(match_c)