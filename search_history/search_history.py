# coding: utf-8

import sys

# 入力と前処理
lines = sys.stdin.readlines()
re_lines = lines[::-1]
#print(re_lines)


# 検索ワードリストの重複を削除して出力
search_list = []
for i in re_lines[:-1]:
    s_w = i.rstrip()
    if s_w not in search_list:
        # HACK: 重複を削除するためにもっと良い書き方があるかもしれない
        search_list.append(s_w)
        print(s_w)