# coding: utf-8
import sys
import pprint

# 入力リスト
lines = sys.stdin.readlines()
# ソート対象
data_row = lines[1:]
#print(data_row)

# {"半角英文字":数値}な辞書を作る
data_dic = {}
for i, d in enumerate(data_row):
    key, val = d.rstrip().split(" ")
    # 同じ "半角英文字" を判定
    if key in data_dic:
        data_dic[key] += int(val)
    else:
        data_dic[key] = int(val)
    
#pprint.pprint(data_dic)
#print(sorted(data_dic.items(), key=lambda x:[]))
#print(sorted(data_dic.items(), key=lambda x:x[1], reverse=True))
# 数値を降順にソート（dictにした意味はとくにない）
sorted_data = sorted(data_dic.items(), key=lambda x:x[1], reverse=True)

# ソート済みリストを1要素ずつ出力
for d in sorted_data:
    print(d[0] + " " + str(d[1]))

#print(sorted(data_dic.items(), key=lambda x:x[0]))
#print(sorted(data_dic.items(), key=lambda x:x[1], reverse=True))
#print(sorted(data_dic.items(), key=lambda x:x[1]))