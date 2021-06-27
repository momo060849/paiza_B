# coding: utf-8
import sys
from collections import defaultdict

# 履歴数、キャンペーン期間、履歴を取得
lines = sys.stdin.readlines()
# あとで計算するのですべて int に変換
his_n, period_n = list(map(int,lines[0].split(" ")))
history = list(map(int,lines[1].split(" ")))


# 訪問履歴をキャンペーン期間に分け、平均値を取得
visit_ave = {}
for i, h in enumerate(history):
    #print("index_sum: " + str(i+period_n))
    if i+period_n <= len(history):
        cam_period = history[i:i+period_n]
        ave = sum(cam_period)/period_n
        #print("ave: ", ave)
        # キャンペーン期間の訪問者数、開始日、平均訪問者数を格納
        visit_ave[i] = {"campaign_period":cam_period, "start_date":i+1, "visit_average":ave}
#print(visit_ave)


# 訪問者平均の最大値を取得（しきい値）
max_v_average = max([i["visit_average"] for i in visit_ave.values()])
#print(max_v_average)

# キャンペーン候補の数を取得
# 候補数が複数ある場合を想定して開始日を複数取得できるようにする
candidate_n = 0
fastest_date_candidate = []
for i, v in visit_ave.items():
    if v["visit_average"] == max_v_average:
        candidate_n += 1
        fastest_date_candidate.append(v["start_date"])


# 結果を表示
print(candidate_n, min(fastest_date_candidate))