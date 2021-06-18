# coding: utf-8
import sys

# 入力のリスト
inp_l = sys.stdin.readlines()
#print(inp_l)

# 文字抽出の開始位置を取得
extract_num = int(inp_l[0])
# 抽出対象の文字列を取得
string = inp_l[1]
#print(extract_num, string)

# 文字抽出の開始位置が文字列の長さを超えないか判定する
if len(string) > extract_num:
    print(string[extract_num-1] + " " + string[extract_num])