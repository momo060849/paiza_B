# coding: utf-8
import sys
import pandas as pd
import numpy as np

# 入力リスト
lines = sys.stdin.readlines()
#print(lines)

# 何目並べか
grid_n = len(lines)
#print("grid_n: ", grid_n)

# マス目の情報をマスごとに分割
two_d_array = []
for i in lines:
    ele = []
    for j in i.rstrip():
        ele.append(j)
    two_d_array.append(ele)
gomoku = pd.DataFrame(two_d_array)
#print(type(gomoku))
#print(gomoku)
#diag = np.diag(gomoku)
#print(diag)
#print(sum(diag == "X"))
#print(type(np.diag(gomoku)))
# 行
#print(gomoku.iloc[0])
# 列
#print(gomoku[0])

def height():
    """
    縦のビンゴを判定
    勝った方のマークを返す
    """
    r_h = ""
    for i in range(0, grid_n):
        #print("count: ", i)
        #print("gomoku: ", gomoku.iloc[i])
        #print("bool: ", gomoku.iloc[i] == "O")
        #print("列番号: ", i)
        #print("列: ", gomoku.iloc[i])
        #print("sum: ", sum(gomoku.iloc[i] == "O"))
        if sum(gomoku.iloc[i] == "X") == grid_n:
            r_h = "X"
            #print("height: ", r_h)
            break
        elif sum(gomoku.iloc[i] == "O") == grid_n:
            r_h = "O"
            #print("height: ",r_h)
            break
    
    #print("return: ", r_h)
    return r_h
        
def width():
    """
    横のビンゴを判定
    勝った方のマークを返す
    """
    r_w = ""
    for i in range(0, grid_n):
        if sum(gomoku[i] == "X") == grid_n:
            r_w = "X"
            #print("width: ", r_w)
            break
        elif sum(gomoku[i] == "O") == grid_n:
            r_w = "O"
            #print("width: ", r_w)
            break
    
    return r_w
        
def diagonal():
    """
    斜めのビンゴを判定
    勝った方のマークを返す
    """
    r_d = ""
    diag = np.diag(gomoku)
    #print(diag == "X")
    diag_fli = np.diag(np.fliplr(gomoku))
    #print(diag_fli == "X")
    if sum(diag == "X") == grid_n or sum(diag_fli == "X") == grid_n:
        r_d = "X"
        #print("diagonal: ", r_d)
    elif sum(diag == "O") == grid_n or sum(diag_fli == "O") == grid_n:
        r_d = "O"
        #print("diagonal: ", r_d)
        
    return r_d

# 縦の判定
r_h = height()
#print("r_h: ", r_h)
# 横の判定
r_w = width()
#print("r_w: ", r_w)
# 斜めの判定
r_d = diagonal()
#print("r_d: ", r_d)

# 勝者のマークを辞書に格納
# NOTE: nビンゴに増やすみたいな仕様に変更するなら、辞書の構造を変えれば良さそう
result = {"height":r_h,"width":r_w,"diagonal":r_d}
#print(result)

# 勝利判定
draw_f = 0 # 引き分け判定用フラグ
for ln, l in result.items():
    #print(ln, l)
    # 勝者を出力
    if l:
        print(l)
        break
    # 引き分け判定
    else:
        draw_f += 1
# 引き分け判定
if draw_f == 3:
    print("D")
