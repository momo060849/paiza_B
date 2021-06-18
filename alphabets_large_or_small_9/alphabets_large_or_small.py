# coding: utf-8
import string
import sys

# 大文字アルファベット26文字のリスト
upp_alp_list = string.ascii_uppercase

# 入力リスト
lines = sys.stdin.readlines()
# 検索範囲の開始位置
h_n = upp_alp_list.find(lines[0].rstrip())
# 検索範囲の終了位置
e_n = upp_alp_list.find(lines[1].rstrip())

# 検索対象の文字列を作成
st = []
for s in range(h_n,e_n+1):
    st.append(upp_alp_list[s])
search_t = "".join(st)

# 検索、結果出力
if lines[2].rstrip() in search_t:
    print("true")
else:
    print("false")