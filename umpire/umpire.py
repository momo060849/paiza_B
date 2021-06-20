# coding: utf-8
import sys

# 入力
lines = sys.stdin.readlines()
#print(lines)
# 前処理
p = lines[1:]


# 投球結果をリストに格納
b_f = 0
s_f = 0
for i in p:
    pitc = i.rstrip()

    if pitc == "ball":
        # fourballの判定
        if b_f == 3:
            print("fourball!")
        elif b_f < 3:
            print("ball!")
            b_f += 1

    elif pitc == "strike":
        # outの判定
        if s_f == 2:
            print("out!")
        elif s_f < 2:
            print("strike!")
            s_f += 1