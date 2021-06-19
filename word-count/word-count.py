# coding: utf-8

# 入力受け取りと前処理
lines = input()
s_lines = lines.split(" ")


# 重複なしの順序を保持したリストを作成
element = []
for s in s_lines:
    if s not in element:
        element.append(s)


# 結果出力
for e in element:
    print(e + " " + str(s_lines.count(e)))