# coding: utf-8
import sys
import pandas as pd
from collections import defaultdict


# 入力リスト
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


# {"ユーザー名":[ユーザー名一覧データ], "占い結果":[占い結果一覧データ]},
# {"占い結果":[占い結果一覧データ], "占い解釈":[占い解釈一覧データ]}
# な辞書を作る
for i in lines:
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
        f1_u_n.append(f_ele)
        f1_u_r.append(s_ele)
    # 占いバックデータを dict に格納
    elif f == 2:
        f_ele, s_ele = ele.split(" ")
        #print("f_ele: ", f_ele)
        #print("s_ele: ", s_ele)
        f2_u_r.append(f_ele)
        f2_u_ex.append(s_ele)

uranai_user["user_name"] = f1_u_n
uranai_user["uranai_result"] = f1_u_r

uranai_back_data["uranai_result"] = f2_u_r
uranai_back_data["uranai_explanation"] = f2_u_ex

#print(uranai_user)
#print(uranai_back_data)


# "uranai_result"をキーにして2つのテーブルを結合
uranai_user_df = pd.DataFrame(uranai_user)
#print(uranai_user_df)

uranai_back_data_df = pd.DataFrame(uranai_back_data)
#print(uranai_back_data_df)

uranai_db = pd.merge(uranai_user_df, uranai_back_data_df, on='uranai_result')
#print(uranai_db)


# 結果を表示
for i in uranai_db.itertuples():
    print(i.user_name + " " + i.uranai_explanation)
