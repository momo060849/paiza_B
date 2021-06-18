import sys

# 入力をリストで取得
input_l = sys.stdin.readlines()
#print(input_l)
# 計算対象を取得
obj_calc = input_l[1:]
#print(obj_calc)

s1 = []
for i in obj_calc:
    row = i.rstrip().split(" ")
    #print(row)
    r1, r2 = row[0], row[1]
    # 足し算と掛け算の判定
    if r1 == r2:
        s1.append(int(r1) * int(r2))
    else:
        s1.append(int(r1) + int(r2))
        
# 計算結果を出力
print(sum(s1))
        
        
        