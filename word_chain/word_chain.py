# coding: utf-8
import sys
import pprint

lines = sys.stdin.readlines()
#print(lines)
member_n, word_n, w_uttered_n = map(int,lines[0].rstrip().split(" "))
print(member_n)
#print(word_n)
#print(w_uttered_n)

# しりとりに使える単語を取得（改行コードを削除）
words = [i.rstrip() for i in lines[1:word_n+1]]
#print(words)

# しりとり
w_uttered = [i.rstrip() for i in lines[w_uttered_n:]]
#print(w_uttered)


# ルール1の判定
# 発言は、単語リストにある K 個の単語のうちのいずれかの単語でなければならない
def includ(word):
    return word in words

# ルール2の判定
# 最初の人以外の発言の頭文字は、直前の人の発言の最後の文字と一緒でなければならない
def check_acronym(index_n, word):
    if index_n >= 1:
        #print("一つ前:", w_uttered[index_n-1])
        #print("一つ前の末尾: ", w_uttered[index_n-1][-1])
        #print("発言ワード: ", word)
        #print("発言ワードの頭文字: ", word[0])
        return w_uttered[index_n-1][-1] == word[0]
    else:
        return True

# ルール3の判定
# 今までに発言された単語を発言してはならない
def non_duplicated(word):
    return word not in u_log

# ルール4の判定
# z で終わる単語を発言してはならない
def non_z(word):
    word_l = word.lower()
    return word_l[-1] != "z"

member_score = {}
check = {}
u_log = []
for i, w in enumerate(w_uttered):
    #print("index: ", i)
    #print("member_id: ", i%member_n)
    #print(w)
    #print(u_log)
    rule1 = includ(w)
    rule2 = check_acronym(i,w)
    rule3 = non_duplicated(w)
    rule4 = non_z(w)
    check[i] = {"member_id": i%member_n,
                "rule1":rule1,
                "rule2":rule2,
                "rule3":rule3,
                "rule4":rule4}

    if all([rule1, rule3, rule4]):
        if rule2:
            print("all OK")
            print("id: ", i%member_n)
        else:
            print("rule2: NG")
            member_n -= 1
            print("id: ", i%member_n)
    else:
        print("rule1, rule3, rule4: NG")
        member_n -= 1
        print("id: ", i%member_n)

print(member_n)
#pprint.pprint(check)
#pprint.pprint(member_score)
