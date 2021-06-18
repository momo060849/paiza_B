# coding: utf-8
import sys

# 入力のリスト
lines = sys.stdin.readlines()
# 大文字変換の開始位置終了位置を取得
s, e = lines[0].rstrip().split(" ")
#print(lines[1][int(s)-1:int(e)])

# 小文字部分と大文字部分をそれぞれ格納
small1 = lines[1][:int(s)-1]
upper = lines[1][int(s)-1:int(e)].upper()
small2 = lines[1][int(e):]

# 結果出力
print(small1 + upper + small2)