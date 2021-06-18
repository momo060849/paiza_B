import sys

line = sys.stdin.readlines()
# 計算対象は1行目以降
input_l = line[1:]
#print(input_l)

target = []
for i in input_l:
    #print(i)
    # 計算対象の数値を判定
    if int(i) >= 5:
        target.append(int(i))
    else:
        target.append(0)
        
# 計算
s = sum(target)
print(s)