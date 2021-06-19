# coding: utf-8
import sys

# 入力
lines = sys.stdin.readlines()
#print(lines)
# 前処理
lottery_n = int(lines[0].rstrip())
#print(lottery_n)
my_lottery = lines[2:]
#print(my_lottery)


# 当選確認
for i in my_lottery:
    m_l = int(i.rstrip())
    #print("比較: " + str(m_l) + " " + str(lottery_n))
    if m_l == lottery_n:
        #print(str(m_l) + "first")
        print("first")
    elif (m_l-1 == lottery_n) or (m_l+1 == lottery_n):
        # 前後賞の結果が[条件]の範囲内に収まっているか確認する
        if (m_l-1 >= 100000) and (m_l+1 <= 199999):
            #print(str(m_l) + "adjacent")
            print("adjacent")
        else:
            print("blank")
    # 下4桁が一致すれば2等
    elif str(m_l)[-4:] == str(lottery_n)[-4:]:
        #print(str(m_l)[-4:])
        #print(str(m_l) + "second")
        print("second")
    # 下3桁が一致すれば3等
    elif str(m_l)[-3:] == str(lottery_n)[-3:]:
        #print(str(m_l) + "third")
        print("third")
    else:
        #print(str(m_l) + "blank")
        print("blank")