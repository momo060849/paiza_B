# coding: utf-8
import sys

# 入力リスト
lines = sys.stdin.readlines()
#print(lines)

# 抽出開始位置と終了位置を取得
s, e = lines[0].rstrip().split(" ")
#print(s)
#print(e)

# 抽出対象の文字列を取得
string = lines[1]
#print(string)

# 文字列の抽出
print(string[int(s)-1:int(e)])