# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import sys
import pandas as pd
from collections import defaultdict

lines = sys.stdin.readlines()

#print(lines)

# 占い結果を一時保存するリスト
f1_u_n = []
f1_u_r = []
# 占い解釈を一時保存するリスト
f2_u_r = []
f2_u_ex = []
# 占い結果を紐付けるdict
uranai_user = defaultdict(str)
# 占い解釈を紐付けるdict
uranai_back_data = defaultdict(str)
# 占い結果と占い解釈を区別するフラグ
f = 0


# {id_number:(ユーザー名, 占い結果)},
# {"占い結果":占い結果一覧データ}
# な辞書を作る
for id_n, i in enumerate(lines):
    ele = i.rstrip()
    #print("len: ", len(ele))
    # ユーザーデータとバックデータを識別
    if " " not in ele:
        f += 1
        #print("f: ", f)
        continue
    # ユーザーの占い結果を dict に格納
    if f == 1:
        f_ele, s_ele = ele.split(" ")
        #print("f_ele: ", f_ele)
        #print("s_ele: ", s_ele)
        uranai_user[id_n] = (f_ele, s_ele)
    # 占いバックデータを dict に格納
    elif f == 2:
        f_ele, s_ele = ele.split(" ")
        #print("f_ele: ", f_ele)
        #print("s_ele: ", s_ele)
        uranai_back_data[f_ele] = s_ele

# 入力された順番を崩さないように dataframe に格納
uranai_user_df = pd.DataFrame(uranai_user.values(), index = uranai_user.keys(),
                              columns=["user_name","uranai_result"])
#print(uranai_user_df)

uranai_back_data_df = pd.DataFrame(uranai_back_data.items(),
                                   columns=["uranai_result","uranai_explanation"])
#print(uranai_back_data_df)

uranai_db = pd.merge(uranai_user_df, uranai_back_data_df, on='uranai_result', how='left')
#print(uranai_db)


# 結果出力
for i in uranai_db.itertuples():
    print(i.user_name + " " + i.uranai_explanation)
