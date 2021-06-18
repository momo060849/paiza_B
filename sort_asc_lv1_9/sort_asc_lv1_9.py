# coding: utf-8
import sys

# 入力リスト
lines = sys.stdin.readlines()
#print(lines)
# ソート対象の値
data = lines[1:]

# {"半角英文字":数値}な辞書を作る
data_ext = {}
for i in data:
    #print(i)
    key, val = i.rstrip().split(" ")
    #print(key)
    #print(val)
    data_ext[key] = int(val)

# 数値を降順にソート（dictにした意味はとくにない）
sorted_data = sorted(data_ext.items(), key = lambda x:x[1])

# ソート済みリストを1要素ずつ出力
for i in sorted_data:
    print(i[0])
    
